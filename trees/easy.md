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
- Identify the Recursive DFS signal before choosing a template.
- State the invariant for Maximum Depth of Binary Tree: the simplest recursive return contract.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Maximum Depth of Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Recursive DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Same Tree

LeetCode: [Same Tree](https://leetcode.com/problems/same-tree/)

Difficulty: Easy

Pattern: Recursive DFS

Why It Matters: Tests paired traversal and structural equality.

Skills Tested:
- Identify the Recursive DFS signal before choosing a template.
- State the invariant for Same Tree: tests paired traversal and structural equality.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Same Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Recursive DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Invert Binary Tree

LeetCode: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

Difficulty: Easy

Pattern: Recursive DFS

Why It Matters: Practices local subtree mutation.

Skills Tested:
- Identify the Recursive DFS signal before choosing a template.
- State the invariant for Invert Binary Tree: practices local subtree mutation.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Invert Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Recursive DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Balanced Binary Tree

LeetCode: [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

Difficulty: Easy

Pattern: Postorder DFS

Why It Matters: Combines height and validity.

Skills Tested:
- Identify the Postorder DFS signal before choosing a template.
- State the invariant for Balanced Binary Tree: combines height and validity.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Balanced Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Postorder DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Diameter of Binary Tree

LeetCode: [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Difficulty: Easy

Pattern: Tree DP

Why It Matters: Introduces global answer plus local height.

Skills Tested:
- Identify the Tree DP signal before choosing a template.
- State the invariant for Diameter of Binary Tree: introduces global answer plus local height.
- Handle null roots, skewed depth, duplicate BST values, and global-state reset.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Diameter of Binary Tree toward iterative stack, BFS queue, parent maps, or graph traversal?
- Which null roots case would break the first implementation?
- Can the Tree DP invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
