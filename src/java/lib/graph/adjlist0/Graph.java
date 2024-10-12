package graph.adjlist0;

import java.util.ArrayList;
import java.util.List;


/**
 * This class implements a Graph using an Adjacency List representation.
 * Each node in the graph stores a list of adjacent nodes, making this
 * structure efficient for representing sparse graphs.
 */
public class Graph {

    public final List<List<Node>> adjacencyList;

    public Graph(final List<Edge> edges) {

        this.adjacencyList = new ArrayList<>();

        for (int i = 0; i < edges.size(); i++) {
            this.adjacencyList.add(i, new ArrayList<>());
        }            

        for (Edge e: edges) {
            this.adjacencyList.get(e.src).add(new Node(e.dest, e.weight));
        }
    }


    /**
     * Print the Adjaceny List Graph representation
     * 
     */
    public void printGraph() {
        int src = 0;
        final int n = this.adjacencyList.size();

        while (src < n) {
            for (Node edge: this.adjacencyList.get(src)) {
                System.out.print(src + " --> " 
                    + edge.value 
                    + " (" 
                    + edge.weight 
                    + ")\t");
            }

            System.out.println();
            src++;
        }
    }
}
