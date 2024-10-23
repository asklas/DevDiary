import java.util.*;

public class Solution {
    
    private static int[] info;
    private static List<int[]> edges;
    private static int[] visited;
    private static List<Integer> answer = new ArrayList<>();
    
    public int solution(int[] info, int[][] edges) {
        Solution.info = info;
        Solution.edges = new ArrayList<>();
        for (int[] edge : edges) {
            Solution.edges.add(edge);
        }
        visited = new int[info.length];
        
        visited[0] = 1;
        dfs(1, 0);
        
        return Collections.max(answer);
    }
    
    private static void dfs(int sheep, int wolf) {
        if (sheep > wolf) {
            answer.add(sheep);
        } else {
            return;
        }
        
        for (int[] edge : edges) {
            int p = edge[0];
            int c = edge[1];
            if (visited[p] == 1 && visited[c] == 0) {
                visited[c] = 1;
                if (info[c] == 0) {
                    dfs(sheep + 1, wolf);
                } else {
                    dfs(sheep, wolf + 1);
                }
                visited[c] = 0;
            }
        }
    }
}
