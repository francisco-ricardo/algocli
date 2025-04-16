"""
Design a data structure that follows the constraints of a Least 
Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive 
size capacity.
- int get(int key) Return the value of the key if the key exists, 
otherwise return -1.
- void put(int key, int value) Update the value of the key if the 
key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

class LRUCache:

    def __init__(self, capacity: int) -> None:
        """
        Initializes the LRU cache with positive size capacity.
        
        Parameters
        ----------
        capacity: the maximum number of items in the cache
        """
        self.capacity = capacity
        self.cache = {}
        self.order = []

    
    def get(self, key: int) -> int:
        """
        Returns the value of the key if the key exists, otherwise 
        returns -1.
        
        Parameters
        ----------
        key: the key to search for
        
        Returns
        -------
        int: the value of the key or -1 if not found
        """
        if key in self.cache:
            # Move the accessed item to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Updates the value of the key if the key exists. Otherwise, 
        adds the key-value pair to the cache. If the number of keys 
        exceeds the capacity from this operation, evicts the least 
        recently used key.
        
        Parameters
        ----------
        key: the key to add or update
        value: the value to associate with the key
        """
        if key in self.cache:
            # Update the value and move to end of order list
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            # Add new key-value pair
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item
                lru_key = self.order.pop(0)
                self.cache.pop(lru_key)
            self.cache[key] = value
            self.order.append(key)
        # The order list maintains the order of keys based on usage
        # The first element is the least recently used key

# EOF