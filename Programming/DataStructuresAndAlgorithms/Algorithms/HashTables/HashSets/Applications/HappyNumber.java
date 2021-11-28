package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets.Applications;
import java.util.HashSet;

/// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.
public class HappyNumber {
    public boolean isHappy(int n) {
        if (n == 1) {
            return true;
        }
        // set keeps track of numbers which have appeared before
        HashSet hashSet = new HashSet();
        while (n != 1) {
            n = sumSquares(n);
            if (n == 1) {
                return true;
            }
            // break if existing in set, because a loop will occur
            if (!hashSet.contains(n)) {
                hashSet.add(n);
            } else {
                break;
            }
        }
        return false;
    }
    private int sumSquares(int n) {
        System.out.println(n);
        // number of digits is log10 x(power to which 10 must be raised to fill x) + 1 
        // casted as int to truncate to zero
        int[] arr = new int[(int) Math.log10(n) + 1];
        
        // get digits from end to start
        for (int i=arr.length-1; i>-1; i--) {
            
            arr[i] = n % 10; // get remainder
            n = (int) n / 10; // update number
        }
        
        int sum = 0;
        for (int digit : arr) {
            sum += digit*digit;
        }
        return sum;
        
    }
}
