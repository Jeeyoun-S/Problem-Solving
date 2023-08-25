import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        
        Stack<Integer> stack = new Stack<>();
        
        for (int a : arr) {
            if (stack.isEmpty()) {
                stack.push(a);
                continue;
            }
            int top = stack.peek();
            if (top == a) continue;
            stack.push(a);
        }

        return stack.stream().mapToInt(x -> x).toArray();
    }
}