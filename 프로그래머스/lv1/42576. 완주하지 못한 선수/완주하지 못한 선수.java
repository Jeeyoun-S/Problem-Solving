import java.lang.*;
import java.io.*;
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hm = new HashMap<>();
        for (String c : completion) {
            if (!hm.containsKey(c)) hm.put(c, 1);
            else hm.put(c, hm.get(c) + 1);
        }
        
        for (String p : participant) {
            if (!hm.containsKey(p)) return p;
            int num = hm.get(p);
            if (num > 0) hm.put(p, num-1);
            else return p;
        }
        
        return "";
    }
}