import java.util.*;

public class topological {

    public static void main(String[] args) {
        String[][] wears = new String[][]{
            {"undershorts", "pants"}, 
            {"undershorts", "shoes"}, 
            {"socks", "shoes"}, 
            {"pants", "shoes"}, 
            {"pants", "belt"}, 
            {"shirt", "belt"}, 
            {"shirt", "tie"}, 
            {"tie", "jacket"}, 
            {"belt", "jacket"}
        };
        String[] parts = new String[]{"undershorts", "pants", "belt", "shirt", "tie", "jacket", "socks", "shoes", "watch"};

        List<String> res = topological_bfs(parts, wears);
        System.out.println("topo bfs result:");
        for(int i=0;i<res.size();i++) {
            String s = res.get(i);
            if(i<res.size()-1) {
                System.out.print(s+"->");
            } else {
                System.out.print(s+"\n");
            }
        }

        List<String> res2 = topological_dfs(parts, wears);
        System.out.println("topo dfs result:");
        for(int i=0;i<res2.size();i++) {
            String s = res2.get(i);
            if(i<res2.size()-1) {
                System.out.print(s+"->");
            } else {
                System.out.print(s+"\n");
            }
            
        }
    }

    public static List<String> topological_bfs(String[] parts, String[][] wears) {
        Map<String, List<String>> graph = build_graph(parts, wears);
        Map<String, Integer> in_degree_graph = build_in_degree(parts, wears);

        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        List<String> answer = new LinkedList<>();

        for(String part:parts) {
            if(in_degree_graph.get(part) == 0) {
                queue.offer(part);
            }
        }

        while(!queue.isEmpty()) {
            // 1. get current part
            String part = queue.poll();
            if(visited.contains(part)) continue;
            visited.add(part);

            // 2. remove the part from graph
            in_degree_graph.remove(part);

            // 3. update inDegree for the other nodes
            for(String adj:graph.get(part)) {
                in_degree_graph.put(adj, in_degree_graph.get(adj)-1);
                if(in_degree_graph.get(adj) == 0) {
                    queue.offer(adj);
                }
            }

            // 4. append the result
            answer.add(part);
        }

        return answer;
    }

    public static List<String> topological_dfs(String[] parts, String[][] wears) {
        Map<String, List<String>> graph = build_graph(parts, wears);
        LinkedList<String> answer = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        for(String part:parts) {
            if(!visited.contains(part)) {
                dfs(graph, answer, visited, part, "");
            }
        }
        return answer;
    }

    private static void dfs(Map<String, List<String>> graph, LinkedList<String> answer, Set<String> visited, String cur, String prev) {
        if(visited.contains(cur)) return;
        visited.add(cur);
        for(String next:graph.get(cur)) {
            if(next==prev) continue;
            else {
                dfs(graph, answer, visited, next, cur);
            }
        }
        answer.addFirst(cur);
    }

    private static Map<String, List<String>> build_graph(String[] parts, String[][] wears) {
        Map<String, List<String>> map = new HashMap<>();
        for(String part: parts) {
            map.put(part, new LinkedList<>());
        }

        for(String[] wear: wears) {
            map.get(wear[0]).add(wear[1]);
        }
        return map;
    }

    private static Map<String, Integer> build_in_degree(String[] parts, String[][] wears) {
        Map<String, Integer> map = new HashMap<>();
        for(String part: parts) {
            map.put(part, 0);
        }

        for(String[] wear: wears) {
            map.put(wear[1], map.getOrDefault(wear[1], 0)+1);
        }

        return map;
    }
    
}
