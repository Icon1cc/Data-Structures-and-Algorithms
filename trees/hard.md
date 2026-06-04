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

Pattern: Tree DP

Why It Matters: Hard local/global path reasoning.

Skills Tested:
- Identify the Tree DP signal before choosing a template.
- State the invariant for Binary Tree Maximum Path Sum: hard local/global path reasoning.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Binary Tree Maximum Path Sum toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Tree DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Serialize and Deserialize Binary Tree

LeetCode: [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

Difficulty: Hard

Pattern: Traversal Encoding

Why It Matters: Tests lossless tree representation.

Skills Tested:
- Identify the Traversal Encoding signal before choosing a template.
- State the invariant for Serialize and Deserialize Binary Tree: tests lossless tree representation.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Serialize and Deserialize Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Traversal Encoding invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Recover Binary Search Tree

LeetCode: [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

Difficulty: Hard

Pattern: Inorder Anomaly Detection

Why It Matters: Uses sorted inorder violations.

Skills Tested:
- Identify the Inorder Anomaly Detection signal before choosing a template.
- State the invariant for Recover Binary Search Tree: uses sorted inorder violations.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Recover Binary Search Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Inorder Anomaly Detection invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Vertical Order Traversal of a Binary Tree

LeetCode: [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

Difficulty: Hard

Pattern: Coordinate Traversal

Why It Matters: Combines BFS/DFS with ordered coordinates.

Skills Tested:
- Identify the Coordinate Traversal signal before choosing a template.
- State the invariant for Vertical Order Traversal of a Binary Tree: combines BFS/DFS with ordered coordinates.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Vertical Order Traversal of a Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Coordinate Traversal invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
