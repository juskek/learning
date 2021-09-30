
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;

public class JavaTest {
    public static void main(String[] mainArgs) {
        System.out.println("Hello World!");
        String text = "M 0,130.96875 270.93333,20.93333 70.9333,54.232 2e-5,4";
        ArrayList<Integer> indices = stringPatternFinder("\\p{Blank}", text);

        String set = ""; // one set per space
        int noSets;
        double[][] args;
        System.out.println("Text Length:" + text.length());
        System.out.println("Last Index From Indices:" + indices.get(indices.size()-1));
        if (indices.get(indices.size() - 1) == text.length()-1) {
            // space is at last position
            // no arg following
            noSets = indices.size() - 1;
            args = new double[indices.size() - 1][2]; // at most 2 args per set
        } else {
            noSets = indices.size();
            args = new double[indices.size()][2]; // at most 2 args per set
        }

        // for each space,
        for (int i = 0; i < noSets; i++) {
            if (i < noSets - 1) {
                // if not the last element
                // get set, split by spaces
                set = text.substring(indices.get(i), indices.get(i + 1));
                System.out.println("Found set :" + set);
            } else {
                // get remaining string
                set = text.substring(indices.get(i));
                System.out.println("Found set :" + set);
            }

            // get args
            if (set.indexOf(',') != -1) {
                // if present, split by comma
                args[i][0] = Double.parseDouble(set.split(",")[0]);
                args[i][1] = Double.parseDouble(set.split(",")[1]);
                System.out.println("Arg 1 :" + args[i][0]);
                System.out.println("Arg 2 :" + args[i][1]);
                System.out.println("Arg 1 * 2 :" + args[i][1]*args[i][0]);
            } else {
                args[i][0] = Double.parseDouble(set);
                System.out.println("Arg :" + args[i][0]);
            }

        }
    }

    public static ArrayList<Integer> stringPatternFinder(String pattern, String text) {
        ArrayList<Integer> indices = new ArrayList<Integer>();

        Matcher m = Pattern.compile(pattern).matcher(text);
        boolean matchFound = m.find();
        while (matchFound) {
            // if match found,
            if (matchFound) {
                // store index
                indices.add(m.start());
                // break loop if current index is last element
                if (m.start() > text.length() - 1) {
                    break;
                } else {
                    // else, find next
                    matchFound = m.find(m.start() + 1);
                }
            }
        }
        return indices;
    }
}