package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets.Applications;
import java.util.HashSet;

/// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
public class SingleNumber {
    public int singleNumber(int[] nums) {
        // Time complexity O(n)
        // Space complexity O(1)
        // for every num
        HashSet<Integer> hashSet = new HashSet<Integer>();
        for (int num : nums) {
            if (!hashSet.contains(num)) {
                // add to set if it is not in there
                hashSet.add(num);
            } else if (hashSet.contains(num)) {
                // remove from set if it is in there 
                hashSet.remove(num);
            }
        }
        
        // check remaining number which would not have been removed since it does not have a duplicate
        for (int ele : hashSet) {
            return ele; // will only return first element in hashset, assumes only one number does not have duplicate
        }
        return -1;
        
    }
    
}
