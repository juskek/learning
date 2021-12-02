package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets.Applications;
// You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
// Letters are case sensitive, so "a" is considered a different type of stone from "A".

import java.util.HashSet;
public class JewelsAndStones {
    public int numJewelsInStones(String jewels, String stones) {
        // add jewels to encylopedia of jewels
        HashSet<Character> jewelSet = new HashSet<Character>();
        for (int i=0; i<jewels.length();i++) {
            if (!jewelSet.contains(jewels.charAt(i))) {
                // add
                jewelSet.add(jewels.charAt(i));
            }
        }
        // count how many jewels out of stones
        int noJewels = 0;
        for (int i=0; i<stones.length();i++) {
            if (jewelSet.contains(stones.charAt(i))) {
                // stone is a jewel
                noJewels++;
            }
        }
        return noJewels;
    }
}
