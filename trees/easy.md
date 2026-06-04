# Trees Easy Problems

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

## 1. Maximum Depth of Binary Tree

LeetCode: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Difficulty: Easy

Pattern: Recursive DFS

Why It Matters: The simplest recursive return contract.

Skills Tested:
- Recognize that depth follows the recurrence `depth(node) = 1 + max(depth(left), depth(right))` with `depth(null) = 0`.
- State the invariant: each call returns the height of the subtree rooted at `node`, and the global answer is the height of the root.
- Handle null roots (return 0), single-node trees (return 1), and skewed trees that approach `n`.
- Time O(n), space O(h) for the recursion stack, and contrast with BFS level counting which uses O(width) memory.

Common Follow-Ups:
- Minimum Depth of Binary Tree (LC 111) requires special-casing leaf detection.
- N-ary Tree Maximum Depth (LC 559) generalizes to many children.
- Implement iteratively with BFS or an explicit stack.

## 2. Same Tree

LeetCode: [Same Tree](https://leetcode.com/problems/same-tree/)

Difficulty: Easy

Pattern: Paired Recursive DFS

Why It Matters: Tests paired traversal and structural equality.

Skills Tested:
- Recognize that "same tree" means same shape and same values, which is a synchronized DFS over both trees.
- State the invariant: at each call, both arguments are aligned positions in their respective trees; mismatch in null-ness or value returns false.
- Handle both-null (return true), one-null (return false), and value mismatch (return false) before recursing.
- Time O(min(m, n)), space O(h), and explain why early exit on first mismatch is essential.

Common Follow-Ups:
- Symmetric Tree (LC 101) is paired DFS with mirrored arguments.
- Subtree of Another Tree (LC 572) layers same-tree onto every node of the bigger tree.
- What if equality is structural only (ignore values).

## 3. Invert Binary Tree

LeetCode: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

Difficulty: Easy

Pattern: Recursive DFS

Why It Matters: Practices local subtree mutation.

Skills Tested:
- Recognize that mirroring is a postorder operation: invert children first, then swap them.
- State the invariant: when a call returns, the subtree at `node` is fully mirrored.
- Handle null safely (return null) and write the swap with a temporary or tuple unpacking.
- Time O(n), space O(h), and the iterative BFS or stack form is equivalent.

Common Follow-Ups:
- Symmetric Tree (LC 101) checks if a tree equals its inverse.
- N-ary Tree Inversion reverses the children list at each node.
- Implement iteratively without recursion.

## 4. Balanced Binary Tree

LeetCode: [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

Difficulty: Easy

Pattern: Postorder With Early Exit

Why It Matters: Combines height and validity.

Skills Tested:
- Recognize that height differences must be checked at every node, so a single postorder pass returns the height or a sentinel for "imbalanced".
- State the invariant: a recursive call returns the subtree height if balanced, or `-1` if not; the parent short-circuits on `-1`.
- Avoid the O(n^2) anti-pattern of computing height inside a recursion that already computes height.
- Time O(n), space O(h), and explain why naive separate height computations cost more.

Common Follow-Ups:
- Maximum Depth of Binary Tree (LC 104) is the underlying primitive.
- Convert Sorted Array to Balanced BST (LC 108) constructs a balanced tree.
- What if balance threshold is `k` instead of 1.

## 5. Diameter of Binary Tree

LeetCode: [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Difficulty: Easy

Pattern: Tree DP With Global

Why It Matters: Introduces global answer plus local height.

Skills Tested:
- Recognize that the diameter is the maximum of `leftHeight + rightHeight` across all nodes, while the recursive return must still be the local height.
- State the invariant: the recursion returns the longest downward path from `node`, and a global `best` accumulates the longest through-node path.
- Initialize the global before recursion and read it after.
- Time O(n), space O(h), and contrast with O(n^2) where height is recomputed for every candidate root.

Common Follow-Ups:
- Binary Tree Maximum Path Sum (LC 124) replaces edges with values and forbids negative contributions.
- Longest Univalue Path (LC 687) restricts the path to equal-valued edges.
- What if path length is measured in nodes instead of edges (off-by-one).

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
