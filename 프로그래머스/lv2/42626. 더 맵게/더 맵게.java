import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int s : scoville) queue.add(s);
        
        while (!queue.isEmpty()) {
            int last = queue.remove();
            if (last >= K) return answer;
            if (queue.isEmpty()) return -1;
            
            int lastBefore = queue.remove();
            queue.add(last + (lastBefore * 2));
            answer++;
        }
        
        return -1;
    }
}