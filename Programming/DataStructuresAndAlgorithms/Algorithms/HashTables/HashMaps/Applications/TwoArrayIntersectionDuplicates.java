package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;
// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

import java.util.HashMap;
import java.util.ArrayList;

public class TwoArrayIntersectionDuplicates {
    public int[] intersect(int[] nums1, int[] nums2) {
        // There are 
        // two maps {num, freq} to store the number of times each num appears in each array
        HashMap<Integer,Integer> map1 = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> map2 = new HashMap<Integer,Integer>();
        // populate nums1 map
        for (int num:nums1) {
            if (!map1.containsKey(num)) {
                // num not stored yet
                map1.put(num,1);
            } else {
                // num stored before, add to count
                map1.put(num,map1.get(num) +1);
            }
        }
        // populate nums2 map
        for (int num:nums2) {
            if (!map2.containsKey(num)) {
                // num not stored yet
                map2.put(num,1);
            } else {
                // num stored before, add to count
                map2.put(num,map2.get(num) +1);
            }
        } 
        ArrayList<Integer> intersect = new ArrayList<Integer>();
        // check whether nums in map1 are in map2
        for (int num : map1.keySet()) {
            if (map2.containsKey(num)) {
                // if they are, get min count and store         
                int reps = Math.min(map1.get(num),map2.get(num));
                for (int i=0;i<reps;i++) {
                    intersect.add(num);
                }
            }
            // else do nothing
        } 
        // return intersect.toArray(new int[]); // cannot be used cause toArray returns Object[]
        return intersect.stream().mapToInt(i -> i).toArray();        
    }
}
