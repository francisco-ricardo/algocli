
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import graph.adjlist.Edge;
import graph.adjlist.Graph;

/**
 * Test program for the Adjacency List Graph implementation
 */
public class Main {
    public static void main(String[] args) {

        final List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 6));
        edges.add(new Edge(1, 2, 7));
        edges.add(new Edge(2, 0, 5));
        edges.add(new Edge(2, 1, 4));
        edges.add(new Edge(3, 2, 10));
        edges.add(new Edge(4, 5, 1));
        edges.add(new Edge(5, 4, 3));

        final Graph graph = new Graph(edges);
        graph.printGraph();
    }
}