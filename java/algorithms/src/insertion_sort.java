import java.util.ArrayList;
import java.util.Collections;

public class insertion_sort {
    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        Collections.addAll(l, 3, 4, 5, 7, 6, 3); // 6 records in total
        i_sort_alg(l);
    }

    public static ArrayList<Integer> i_sort_alg(ArrayList<Integer> l) {
        for(int j=0; j<l.size(); j++) {
            int Key = l.get(j);
            int i = j - 1;
            while (i > -1 && l.get(i) > Key) {
                 l.set(i+1, l.get(i)); /// make value after i = value in i
                i = i - 1;
            }
            l.set(i+1, Key);

        }
        System.out.println(l);
        return l;
    }
}
