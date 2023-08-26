import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.valueOf(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] values = new long[N];
        for (int i=0; i<N; i++) values[i] = Long.valueOf(st.nextToken());
        Arrays.sort(values);

        long result = Long.MAX_VALUE;
        long[] list = new long[3];

        indexLoop:
        for (int j=0; j<N; j++) {
            int start = 0; int end = N-1;
            while (start < end) {
                if (start == j) start++;
                else if (end == j) end--;
                else {
                    long total = values[j] + values[start] + values[end];
//                    System.out.printf("%d %d %d \n", values[j], values[start], values[end]);

                    if (total == 0) {
                        list = new long[] {values[j], values[start], values[end]};
                        break indexLoop;
                    }

                    if (result > Math.abs(total)) {
                        result = Math.abs(total);
                        list = new long[] {values[j], values[start], values[end]};
                    }

                    if (total > 0) end--;
                    else start++;

                }
            }
        }

        Arrays.sort(list);
        System.out.printf("%d %d %d\n", list[0], list[1], list[2]);
    }
}