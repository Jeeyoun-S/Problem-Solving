import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int N = commands.length;
        int[] answer = new int[N];
        
        for (int i=0; i<N; i++) {
            int[] command = commands[i];
            int start = command[0]-1;
            int end = command[1];
            int index = command[2];
            int[] range = Arrays.copyOfRange(array, start, end);
            Arrays.sort(range);
            // System.out.println(Arrays.toString(range));
            answer[i] = range[index-1];
        }
        
        return answer;
    }
}