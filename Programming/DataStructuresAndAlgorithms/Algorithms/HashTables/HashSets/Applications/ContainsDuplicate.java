package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets.Applications;
/// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

import java.util.HashSet;
class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        HashSet hashSet = new HashSet();
        for (int num : nums) {
            // if num is in hashset return true
            if (hashSet.contains(num)) {
                return true;
            }
            hashSet.add(num); // else add to hashset and check next
        }
        return false; // if no duplicates        
    }
}