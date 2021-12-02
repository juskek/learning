package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashMaps.Applications.KeyDesign;

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:
// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.

import java.util.HashMap;
import java.util.HashSet;

public class ValidSudoku {
    private HashSet<Integer> addToSet(HashSet<Integer> set,int value) {
        set.add(value);
        return set;
    }
    public boolean isValidSudoku(char[][] board) {
        // there are three maps
        // rowMap {rowNo : {nums}} which stores the existing nums for each row
        // colMap {colNo : {nums}} which stores the existing nums for each col
        // boxMap {boxNo : {nums}} which stores the existing nums for each box
        HashMap<Integer,HashSet<Integer>> rowMap = new HashMap<Integer,HashSet<Integer>>();
        HashMap<Integer,HashSet<Integer>> colMap = new HashMap<Integer,HashSet<Integer>>();
        HashMap<Integer,HashSet<Integer>> boxMap = new HashMap<Integer,HashSet<Integer>>();
        
        int boxHeight=3;
        int boxWidth=3;
        
        // for each cell
        for (int i=0;i<board.length;i++) {
            // row i
            for (int j=0;j<board[i].length;j++) {
                // col j
                if (board[i][j] == '.') {
                    continue;
                }
                int value = board[i][j];
                int box=(i/boxHeight) * boxHeight + (j/boxWidth);
                
                // init set
                if (!rowMap.containsKey(i)) {
                    rowMap.put(i,new HashSet<Integer>());
                }
                if (!colMap.containsKey(j)) {
                    colMap.put(j,new HashSet<Integer>());
                }
                if (!boxMap.containsKey(box)) {
                    boxMap.put(box,new HashSet<Integer>());
                }
                
                if ((!rowMap.get(i).contains(value)) && (!colMap.get(j).contains(value)) && (!boxMap.get(box).contains(value))) {
                    // if value does not exist in any of the three maps
                    // add to sets
                    rowMap.put(i,addToSet(rowMap.get(i),value));
                    colMap.put(j,addToSet(colMap.get(j),value));
                    boxMap.put(box,addToSet(boxMap.get(box),value));
                } else {
                    // one of the maps already has the value
                    return false;
                }
            }
        }
        // if all values are added without conflict
        return true;
    }
}
