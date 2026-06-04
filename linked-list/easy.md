# Linked List Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Reverse Linked List

LeetCode: [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Difficulty: Easy

Pattern: In-place Reversal

Why It Matters: Baseline pointer reversal.

Skills Tested:
- Recognize that reversing requires three pointers `prev`, `curr`, `next` to flip each link without losing the next node.
- State the invariant: every node already visited has its `next` pointing back, and `prev` is always the new head of the reversed prefix.
- Handle empty lists (return null), single-node lists (return as is), and two-node lists.
- Time O(n), space O(1) iterative or O(n) recursive due to the call stack.

Common Follow-Ups:
- Reverse Linked List II (LC 92) reverses only between positions `m` and `n`.
- Reverse Nodes in k-Group (LC 25) generalizes to chunked reversal.
- Implement the same algorithm recursively and analyze the call stack.

## 2. Merge Two Sorted Lists

LeetCode: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Difficulty: Easy

Pattern: Dummy Head Merge

Why It Matters: Tests sentinel use and sorted attachment.

Skills Tested:
- Recognize that splicing two sorted lists into one is greedy: at each step pick the smaller head.
- State the invariant: the dummy head's `next` always points to the merged sorted prefix; `tail` points to the last appended node.
- Use a sentinel `dummy` node to simplify head handling and avoid null checks at every step.
- Time O(n + m), space O(1) iterative (or O(n + m) recursive).

Common Follow-Ups:
- Merge K Sorted Lists (LC 23) wraps this routine in a heap or pairwise merge.
- Merge Sorted Array (LC 88) is the array version and writes from the back.
- What if the lists must be merged into a circular doubly linked list.

## 3. Linked List Cycle

LeetCode: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Difficulty: Easy

Pattern: Floyd Cycle Detection

Why It Matters: Classic cycle detection.

Skills Tested:
- Recognize that the only O(1)-extra-space method is Floyd's tortoise-and-hare, where two pointers move at different speeds.
- State the invariant: if a cycle exists, the fast pointer must eventually catch the slow pointer; if not, fast reaches null first.
- Handle the empty list, the single-node list with a self-loop, and a long acyclic list (return false promptly).
- Time O(n), space O(1), and contrast with the hash set approach which is O(n) extra space.

Common Follow-Ups:
- Linked List Cycle II (LC 142) returns the entry node of the cycle using a second-walk argument.
- Find the Duplicate Number (LC 287) reuses cycle detection over array indices.
- What changes if the list can have arbitrarily many components.

## 4. Palindrome Linked List

LeetCode: [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Difficulty: Easy

Pattern: Middle Find Plus Reverse Second Half

Why It Matters: Combines slow/fast split and reversal.

Skills Tested:
- Recognize that O(1)-extra-space palindrome check requires finding the middle, reversing the second half, and comparing both halves node by node.
- State the invariant: after the slow/fast walk, `slow` is at the start of the second half (or just past the middle for odd length).
- Restore the list (reverse the second half back) if the caller cares about preserving structure.
- Time O(n), space O(1), and contrast with copying values into an array which is O(n) space.

Common Follow-Ups:
- Reverse Linked List (LC 206) is the helper used here.
- What if the input is a doubly linked list (use both ends and converge).
- How would you do this with concurrent updates to the list.

## 5. Middle of the Linked List

LeetCode: [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Difficulty: Easy

Pattern: Fast And Slow Pointers

Why It Matters: Builds speed-based middle detection.

Skills Tested:
- Recognize that "the middle of an unknown-length list" is solved by advancing two pointers at speeds 1 and 2.
- State the invariant: when `fast` reaches the end, `slow` is at the middle (the second middle for even length per problem spec).
- Handle a single node (the middle is itself) and a two-node list (the second is the middle).
- Time O(n), space O(1), and contrast with two passes (count length, walk to `length // 2`).

Common Follow-Ups:
- Reorder List (LC 143) uses middle-find as its first step.
- Find Cycle Start (LC 142) reuses the same two-speed scheme with a second walk.
- What if you must return the first middle on even-length lists.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
