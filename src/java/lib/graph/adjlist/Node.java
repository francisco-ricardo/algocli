package graph.adjlist;



public class Node {
    private final int value;
    private final int weight;

    public Node(final int value, final int weight) {
        this.value = value;
        this.weight = weight;
    }

    public int getValue() {
        return value;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return String.format("Node(value=%d, weight=%d)", value, weight);
    }
}
