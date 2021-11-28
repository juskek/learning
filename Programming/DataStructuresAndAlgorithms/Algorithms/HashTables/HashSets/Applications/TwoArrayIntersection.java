package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets.Applications;
/// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
import java.util.HashSet;
public class TwoArrayIntersection {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Time complexity: O(2n)
        // Space complexity: O(n)
        // int[] intersect = new int[Math.min(nums1.length,nums2.length)]; // no. of common elements cannot only be as many as shorter arr
        
        // for each el in first arr, find unique elements
        HashSet<Integer> uniqueSet = new HashSet<Integer>();
        for (int num : nums1) {
            if (!uniqueSet.contains(num)) {
                uniqueSet.add(num);
            }
        }
        HashSet<Integer> commonSet = new HashSet<Integer>();
        for (int num : nums2) {
            if (uniqueSet.contains(num)) {
                commonSet.add(num);
            }
        }
        int[] commonArr = new int[commonSet.size()];
        int i = 0;
        for (int el : commonSet) {
            commonArr[i] = el;
            i++;
        }
        return commonArr;
        
    }
}
