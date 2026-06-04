# Linked List Hard Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Hard order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Design Skiplist

LeetCode: [Design Skiplist](https://leetcode.com/problems/design-skiplist/)

Difficulty: Hard

Pattern: Layered Linked Structure

Why It Matters: Tests pointer-rich ordered structure design beyond single-list rewiring.

Skills Tested:
- Recognize that a skiplist supports search, insert, and erase in O(log n) expected by stacking probabilistic express lanes over a sorted linked list.
- State the invariant: each level above the bottom is a sublist of the level below, and a node's level is chosen by repeated coin flips.
- Implement search by walking down levels, inserting predecessors per level.
- Expected time O(log n) per operation, space O(n) expected.

Common Follow-Ups:
- Replace skiplist with a balanced BST (red-black tree) and compare implementation difficulty.
- What if the level distribution must be deterministic.
- How does concurrent access affect the implementation (lock-free skiplist).

## 2. Reverse Nodes in k-Group

LeetCode: [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

Difficulty: Hard

Pattern: Group Reversal With Boundary Tracking

Why It Matters: Tests reversal boundaries and incomplete groups.

Skills Tested:
- Recognize that the algorithm reverses groups of size `k` and leaves the final partial group untouched.
- State the invariant: after reversing the current group, `prevGroupTail` connects to the new head, and the old head becomes the next group's tail.
- Use a dummy head to simplify the first group; pre-check that `k` nodes remain before reversing.
- Time O(n), space O(1) iterative or O(n / k) recursive.

Common Follow-Ups:
- Swap Nodes in Pairs (LC 24) is the `k = 2` case.
- What if the last partial group also reverses (variant).
- How does the answer change with k as a function of position.

## 3. LFU Cache

LeetCode: [LFU Cache](https://leetcode.com/problems/lfu-cache/)

Difficulty: Hard

Pattern: Frequency-Bucketed Doubly Linked Lists

Why It Matters: Advanced cache design with linked buckets.

Skills Tested:
- Recognize that O(1) LFU operations require a hash map of key to node, a hash map of frequency to doubly linked list of nodes, and a tracker of the minimum frequency for eviction.
- State the invariant: every node belongs to exactly one frequency bucket; on access, the node moves to its `freq + 1` bucket.
- Update `minFreq` correctly when the current min bucket empties after an access.
- Time O(1) per operation, space O(capacity).

Common Follow-Ups:
- LRU Cache (LC 146) is the eviction-by-recency simpler cousin.
- What if frequencies must decay over time (sliding window LFU).
- Implement an LFU with TTL where entries also expire by time.

## 4. All O(1) Data Structure

LeetCode: [All O(1) Data Structure](https://leetcode.com/problems/all-oone-data-structure/)

Difficulty: Hard

Pattern: Bucketed Doubly Linked List

Why It Matters: Maintains counts with O(1) key moves.

Skills Tested:
- Recognize that O(1) inc, dec, getMaxKey, getMinKey requires a doubly linked list of count buckets, each holding a set of keys, with a hash map from key to its bucket.
- State the invariant: buckets are linked in strictly increasing count order, so getMin is the head's set and getMax is the tail's set.
- Move a key by removing it from its bucket and inserting into the neighboring bucket (creating one if needed); delete empty buckets.
- Time O(1) per operation, space O(unique keys).

Common Follow-Ups:
- All O(1) with TTL where counts decay periodically.
- What if multi-key updates arrive in a batch.
- How would you persist the structure to disk while keeping operations O(1) amortized.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
