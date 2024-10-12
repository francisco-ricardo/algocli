package graph.adjlist;

import java.util.*;

public class Graph {

    private final Map<Integer, List<Node>> adjacencyList = new HashMap<>();

    public Graph(final List<Edge> edges) {
        for (Edge edge : edges) {
            adjacencyList
                .computeIfAbsent(edge.getSource(), x -> new ArrayList<>())
                .add(new Node(edge.getDestination(), edge.getWeight()));
        }
    }

    public void printGraph() {
        adjacencyList.forEach((key, nodes) -> {
            System.out.print("Vertex " + key + ":");
            nodes.forEach(node -> System.out.print(" -> " + node.getValue() + " (Weight: " + node.getWeight() + ")"));
            System.out.println();
        });
    }
}
