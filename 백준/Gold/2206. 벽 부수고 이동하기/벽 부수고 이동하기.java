import java.util.*;

public class Main {
    public static int n, m;
    public static int[][] arr;

    public static class Node {
        int x, y, dist, broken;

        public Node(int x, int y, int dist, int broken) {
            this.x = x;
            this.y = y;
            this.dist = dist;
            this.broken = broken;
        }
    }

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static int bfs() {
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        boolean[][][] visited = new boolean[n][m][2];

        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(0, 0, 1, 0));
        visited[0][0][0] = true;

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.x == n - 1 && current.y == m - 1) {
                return current.dist;
            }

            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if (inRange(nx, ny)) {
                    // 벽이고, 아직 벽을 부순 적이 없는 경우
                    if (arr[nx][ny] == 1 && current.broken == 0 && !visited[nx][ny][1]) {
                        visited[nx][ny][1] = true; // 벽 부순 상태 표시
                        queue.offer(new Node(nx, ny, current.dist + 1, 1));
                    }
                    // 벽이 아니고, 현재 상태로 방문하지 않은 경우
                    else if (arr[nx][ny] == 0 && !visited[nx][ny][current.broken]) {
                        visited[nx][ny][current.broken] = true;
                        queue.offer(new Node(nx, ny, current.dist + 1, current.broken));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        arr = new int[n][m];

        for(int i=0; i<n; i++)
        {
            String line = sc.nextLine();
            for(int j=0; j<m; j++)
            {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        int result = bfs();

        System.out.println(result);


    }
}