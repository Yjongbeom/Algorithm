import java.util.*;

public class Main {
    public static int n,m;
    public static int[][] arr;

    public static class Node{
        int x, y, dist;

        public Node(int x, int y, int dist)
        {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }

    public static boolean inRange(int x, int y)
    {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static int bfs()
    {
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};
        boolean[][] visited = new boolean[n][m];

        Queue<Node> queue = new LinkedList<>();

        queue.offer(new Node(0, 0, 1));
        visited[0][0] = true;

        while(!queue.isEmpty())
        {
            Node current = queue.poll();

            if(current.x == n-1 && current.y == m-1)
            {
                return current.dist;
            }

            for(int i=0; i<4; i++)
            {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if(inRange(nx, ny) && arr[nx][ny] == 1 && !visited[nx][ny])
                {
                    visited[nx][ny] = true;
                    queue.offer(new Node(nx, ny, current.dist + 1));
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