
import java.util.Arrays;
import java.util.PriorityQueue;

public class dijkstra {
    private static int[][][] graph;

    public static void main(String[] args) {
        graph = new int[][][]{{{1,4},{7,8}},{{0,4},{2,8},{7,11}},{{1,8},{3,7},{5,4},{8,2}},{{2,7},{4,9},{5,14}},{{3,9},{5,10}},{{2,4},{3,14},{4,10},{6,2}},{{5,2},{7,1},{8,6}},{{0,8},{1,11},{6,1},{8,7}},{{2,2},{6,6},{7,7}}};
        boolean validateRes = validateGraph(graph);
        System.out.println("the validate result is "+validateRes);
        String path = shortestPath(graph, 1, 8);
        System.out.println(path);
    }

    private static String shortestPath(int[][][] graph, int start, int end) {
        int MAX_VALUE = (int)1e7;
        int n = graph.length;
        int[] distance = new int[n];
        boolean[] visited = new boolean[n];
        int[] prev = new int[n];
        Arrays.fill(distance, MAX_VALUE);
        Arrays.fill(prev, -1);

        // initialization
        // int cur = start;
        distance[start] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2)->Double.compare(o1[1], o2[1]));
        pq.offer(new int[]{start, 0});

        while(!pq.isEmpty()) {
            int[] point = pq.poll();
            int cur = point[0];
            visited[cur] = true;
            int[][] adj = graph[cur];
            // update shortest path
            for(int i=0;i<adj.length;i++) {
                int v = adj[i][0];
                int weight = adj[i][1];
                if(!visited[v] && distance[cur]+weight<distance[v]) {
                    distance[v] = distance[cur]+weight;
                    prev[v] = cur;
                    pq.offer(new int[]{v, distance[v]});
                }
            }
        }
        // find the path
        int cur = end;
        String ans = Integer.toString(cur);
        while(cur!=-1) {
            int last = prev[cur];
            if(last!=-1) {
                ans = last+"->"+ans;
            } else {
                ans = "Distance:"+distance[end]+" path:"+ans;
            }
            cur = last;
        }
        return ans;
    }

    private static boolean validateGraph(int[][][] graph) {
        boolean sign = true;
        for(int i=0;i<graph.length;i++) {
            for(int j=0;j<graph[i].length;j++) {
                int verticle = graph[i][j][0];
                int edge = graph[i][j][1];
                boolean checked = false;
                for(int k=0;k<graph[verticle].length;k++) {
                    if(graph[verticle][k][0]==i) {
                        if(graph[verticle][k][1]==edge) {
                            checked = true;
                        } else {
                            checked = true;
                            sign = false;
                        }
                    }
                }
                if(!checked) {
                    sign = false;
                }
            }
        }

        return sign;
    }
}