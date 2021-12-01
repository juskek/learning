package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;
// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

import java.util.HashMap;
import java.util.HashSet;

public class FirstUniqueCharacterInString {
    public int firstUniqChar(String s) {
        // There are two data structures
        // map {character: index} which stores the character and its index
        // index is set to -1 if there are duplicate characters
        // set {character} which stores unique characters
        
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        HashSet<Character> set = new HashSet<Character>(); 
        
        for (int i=0;i<s.length();i++) {
            if (!map.containsKey(s.charAt(i))) {
                // no duplicates
                map.put(s.charAt(i),i);
                set.add(s.charAt(i));
            } else {
                // repeating character
                map.put(s.charAt(i),-1);
                set.remove(s.charAt(i));
            }
        }
        int indexUnique = -1;
        if (set.size() == 0) {
            // no unique characters
            return indexUnique;
        } else {
            // unique characters present, find smallest index
            for (char c : set) {
                if (indexUnique==-1) {
                    // not init yet
                    indexUnique = map.get(c);
                } else if (map.get(c) < indexUnique) {
                    indexUnique = map.get(c);
                }
            }
        }
        return indexUnique;
    }
}
