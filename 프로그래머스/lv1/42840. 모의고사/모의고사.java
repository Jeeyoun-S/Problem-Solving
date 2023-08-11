import java.util.*;
import java.io.*;
import java.lang.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] scores = new int[3];
        
        for (int i=0; i<answers.length; i++) {
            int answer = answers[i];
            // 1번
            int rest = i % 5 + 1;
            if (rest == answer) scores[0]++;
            // 2번
            int rest2 = i % 2;
            if (rest2 == 0) {
                if (answer == 2) scores[1]++;    
            } else {
                int rest3 = (i / 2) % 4;
                if (rest3 == 0 && answer == 1) scores[1]++;
                else if (rest3 == 1 && answer == 3) scores[1]++;
                else if (rest3 == 2 && answer == 4) scores[1]++;
                else if (rest3 == 3 && answer == 5) scores[1]++;
            }
            // 3번
            int rest4 = (i / 2) % 5;
            if (rest4 == 0 && answer == 3) scores[2]++;
            else if (rest4 == 1 && answer == 1) scores[2]++;
            else if (rest4 == 2 && answer == 2) scores[2]++;
            else if (rest4 == 3 && answer == 4) scores[2]++;
            else if (rest4 == 4 && answer == 5) scores[2]++;
        }
        // System.out.println(Arrays.toString(scores));
        
        int max_value = 0;
        List<Integer> list = new ArrayList<>();
        for (int i=0; i<3; i++) {
            if (scores[i] > max_value) {
                list.clear();
                list.add(i);
                max_value = scores[i];
            }
            else if (scores[i] == max_value) {
                list.add(i);
            }
        }
        // System.out.println(list.toString());
        
        // int[] result = new int[3];
        // System.out.println(list.size());
        int N = list.size();
        int[] result = new int[N];
        for (int i=0; i<N; i++) result[i] = list.get(i)+1;
        
        return result;
    }
}