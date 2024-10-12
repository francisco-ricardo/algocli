import graph.adjlist.Edge;
import graph.adjlist.Graph;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 6));
        edges.add(new Edge(1, 2, 7));
        edges.add(new Edge(2, 0, 5));
        edges.add(new Edge(2, 1, 4));
        edges.add(new Edge(3, 2, 10));
        edges.add(new Edge(4, 5, 1));
        edges.add(new Edge(5, 4, 3));

        Graph graph = new Graph(edges);
        graph.printGraph();
    }
}
