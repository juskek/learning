package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;
import java.util.HashMap;
import java.util.Map;

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        // hashMap stores num:index
        // bucket length only 2 despite possibility of multiple locations of a num
        // this works because there can only be one solution
        // so either 
        // 1. summands are in the same position 
        // 2. the array is not part of the valid solution
        // for comprehensiveness, use array or list 
        HashMap<Integer,int[]> hashMap = new HashMap<Integer,int[]>();
        // for each el in nums
        for (int i=0; i<nums.length;i++) {
            // store in hashmap
            if (!hashMap.containsKey(nums[i])) {
                // if key does not exist, add new 
                hashMap.put(nums[i],new int[]{i,-1});
            } else {
                // if key exists, add to existing
                hashMap.put(nums[i],new int[]{hashMap.get(nums[i])[0],i});
            }
        }
            
        
        // for each num in hashmap
        for (Map.Entry<Integer, int[]> entry : hashMap.entrySet()) {
            
            int currentNum = entry.getKey();
            int requiredNum = target - currentNum;
            // check if hashmap contains target - currentNum 
            if (hashMap.containsKey(requiredNum)) {
                if (currentNum==requiredNum) {
                    // if it is in the same position
                    return hashMap.get(currentNum);
                } else {
                    // if it is somewhere else                    
                    return new int[]{hashMap.get(currentNum)[0],hashMap.get(requiredNum)[0]};
                }            
            }
        }
        // return indices 
        return new int[]{-1,-1};
    }
    
}
