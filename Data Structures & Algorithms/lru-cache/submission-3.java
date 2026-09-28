class Node {
    int key;
    int val;
    Node next = null;
    Node prev = null;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private int capacity;
    private Node left = new Node(0,0);
    private Node right = new Node(0,0);
    private Map<Integer, Node> keyToNode = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        left.next = right;
        right.prev = left;
    }

    public void remove(int key) {
        Node node = keyToNode.get(key);
        Node leftNei = node.prev;
        Node rightNei = node.next;

        leftNei.next = rightNei;
        rightNei.prev = leftNei;
    }

    public void insert(int key) {
        Node node = keyToNode.get(key);
        Node rightPrev = right.prev;
        
        rightPrev.next = node;
        node.prev = rightPrev;

        node.next = right;
        right.prev = node;
    }
    
    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return -1;
        }
        remove(key);
        insert(key);
        return keyToNode.get(key).val;
    }
    
    public void put(int key, int value) {
        if (keyToNode.containsKey(key)) {
            remove(key);
            insert(key);
            Node node = keyToNode.get(key);
            node.val = value;
        }
        else {
            Node node = new Node(key, value);
            keyToNode.put(key, node);
            insert(key);

            if (keyToNode.size() > capacity) {
                Node lru = left.next;
                remove(lru.key);
                keyToNode.remove(lru.key);
            }
        }
        
    }
}
