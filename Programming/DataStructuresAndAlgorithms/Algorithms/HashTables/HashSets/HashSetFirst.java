package Programming.DataStructuresAndAlgorithms.Algorithms.HashTables.HashSets;

public class HashSetFirst {
    // Time: insertion O(1), retrieval O(1)
    // Space: O(n)
    private int buckets;
    private double loadThresh = 0.8;
    private int probeThresh = 10; 
    private int elements;
    private Integer[] hashSet; // init as obj for default of null, as primitive default val is 0
    private boolean rehash;
    
    
    public HashSetFirst() {
        buckets = 10;
        probeThresh = 10;
        elements = 0;
        rehash = false;
        hashSet = new Integer[buckets];
    }
    
    // Hash function
    // Input: Key
    // Returns: Hashcode 
    private int hash(int key) {
        int hashCode = key % buckets;
        return hashCode;
    }
    
    // Linear Probing Add 
    // checks for nulls
    private int linProbeAdd(int hashCode,int key) {
        int probeCount = 0;
        int altHashCode = hashCode;
        
        for (int i=0;i<hashSet.length;i++) {
            // resetting bucket to start if reached end
            if (altHashCode == hashSet.length-1) {
                // reached end of hashcodes 
                altHashCode = -1; // restart at beginning
            }
            altHashCode++;
            probeCount++;
            // rehashing if probe iterations exceed threshold
            if (probeCount >= 10) {
                rehash = true;
            }
            // checking if alt bucket found
            if ((hashSet[altHashCode] == null)) {
                return altHashCode;
            } // else do nothing 
        }
        return -1; // invalid arr position
    }

    // Linear Probing Find
    // checks non-null and checks if it is the same key
    private int linProbeFind(int hashCode, int key) {
        int probeCount = 0;
        int altHashCode = hashCode;
        
        for (int i=0;i<hashSet.length;i++) {
            
            // resetting bucket to start if reached end
            if (altHashCode == hashSet.length-1) {
                // reached end of hashcodes 
                altHashCode = -1; // restart at beginning
            }
            // skip current hashCode
            altHashCode++;
            probeCount++;

            // checking if alt bucket found
            if ((hashSet[altHashCode] != null) && (hashSet[altHashCode] == key)) {
                return altHashCode;
            } // else do nothing 
        }
        return -1; // invalid arr position
    }
    
    private void rehashSet() {
        rehash = false;
        HashSetFirst newHashSet = new HashSetFirst(); 
        
        newHashSet.buckets = this.buckets*2;
        newHashSet.hashSet = new Integer[newHashSet.buckets];

        for (int i=0; i<hashSet.length;i++) {
            if (hashSet[i] != null) {
                newHashSet.add(hashSet[i]);    
            }
        }
        this.hashSet = newHashSet.hashSet;
        this.buckets = newHashSet.buckets;
        
    }
    
    public void add(int key) {
        // rehash if load factor above threshold
        if (elements/hashSet.length > loadThresh) {
            rehash = true;
        }
        if (rehash == true) {
            rehashSet();
        }
        // hash and insert if null
        int hashCode = hash(key);
        
        if (hashSet[hashCode] == null) {
            // add 
            hashSet[hashCode] = key;
            elements++;
        } else if (hashSet[hashCode] != key) {
            // not equal to null, and is not equal to key
            // collision 
            int altHashCode = linProbeAdd(hashCode,key);
            if (altHashCode != -1) {
                hashSet[altHashCode] = key;
                elements++;
            }
            
        }
    }
    
    public void remove(int key) {
        int hashCode = hash(key);
        if (hashSet[hashCode] != null) {
            if (hashSet[hashCode] == key) {
                // remove
                hashSet[hashCode] = null;
                elements--;    
            } else if (hashSet[hashCode] != key) {
                // collision
                int altHashCode = linProbeFind(hashCode,key);
                if (altHashCode != -1) {
                    hashSet[altHashCode] = null;
                    elements--;
                }
            }
            
        }
    }
    
    public boolean contains(int key) {
        int hashCode = hash(key);
        if (hashSet[hashCode] != null) {
            if (hashSet[hashCode] == key) {
                return true;
            } else {
                // collision
                int altHashCode = linProbeFind(hashCode,key);
                if (altHashCode != -1) {
                    return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your HashSetFirst object will be instantiated and called as such:
 * HashSetFirst obj = new HashSetFirst();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
