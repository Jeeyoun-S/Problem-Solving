import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.valueOf(st.nextToken());
        int M = Integer.valueOf(st.nextToken());

        int[][] maps = new int[N][M];
        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split("");
//            System.out.println(Arrays.toString(row));
            for (int j=0; j<M; j++) maps[i][j] = Integer.valueOf(row[j]);
        }

        int[][][] distances = new int[N][M][2];
        distances[0][0][0] = 1;

        int[][] delta = new int[][] { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { 0, 0, 1, 0 });

        int result = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int[] infos = queue.remove();
            int x = infos[0]; int y = infos[1];
            int cost = infos[2]; int isBroken = infos[3];

            if (x == N-1 && y == M-1) {
                result = Math.min(result, cost);
                continue;
            }

            for (int[] d : delta) {
                int xx = x+d[0]; int yy = y+d[1];
                if (xx < 0 || xx >= N || yy < 0 || yy >= M) continue;

                if (maps[xx][yy] == 0) {
                    if (isBroken == 0 && (distances[xx][yy][0] > cost+1 || distances[xx][yy][0] == 0)) {
                        distances[xx][yy][0] = cost+1;
                        queue.add(new int[] { xx, yy, cost+1, isBroken });
                    } else if (isBroken == 1 && (distances[xx][yy][1] > cost+1 || distances[xx][yy][1] == 0)) {
                        distances[xx][yy][1] = cost+1;
                        queue.add(new int[] { xx, yy, cost+1, isBroken });
                    }
                } else if (isBroken == 0 && (distances[xx][yy][1] > cost+1 || distances[xx][yy][1] == 0)) {
                    distances[xx][yy][1] = cost+1;
                    queue.add(new int[] { xx, yy, cost+1, 1 });
                }
            }
        }

        if (result == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(result);
    }
}