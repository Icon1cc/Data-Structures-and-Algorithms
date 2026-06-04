# Trees Hard Problems

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

## 1. Binary Tree Maximum Path Sum

LeetCode: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

Difficulty: Hard

Pattern: Tree DP With Global

Why It Matters: Hard local/global path reasoning.

Skills Tested:
- Recognize that the recursion must return the best downward gain `node.val + max(0, leftGain, rightGain)` while a global tracks the best through-node path `node.val + max(0, leftGain) + max(0, rightGain)`.
- State the invariant: negative gains are clamped to zero, since any subtree contributes at most `max(0, gain)` to a parent.
- Initialize the global to `-inf` to handle all-negative trees correctly.
- Time O(n), space O(h), and contrast with O(n^2) where each node tries to root the path.

Common Follow-Ups:
- Diameter of Binary Tree (LC 543) is the unweighted version.
- Longest Univalue Path (LC 687) restricts to equal values.
- What if there is a budget on the number of edges in the path.

## 2. Serialize and Deserialize Binary Tree

LeetCode: [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

Difficulty: Hard

Pattern: Traversal Encoding

Why It Matters: Tests lossless tree representation.

Skills Tested:
- Recognize that a single traversal (preorder with null markers, or BFS with `#` sentinels) is enough to reconstruct any binary tree losslessly.
- State the invariant: the encoder emits null markers at every missing child, and the decoder consumes the same stream in the same order.
- Handle empty trees (encode as a single null marker) and trees with values that contain the chosen delimiter.
- Time O(n), space O(n), and contrast with two-traversal encodings (preorder + inorder) which require unique values.

Common Follow-Ups:
- Serialize and Deserialize BST (LC 449) can use a more compact encoding.
- Serialize and Deserialize N-ary Tree (LC 428) needs sibling counts or end markers.
- Design a streaming serializer that emits as it walks.

## 3. Recover Binary Search Tree

LeetCode: [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

Difficulty: Hard

Pattern: Inorder Anomaly Detection

Why It Matters: Uses sorted inorder violations.

Skills Tested:
- Recognize that in a valid BST, inorder yields a strictly increasing sequence; with two swapped nodes, exactly two adjacent-in-time pairs violate `prev.val < node.val`.
- State the invariant: the first violation's `prev` is one of the swapped nodes; the second violation's `node` is the other (or, if only one violation, both are at that pair).
- Implement Morris inorder for O(1) extra space (otherwise the recursion stack is O(h)).
- Time O(n), space O(1) Morris or O(h) recursive.

Common Follow-Ups:
- Validate Binary Search Tree (LC 98) is the closely related validation problem.
- What if `k` swaps must be undone (k > 2 makes it harder).
- Morris traversal in detail: how does the temporary thread maintain correctness.

## 4. Vertical Order Traversal of a Binary Tree

LeetCode: [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

Difficulty: Hard

Pattern: Coordinate Bucketing

Why It Matters: Combines BFS/DFS with ordered coordinates.

Skills Tested:
- Recognize that "vertical order" assigns each node coordinates `(col, row)` and the output groups by `col` ascending, then by `row`, then by value.
- State the invariant: each DFS step assigns `col -> col +/- 1` and `row -> row + 1`, accumulating into a dict keyed by column.
- Sort each column's entries by `(row, value)` before joining.
- Time O(n log n), space O(n), and contrast with naive BFS that fails to break ties by value at the same coordinate.

Common Follow-Ups:
- Binary Tree Vertical Order Traversal (LC 314) is the simpler tie-broken-by-insertion-order variant.
- Boundary of a Binary Tree (LC 545) needs left + leaves + right with no duplicates.
- How would you stream output without sorting (priority queue per column).

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
