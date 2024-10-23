import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public static int[] solution(String[] operations) {
        List<Integer> list = new ArrayList<>();
        
        for (String op : operations) {
            String[] parts = op.split(" ");
            String oper = parts[0];
            int num = Integer.parseInt(parts[1]);

            if (oper.equals("I")) {
                list.add(num);
                Collections.sort(list);
            } else if (oper.equals("D") && !list.isEmpty()) {
                if (num == -1) {
                    list.remove(0);
                } else if (num == 1) {
                    list.remove(list.size() - 1);
                }
            }
        }

        if (!list.isEmpty()) {
            return new int[]{list.get(list.size() - 1), list.get(0)};
        } else {
            return new int[]{0, 0};
        }
    }
}
