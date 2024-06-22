import java.util.Arrays;
import java.util.Stack;

public class depth_first_serarch {
    private static int[][] graph_no_cycle;
    private static int[][] graph_with_cycle;

    public static void main(String[] args) {
        graph_no_cycle = new int[][]{{1,2,4},{3},{3},{},{1,2}};
        graph_with_cycle = new int[][]{{1,2},{3},{3},{4},{0,2}};
        int[] visited1 = new int[graph_no_cycle.length];
        boolean cycleResult1 = hasCycle(graph_no_cycle, visited1, 0, -1, new Stack<Integer>());
        // output: [2, 2, 2, 2, 2]
        System.out.println(Arrays.toString(visited1));
        // output: false
        System.out.println(cycleResult1);

        int[] visited2 = new int[graph_with_cycle.length];
        boolean cycleResult2 = hasCycle(graph_with_cycle, visited2, 0, -1, new Stack<Integer>());
        // output: [2, 2, 2, 2, 2]
        System.out.println(Arrays.toString(visited2));
        // output: true
        System.out.println(cycleResult2);
    }

    public static boolean hasCycle(int[][] graph, int[] color, int cur, int prev, Stack<Integer> stk) {
        if(color[cur]==1) {
            stk.push(cur);
            // This will ONLY print part of cycles, not all cycles
            // output:
            // cycle: 0->1->3->4->0
            // cycle: 3->4->2->3
            System.out.println("cycle: "+getCycle(stk));
            stk.pop();
            return true;
        }
        else if(color[cur]==2) return false;
        else {
            color[cur] = 1;
            stk.push(cur);
            boolean ans = false;
            for(int w:graph[cur]) {
                // pay attention to this line, we cannot go
                // back to parent node and find a "cycle"!
                if(w==prev) continue;
                else {
                    boolean res = hasCycle(graph, color, w, cur, stk);
                    ans = ans||res;
                }
            }
            color[cur] = 2;
            stk.pop();
            return ans;
        }
    }

    private static String getCycle(Stack<Integer> stk) {
        Stack<Integer> tmp = new Stack<>();
        int top = stk.pop();
        tmp.push(top);
        String res = "->"+top;
        while(!stk.isEmpty()&&stk.peek()!=top) {
            int e = stk.pop();
            res = "->"+e+res;
            tmp.push(e);
        }
        int e = stk.pop();
        res = e+res;
        tmp.push(e);
        while(!tmp.isEmpty()) {
            stk.push(tmp.pop());
        }
        return res;
    }
    
}
