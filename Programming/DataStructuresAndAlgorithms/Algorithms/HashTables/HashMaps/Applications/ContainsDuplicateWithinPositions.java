package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;

// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

import java.util.HashMap;
import java.util.ArrayList;

public class ContainsDuplicateWithinPositions {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // There is 
        // one map: {num: index[]} storing the numbers which appeared and their positions
        
        HashMap<Integer,ArrayList<Integer>> map = new HashMap<Integer,ArrayList<Integer>>();
        
        // populate map with nums and positions
        for (int i=0;i<nums.length;i++) {
            if (!map.containsKey(nums[i])) {
                // new entry
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(i);
                map.put(nums[i],temp);
            } else {
                // existing entry, append new position
                ArrayList<Integer> temp = map.get(nums[i]);
                temp.add(i);
                map.put(nums[i],temp);
            }
        }
        // check distance between duplicates within map
        for (int num : map.keySet()) {
            ArrayList<Integer> positions = map.get(num);
            if (positions.size()!=-1) {
                // there are duplicates
                for (int i=0;i<positions.size()-1;i++) {
                    // stops at -1 for second last element
                    int j=i+1;
                    if (Math.abs((positions.get(i)-positions.get(j))) <= k) {
                        return true;
                    } 
                }
            }
        }
        return false;
    }
}
