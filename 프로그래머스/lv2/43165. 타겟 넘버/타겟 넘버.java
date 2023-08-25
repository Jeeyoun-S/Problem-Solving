import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        hm.put(0, 1);
        
        for (int number : numbers) {
            HashMap<Integer, Integer> newhm = new HashMap<>();
            for (int key : hm.keySet()) {
                int num = hm.get(key);
                
                int plus = key + number;
                if (newhm.containsKey(plus)) newhm.put(plus, newhm.get(plus) + num);
                else newhm.put(plus, num);
                
                int minus = key - number;
                if (newhm.containsKey(minus)) newhm.put(minus, newhm.get(minus) + num);
                else newhm.put(minus, num);
            }
            hm = newhm;
        }
        
        if (hm.containsKey(target)) return hm.get(target);
        return 0;
    }
}