package graph.adjlist0;


/**
 * This class represents a node (vertex) in the graph.
 * Each node stores information about itself, such as a label or value, 
 * and may be connected to other nodes through edges.
 */
public class Node {
    public int value;
    public int weight;

    public Node(final int value, final int weight) {
        this.value = value;
        this.weight = weight;
    }
}

