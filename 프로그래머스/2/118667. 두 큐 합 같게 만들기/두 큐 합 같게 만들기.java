import java.util.LinkedList;
import java.util.Queue;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long v1 = IntStream.of(queue1).sum();
        long v2 = IntStream.of(queue2).sum();
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for (int i = 0; i < queue1.length; i++) {
            q1.offer(queue1[i]);
            q2.offer(queue2[i]);
        }

        if (v1 == v2) {
            return 0;
        }

        int maxOperations = 2 * (queue1.length + queue2.length);

        while (answer < maxOperations) {
            if (v1 > v2) {
                int val = q1.poll();  
                v1 -= val;
                q2.offer(val);
                v2 += val;
            } else {
                int val = q2.poll();
                v2 -= val;
                q1.offer(val);
                v1 += val;
            }

            answer++;
            if (v1 == v2) {
                return answer;
            }
        }

        return -1;
    }
}
