
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Main {
    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
        Set<String> set = new HashSet<>();  // 중복을 제거하기 위해 HashSet 사용

        for (int i = 0; i < count; i++) {
            String str = br.readLine();
            set.add(str);  // Set에 추가하면 자동으로 중복이 제거됨
        }
        br.close();
        
        // Set을 List로 변환하고, 길이 순, 사전순으로 정렬
        List<String> list = set.stream()
                               .sorted(new Comparator<String>() {
                                   @Override
                                   public int compare(String s1, String s2) {
                                       // 첫 번째 기준: 문자열 길이 순으로 정렬
                                       if (s1.length() != s2.length()) {
                                           return s1.length() - s2.length();
                                       }
                                       // 두 번째 기준: 길이가 같으면 사전순으로 정렬
                                       return s1.compareTo(s2);
                                   }
                               })
                               .collect(Collectors.toList());
        
        // 정렬된 문자열 출력
        for (String x : list) {
            System.out.println(x);
        }
    }

    public static void main(String[] args) throws IOException {
        solution();
    }
}
