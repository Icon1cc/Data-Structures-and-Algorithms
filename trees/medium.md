# Trees Medium Problems

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

## 1. Binary Tree Level Order Traversal

LeetCode: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Difficulty: Medium

Pattern: BFS Level Order

Why It Matters: Core breadth-first tree traversal.

Skills Tested:
- Recognize that level groupings need BFS where each loop iteration processes exactly one level using the current queue size.
- State the invariant: at the start of each outer iteration, the queue holds exactly the nodes at the next level.
- Use a snapshot of `len(queue)` at each level to bound the inner loop.
- Time O(n), space O(width) which can be up to n/2 in a balanced tree.

Common Follow-Ups:
- Binary Tree Zigzag Level Order Traversal (LC 103) flips the row direction.
- Binary Tree Right Side View (LC 199) emits one node per level.
- N-ary Tree Level Order Traversal (LC 429) generalizes to many children.

## 2. Validate Binary Search Tree

LeetCode: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

Difficulty: Medium

Pattern: BST Bounds Recursion

Why It Matters: Tests ancestor constraints, not only parent checks.

Skills Tested:
- Recognize that a BST node must be greater than every left ancestor's lower bound and less than every right ancestor's upper bound, not only its immediate parent.
- State the invariant: each call gets a tighter `(low, high)` open interval; the value must satisfy `low < node.val < high`.
- Use `-inf` and `+inf` as initial sentinels and tighten as you recurse.
- Time O(n), space O(h), and contrast with the inorder approach where a strictly increasing inorder sequence is also a valid check.

Common Follow-Ups:
- Recover Binary Search Tree (LC 99) finds the two swapped nodes via inorder.
- Insert into a BST (LC 701) and Delete Node in a BST (LC 450) reuse the bounds idea.
- What if duplicates are allowed (relax `<` to `<=` carefully).

## 3. Kth Smallest Element in a BST

LeetCode: [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Difficulty: Medium

Pattern: Iterative Inorder

Why It Matters: Uses BST sorted order.

Skills Tested:
- Recognize that BST inorder yields sorted order, so the k-th popped node is the answer.
- State the invariant: the iterative inorder maintains a stack of left-spine nodes; popping yields the next smallest.
- Stop after popping `k` nodes; do not finish the full traversal.
- Time O(h + k), space O(h), and contrast with full traversal which is O(n).

Common Follow-Ups:
- BST Iterator (LC 173) generalizes the iterative inorder into an iterator class.
- What if the tree is augmented with subtree counts (precompute, then descend).
- How does the answer change for the k-th largest (reverse inorder).

## 4. Lowest Common Ancestor of a Binary Tree

LeetCode: [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

Difficulty: Medium

Pattern: LCA Recursive DFS

Why It Matters: Classic ancestor return contract.

Skills Tested:
- Recognize the LCA recursion contract: each call returns `p` or `q` if found in its subtree, else null; if both children return non-null, the current node is the LCA.
- State the invariant: a non-null return propagates up until two non-null returns meet, which marks the LCA.
- Handle the case where one node is an ancestor of the other (the deeper return wins).
- Time O(n), space O(h), and contrast with parent pointers (build a map, then walk both up).

Common Follow-Ups:
- LCA of a BST (LC 235) uses BST ordering for O(log n).
- LCA III (LC 1650) where nodes have parent pointers.
- LCA IV (LC 1676) generalizes to k nodes.

## 5. Binary Tree Right Side View

LeetCode: [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

Difficulty: Medium

Pattern: BFS With Last-of-Level

Why It Matters: Extracts one node per level.

Skills Tested:
- Recognize that the right-side view is the rightmost node at each depth, which BFS exposes naturally as the last node of each level.
- State the invariant: at each level, after visiting all nodes left-to-right, the last visited is the rightmost.
- Equivalent reverse-DFS: visit right child first and append the node only when the depth equals the current result length.
- Time O(n), space O(width).

Common Follow-Ups:
- Binary Tree Left Side View - mirror the same algorithm.
- Boundary of a Binary Tree (LC 545) combines left view, leaves, and right view.
- What if some nodes are obscured by a virtual gridline (vertical view).

## 6. Construct Binary Tree from Preorder and Inorder Traversal

LeetCode: [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Difficulty: Medium

Pattern: Recursive Reconstruction

Why It Matters: Builds trees from traversal invariants.

Skills Tested:
- Recognize that preorder's first element is the root, and the inorder split around that root yields left and right subtrees.
- State the invariant: at each recursive call, a `(preorderStart, inorderStart, inorderEnd)` window selects the subtree to build.
- Use a hash map of inorder value to index for O(1) split lookups.
- Time O(n), space O(n), and contrast with the O(n^2) recurrence that scans inorder each call.

Common Follow-Ups:
- Construct Binary Tree from Inorder and Postorder Traversal (LC 106).
- Construct Binary Tree from Preorder and Postorder Traversal (LC 889).
- Generalize to N-ary trees with sibling counts.

## 7. Path Sum II

LeetCode: [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

Difficulty: Medium

Pattern: Path Backtracking

Why It Matters: Maintains root-to-leaf path state.

Skills Tested:
- Recognize that collecting all root-to-leaf paths summing to a target is DFS with explicit push and pop on the path stack.
- State the invariant: at every recursive call, the `path` list equals the current root-to-node path.
- Append a copy (`path[:]`) to the result on a leaf-with-target match (modifying the live list later would corrupt prior results).
- Time O(n * h) in the worst case (path copying), space O(h).

Common Follow-Ups:
- Path Sum III (LC 437) counts paths starting at any node using prefix sums on the call stack.
- Sum Root to Leaf Numbers (LC 129) accumulates a base-10 number along each path.
- What if you must return only the lexicographically smallest matching path.

## 8. House Robber III

LeetCode: [House Robber III](https://leetcode.com/problems/house-robber-iii/)

Difficulty: Medium

Pattern: Tree DP With Tuple Return

Why It Matters: Returns choose and skip states per node.

Skills Tested:
- Recognize that each node has two states: rob it (skip children) or skip it (best of children's choices).
- State the invariant: the recursive return is `(robThis, skipThis)` where `robThis = node.val + skip(left) + skip(right)` and `skipThis = max(rob(left), skip(left)) + max(rob(right), skip(right))`.
- Avoid memoization mistakes by using the tuple-return form rather than a value-keyed cache.
- Time O(n), space O(h).

Common Follow-Ups:
- House Robber (LC 198) is the linear array version.
- House Robber II (LC 213) is on a circular array.
- Generalize to weighted independent set on trees.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
