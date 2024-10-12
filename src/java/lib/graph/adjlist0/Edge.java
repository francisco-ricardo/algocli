package graph.adjlist0;

/**
 * This class represents an edge in the graph.
 * Each edge connects two nodes (vertices) and also store 
 * the weight property.
 */
public class Edge {
    public int src, dest, weight;

    public Edge(final int src, final int dest, final int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
}
