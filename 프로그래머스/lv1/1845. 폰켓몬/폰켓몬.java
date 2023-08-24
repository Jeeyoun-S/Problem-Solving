import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int N = nums.length;
        HashSet<Integer> hs = new HashSet<>();
        for (int num : nums) hs.add(num);
        System.out.println(hs.toString());
        return Math.min(hs.size(), N/2);
    }
}