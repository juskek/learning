package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;

public class IsomorphicStrings {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,ArrayList<Integer>> hashMap = new HashMap<Character,ArrayList<Integer>>();
        // check if lengths are the same
        if (s.length() != t.length()) {
            return false;
        }
        // System.out.println("Length check passed");
        // three data structures used
        // map to store char positions {char:[index]}
        // set to track existing characters in map {char}
        // list to store first position where each character appeared [firstIndex,char]
        HashMap<Character,ArrayList<Integer>> sMap = new HashMap<Character,ArrayList<Integer>>();
        HashMap<Character,ArrayList<Integer>> tMap = new HashMap<Character,ArrayList<Integer>>();
        
        HashSet<Character> charSet = new HashSet<Character>();
        
        ArrayList<Object[]> sFirsts = new ArrayList<Object[]>();
        ArrayList<Object[]> tFirsts = new ArrayList<Object[]>();
        
        // populate sMap and sFirsts
        for (int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if (!charSet.contains(c)) {
                // if char not added before
                charSet.add(c);
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(i);
                sMap.put(c,temp);
                sFirsts.add(new Object[]{i,c});
            } else if (charSet.contains(c)) {
                // char added before
                ArrayList<Integer> temp = sMap.get(c);
                temp.add(i);
                sMap.put(c,temp);
            }
        }
        charSet.clear();
        
        // populate tMap and tFirsts
        for (int i=0;i<t.length();i++) {
            char c = t.charAt(i);
            if (!charSet.contains(c)) {
                // if char not added before
                charSet.add(c);
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(i);
                tMap.put(c,temp);
                tFirsts.add(new Object[]{i,c});
            } else if (charSet.contains(c)) {
                // char added before
                ArrayList<Integer> temp = tMap.get(c);
                temp.add(i);
                tMap.put(c,temp);
            }
        }
        
        if (sFirsts.size() != tFirsts.size()) {
            // no of unique characters not equal
            return false;
        }
        System.out.println("Unique character check passed");
        
        // starting from the character in index 0 of each string
        // check if the positions for that character matches, [0,...] == [0,...]
        for (int i=0; i<sFirsts.size(); i++) {
            // get [firstIndex,char]
            Object[] sFirst = sFirsts.get(i);
            Object[] tFirst = tFirsts.get(i);
            
            System.out.println("Character from s: " + sFirst[1]);
            System.out.println("Character from t: " + tFirst[1]);
            // first position of each character should match 
            // e.g. aabbcc vs aabcbc would have passed previous return false
            // 0,2,4 vs 0,2,3
            if (sFirst[0] != tFirst[0]) {
                return false;
            }
            System.out.println("First position check passed");
            
            
            // check arrays of character for each map
            ArrayList<Integer> sPos = sMap.get(sFirst[1]);
            ArrayList<Integer> tPos = tMap.get(tFirst[1]);
            
            // positions should be the same
            if (sPos.size() != tPos.size()) {
                return false;
            } else {
                System.out.println("Number of positions for character check passed");

                for (int j=0; j<sPos.size(); j++) {
                    // if (sPos.get(j) != tPos.get(j)) { // checks for object equality, does not work for values above 128, see caching 
                    if (!(sPos.get(j).equals(tPos.get(j)))) { // checs for value equality
                        return false;
                    }    
                }
                System.out.println("Same positions check passed");
            }
        }
        // else, all checks passed
        return true;
    }
}
