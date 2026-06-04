# Linked List Medium Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Medium order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Add Two Numbers

LeetCode: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

Difficulty: Medium

Pattern: Linked Addition With Carry

Why It Matters: Tests carrying state through linked traversal.

Skills Tested:
- Recognize that digits are stored least-significant-first, so a single pass with running carry sums each pair into a new node.
- State the invariant: `carry` is always 0 or 1 entering each step, and a final non-zero `carry` requires one more node.
- Handle lists of different lengths (treat missing digits as 0) and a final carry-out (append a `1`).
- Time O(max(m, n)), space O(max(m, n)), and contrast with converting both lists to integers (overflow-prone for large inputs).

Common Follow-Ups:
- Add Two Numbers II (LC 445) stores digits most-significant-first; reverse first or use stacks.
- Plus One Linked List (LC 369) is a single-list increment with carry.
- What if the digits are in a different base.

## 2. Remove Nth Node From End of List

LeetCode: [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Difficulty: Medium

Pattern: Two Pointers With Gap

Why It Matters: Core fixed-distance deletion.

Skills Tested:
- Recognize that "n-th from the end" can be located in one pass by advancing a fast pointer `n` steps ahead, then walking both until fast reaches the end.
- State the invariant: when `fast` becomes null, `slow.next` is the node to remove; a dummy head simplifies removing the first node.
- Handle removing the head, the tail, and a list whose length equals `n`.
- Time O(L), space O(1), and contrast with two passes (count length, walk `length - n`).

Common Follow-Ups:
- Delete the Middle Node of a Linked List (LC 2095) uses the slow/fast middle find.
- What if `n` is given as a fraction of the length.
- How does the answer change with a doubly linked list (walk from the tail directly).

## 3. Reorder List

LeetCode: [Reorder List](https://leetcode.com/problems/reorder-list/)

Difficulty: Medium

Pattern: Split, Reverse, Merge

Why It Matters: Combines three linked-list operations.

Skills Tested:
- Recognize that the desired interleave `L0 -> Ln -> L1 -> Ln-1 -> ...` decomposes into find-middle, reverse-second-half, and merge-alternate.
- State the invariant: after splitting at the middle, the first list's tail must be set to null before reversing the second half.
- Handle odd and even lengths consistently (slow/fast convention defines the split).
- Time O(n), space O(1), and contrast with a stack-based reorder which is O(n) extra.

Common Follow-Ups:
- Palindrome Linked List (LC 234) uses the same split-and-reverse skeleton.
- What if the reorder pattern is `L0, Ln, L1, Ln-1, L2` truncated at length `k`.
- Generalize to interleave by an arbitrary index permutation.

## 4. Copy List with Random Pointer

LeetCode: [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

Difficulty: Medium

Pattern: Hash Map Or Interweaving

Why It Matters: Forces node identity preservation.

Skills Tested:
- Recognize that random pointers mean a copied node's `random` must point to the matching copied node, so a mapping from original to copy is required.
- State the invariant (hash variant): `mapping[orig]` is the corresponding copy, built in a first pass and used to wire `next` and `random` in a second pass.
- Implement the O(1)-extra-space variant by interweaving copies into the original list, then unweaving.
- Time O(n), space O(n) for hash or O(1) for interweave, and explain the trade-off.

Common Follow-Ups:
- Clone Graph (LC 133) is the same node-identity problem on a graph.
- What if random can also point to nodes from another list.
- How would you serialize the list (encode each random as an index).

## 5. LRU Cache

LeetCode: [LRU Cache](https://leetcode.com/problems/lru-cache/)

Difficulty: Medium

Pattern: Hash Map Plus Doubly Linked List

Why It Matters: Real data-structure design with O(1) updates.

Skills Tested:
- Recognize that O(1) get and put with eviction requires a doubly linked list for ordering and a hash map for direct node access.
- State the invariant: most-recently-used at the head, least-recently-used at the tail, and the map always maps key to its node.
- Use sentinel head and tail nodes to remove edge cases at list boundaries.
- Time O(1) per operation, space O(capacity), and contrast with `OrderedDict` which already implements this.

Common Follow-Ups:
- LFU Cache (LC 460) extends to least-frequently-used eviction.
- Design a TTL cache where entries also expire by time.
- What if the cache is sharded across nodes for concurrent access.

## 6. Swap Nodes in Pairs

LeetCode: [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

Difficulty: Medium

Pattern: Local Pairwise Rewiring

Why It Matters: Practices careful pointer swaps.

Skills Tested:
- Recognize that swapping every two adjacent nodes is a small group reversal and a dummy head simplifies the head replacement.
- State the invariant: after each swap, the previous tail's `next` is wired to the new (swapped) head of the next pair.
- Handle odd-length lists (the last single node stays in place).
- Time O(n), space O(1) iterative or O(n) recursive.

Common Follow-Ups:
- Reverse Nodes in k-Group (LC 25) generalizes from pairs to k-sized groups.
- What if every k-th group must be reversed but others stay (alternate reversal).
- Implement recursively and compare to the iterative version.

## 7. Odd Even Linked List

LeetCode: [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

Difficulty: Medium

Pattern: Two-List Partition

Why It Matters: Separates nodes by position while preserving order.

Skills Tested:
- Recognize that two pointers `odd` and `even`, plus a save of `evenHead`, can partition nodes by index in one pass.
- State the invariant: at each step, `odd` and `even` always point to the last odd-indexed and even-indexed node placed so far.
- Connect `odd.next = evenHead` at the end to splice the two halves.
- Time O(n), space O(1), and contrast with a value-copy approach that is also O(n) but uses extra space.

Common Follow-Ups:
- Partition List (LC 86) splits by value rather than position.
- What if the partition criterion is parity of value, not position.
- Generalize to k disjoint position classes.

## 8. Design Browser History

LeetCode: [Design Browser History](https://leetcode.com/problems/design-browser-history/)

Difficulty: Medium

Pattern: Doubly Linked List Or Two Stacks

Why It Matters: Models navigation with mutable current pointer.

Skills Tested:
- Recognize that `visit` invalidates forward history, which is exactly two stacks (back and forward) or a doubly linked list with a current pointer.
- State the invariant: the back stack holds the visited prefix excluding current; the forward stack holds undone history.
- Implement `back(steps)` and `forward(steps)` as bounded shifts that respect stack lengths.
- Per-call time O(min(steps, history)), space O(history).

Common Follow-Ups:
- Build a tab manager with branching history per tab.
- What if visits also need to be stored persistently to disk.
- How would you compress long histories.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
