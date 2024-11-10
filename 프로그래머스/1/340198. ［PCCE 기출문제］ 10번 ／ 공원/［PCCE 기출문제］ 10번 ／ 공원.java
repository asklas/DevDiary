

import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public int solution(int[] mats, String[][] park) {
        int[] sortMat = Arrays.stream(mats)
                .boxed() 
                .sorted(Comparator.reverseOrder())
                .mapToInt(Integer::intValue) 
                .toArray();
        for (int i : sortMat) {
            String[][] tem = createTemplate(i);
            for (int h = 0; h < park.length + 1 - i; h++) {
                for (int v = 0; v < park[h].length + 1 - i; v++) {
                    String[][] subArray = new String[i][i];
                    for (int x = 0; x < i; x++) {
                        for (int y = 0; y < i; y++) {
                            subArray[x][y] = park[h + x][v + y];
                        }
                    }
                    if (Arrays.deepEquals(tem, subArray)) {
                        return i;
                    }
                }
            }
        }
        return -1;
    }

    private String[][] createTemplate(int length) {
        String[][] template = new String[length][length];
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                template[i][j] = "-1";
            }
        }
        return template;
    }
}

