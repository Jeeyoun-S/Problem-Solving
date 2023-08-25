import java.util.*;

class Solution {
    
    static boolean[] primes;
    static int lastIdx;
    
    public boolean isPrime(int number) {
        // if (lastIdx >= number) return !primes[number];
        // for (int 1; i<=number; i++) {
        if (number <= 1) return false;
        else if (number <= 3) return true;
        
        for (int j=2; j<number; j++) {
            if (number%j == 0) return false;
        }
        // }
        return true;
        // lastIdx = number;
        // return !primes[number];
    }
    
    public int backtracking(HashMap<Integer, Integer> hm, ArrayList<Integer> list, int prev) {
        int N = list.size();
        int total = 0;
        
        // System.out.println("prev " + prev);
        for (int i=0; i<N; i++) {
            int num = list.get(i);
            int cnt = hm.get(num);
            if (cnt < 1) continue;
            
            hm.put(num, cnt-1);
            int next = (prev*10) + num;
            
            if (isPrime(next)) total ++;
            if (next != 0) total += backtracking(hm, list, next);
            hm.put(num, cnt);
        }
        return total;
    }
    
    public int solution(String numbers) {
        primes = new boolean[10000000];
        primes[0] = true; primes[1] = true;
        lastIdx = 3;
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i=0; i<numbers.length(); i++) {
            int number = Integer.valueOf(numbers.charAt(i)) - 48;
            if (hm.containsKey(number)) hm.put(number, hm.get(number) + 1);
            else {
                hm.put(number, 1);
                list.add(number);
            }
        }
        System.out.println(list.toString());
        int answer = backtracking(hm, list, 0);
        return answer;
    }
}