import java.util.*;

class Solution {
    public int backtracking(ArrayList<String> types, HashMap<String, Integer> counts, int idx, int prev) {
        // System.out.println("idx " + idx + ", prev " + prev);
        
        int total = 0;
        for (int i=idx; i<types.size(); i++) {
            String type = types.get(i);
            int cnt = counts.get(type);
            total += prev * cnt;
            total += backtracking(types, counts, i+1, prev*cnt);
        }
        return total;
    }
    
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> counts = new HashMap<>();
        
        for (String[] cloth : clothes) {
            String type = cloth[1];

            if (counts.containsKey(type)) counts.put(type, counts.get(type)+1);
            else counts.put(type, 1);
        }
        ArrayList<String> types = new ArrayList<>(counts.keySet());
        // System.out.println(hm.toString());
        int answer = backtracking(types, counts, 0, 1);
        
        return answer;
    }
}