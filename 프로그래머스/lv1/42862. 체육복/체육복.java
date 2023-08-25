import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
      
        ArrayList<Integer> lostArr = new ArrayList<>(lost.length);
        for (int l : lost) lostArr.add(Integer.valueOf(l));
        
        ArrayList<Integer> reserveArr = new ArrayList<>(reserve.length);
        for (int r : reserve) reserveArr.add(Integer.valueOf(r));
        
        Collections.sort(lostArr); Collections.sort(reserveArr);
        
        System.out.println(lostArr.toString());
        System.out.println(reserveArr.toString());
        
        int lostN = lostArr.size(); int reserveN = reserveArr.size();
        int lostIdx = 0; int reserveIdx = 0;
        int total = lostN;
        
        while (lostIdx < lostN && reserveIdx < reserveN) {
            int l = lostArr.get(lostIdx);
            int r = reserveArr.get(reserveIdx);
            System.out.println("l " + l + ", r " + r);
            
            if (l == r) {
                lostIdx++;
                reserveIdx++;
                total--;
            }
            else if (l > r) {
                
                if (reserveIdx+1 < reserveN && reserveArr.get(reserveIdx+1) == l) {
                    lostIdx++;
                    reserveIdx += 2;
                    total--;
                } else if (l == (r+1)) {
                    lostIdx++;
                    reserveIdx++;
                    total--;
                } else {
                    reserveIdx++;
                }
                
            } else {
                if (lostIdx+1 < lostN && lostArr.get(lostIdx+1) == r) {
                    lostIdx += 2;
                    reserveIdx ++;
                    total--;
                } else if (l == (r-1)) {
                    lostIdx++;
                    reserveIdx++;
                    total--;
                } else {
                    lostIdx++;
                }
            }
        }
        
        return n - total;
    }
}