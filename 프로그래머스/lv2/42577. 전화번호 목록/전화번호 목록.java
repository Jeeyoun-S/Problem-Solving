import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        int N = phone_book.length;
        
        if (N < 2) return true;
        
        Arrays.sort(phone_book);
        // System.out.println(Arrays.toString(phone_book));
        int start = 0; int end = 1;
        
        while (start < end && start < N && end < N) {
            // System.out.println("start " + start + ", end " + end);
            
            String A = phone_book[start];
            String B = phone_book[end];
            
            if (A.length() > B.length()) {
                start++;
                if (start == end) end++;
                continue;
            }
            
            // if (A.charAt(0) != B.charAt(0)) {
            //     start++;
            //     if (start == end) end++;
            //     continue;
            // }
            
            boolean isFalse = true;
            
            for (int i=0; i<A.length(); i++) {
                if (A.charAt(i) == B.charAt(i)) continue;
                isFalse = false;
                // if (end == N-1) start++;
                // else end++;
                start++; end++;
                break;
            }
            
            if (isFalse) return false;
        }

        return true;
    }
}