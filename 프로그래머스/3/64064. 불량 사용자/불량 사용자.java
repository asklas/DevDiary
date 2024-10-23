import java.util.HashSet;

class Solution {
    String[] user;
    String[] ban;
    HashSet<HashSet<String>> answer = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        user = user_id;
        ban = banned_id;
        dfs(new HashSet<>(), 0);
        return answer.size();
    }

    void dfs(HashSet<String> set, int idx) {
        if (idx == ban.length) {
            answer.add(new HashSet<>(set));
            return;
        }
        for (String s : user) {
            if (check(s, ban[idx]) && !set.contains(s)) {
                set.add(s);
                dfs(set, idx + 1);
                set.remove(s);
            }
        }
    }

    boolean check(String u, String b) {
        if (u.length() != b.length()) {
            return false;
        }
        for (int i = 0; i < u.length(); i++) {
            if (u.charAt(i) != b.charAt(i) && b.charAt(i) != '*') {
                return false;
            }
        }
        return true;
    }
}