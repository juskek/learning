package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications.KeyDesign;
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;


public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        // there is 
        // one map {sortedString : [string]} which stores the strings against their sorted equivalent
        HashMap<String,ArrayList<String>> map = new HashMap<String,ArrayList<String>>();
        // populate map
        for (String str : strs) {
            String sorted;
            if (str.isEmpty()) {
                // for case ""
                sorted = null;
            } else {
                // sort string
                char[] sortedArray = str.toCharArray();
                Arrays.sort(sortedArray);
                sorted = new String(sortedArray);
            }
            
            if (!map.containsKey(sorted)) {
                // add new key
                ArrayList<String> temp = new ArrayList<String>();
                temp.add(str);
                map.put(sorted,temp);
            } else {
                // append to existing key
                ArrayList<String> temp = map.get(sorted);
                temp.add(str);
                map.put(sorted,temp);
            }
        }
        // append groups 
        List<List<String>> groups = new ArrayList<List<String>>();
        for (String key : map.keySet()) {
            groups.add(map.get(key));
        }
        return groups;
    }
}
