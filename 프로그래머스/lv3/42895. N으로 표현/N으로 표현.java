import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = 0;
        String str = Integer.toString(N);
        
        ArrayList<HashSet<Integer>> dp = new ArrayList<>();
        System.out.println(dp.toString());
        
        for (int i=1; i<=8; i++) {
            HashSet<Integer> hs = new HashSet<>();
            
            String result = "";
            for (int k=0; k<i; k++) result += str;
            hs.add(Integer.valueOf(result));
            System.out.println(dp.toString());
            for (int j=1; j<=i/2; j++) {
                
                System.out.println(j-1 + " " + (i-j-1));
                HashSet<Integer> one = dp.get(j-1);
                HashSet<Integer> two = dp.get(i-j-1);
                
                for (int o : one) {
                    for (int t : two) {
                        hs.add(o+t);
                        hs.add(o-t);
                        hs.add(o*t);
                        if (t != 0) hs.add(o/t);
                        
                        hs.add(t+o);
                        hs.add(t-o);
                        hs.add(t*o);
                        if (o != 0) hs.add(t/o);
                    }
                }
            }
            
            if (hs.contains(number)) return i;
            dp.add(hs);
        }
        
        return -1;
    }
}