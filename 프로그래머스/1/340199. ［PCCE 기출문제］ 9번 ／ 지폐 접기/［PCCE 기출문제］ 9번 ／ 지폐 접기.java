class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int v = 0;
        int h = 0;
        if(wallet[0]>wallet[1]){
            v = wallet[0];
            h = wallet[1];
        } else {
            v = wallet[1];
            h = wallet[0];
        }
        while (Math.max(bill[0],bill[1])>v || Math.min(bill[0],bill[1])>h) {
            if(bill[0]>bill[1]){
                bill[0] = bill[0]/2;
            } else {
                bill[1] = bill[1]/2;
            }
            answer ++;
        }
        return answer;
    }
}