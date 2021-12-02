package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;
// Given a string s, find the length of the longest substring without repeating characters.

import java.util.HashMap;
import java.util.Map;
import java.util.Iterator;

public class LongestSubstringWithoutDuplicates {
    public int lengthOfLongestSubstring(String s) {
        // a window is slid from the start of the string till the end
        // the window starts at size zero
        // and increases in size whenever there is a new character
        // if the character has appeared before, and if it is not the character that just appeared,
            // the window is resized to start at the last time the character appeared + 1, 
            // and end at the current character (shift +resize)
        // if the character has appeared before and is one position before the current position,
            // the window is reset to size 1
        
        // charMap {character : position} tracks the characters that are in the current window and their positions
        // indexMap {position : character} tracks the indices that are in the current window and their characters, used to remove characters from charMap
        HashMap<Character,Integer> charMap = new HashMap<Character,Integer>();
        HashMap<Integer,Character> indexMap = new HashMap<Integer,Character>();
        int start=0;
        int end=0;
        int longest=0;
        
        // for each character c
        for (int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if (!charMap.containsKey(c)) {
                // c has not appeared before
                // add to maps
                charMap.put(c,i);
                indexMap.put(i,c);
                // shift end to increase window size
                end=i;
            } else {
                // c appeared before
                if (charMap.get(c).equals(i-1)) {
                    // right before the current position
                    // reset
                    start=i;
                    end=i;
                    charMap.clear();
                    charMap.put(c,i);
                    indexMap.clear();
                    indexMap.put(i,c);
                } else {
                    // appeared somewhere else
                    // resize start to push out last time c appeared
                    // shift end to include new occurence of c
                    start = charMap.get(c) + 1;
                    end=i;
                    // Set<Integer> keys = indexMap.keySet();
                    // for (int key : keys) {
                    //     if (key < start) {
                    //         charMap.remove(indexMap.get(key));
                    //         // indexMap.remove(key); // does not work due to concurrent modification
                    //     }
                    // }
                    Iterator<Map.Entry<Integer, Character>> iterator = indexMap.entrySet().iterator();

                    // remove out of range characters
                    while (iterator.hasNext()) {
                        // Get the entry at this iteration
                        Map.Entry<Integer, Character> entry = iterator.next();
                        if (entry.getKey() < start) {
                            // out of range
                            charMap.remove(entry.getValue()); 
                            iterator.remove(); // remove from indexMap
                        }
                    }
                    // update map with existing char
                    charMap.put(c,i);
                    indexMap.put(i,c);
                }
            }
            int windowSize = end - start + 1;
            longest = Math.max(longest,windowSize);
        }
        return longest;
    }
    
}
