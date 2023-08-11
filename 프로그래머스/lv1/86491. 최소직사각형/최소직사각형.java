import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public int solution(int[][] sizes) {

        int max_size = 0;
        int min_size = 0;
        
        for (int i=0; i < sizes.length; i++) {
            int[] size = sizes[i];
            max_size = Math.max(max_size, Math.max(size[0], size[1]));
            min_size = Math.max(min_size, Math.min(size[0], size[1]));
        }
        
        return max_size*min_size;
    }
}