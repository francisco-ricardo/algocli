package graph.adjlist;

public class Edge {
    private final int src;
    private final int dest;
    private final int weight;

    public Edge(final int src, final int dest, final int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }

    public int getSource() {
        return src;
    }

    public int getDestination() {
        return dest;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return String.format("Edge(src=%d, dest=%d, weight=%d)", src, dest, weight);
    }
}
