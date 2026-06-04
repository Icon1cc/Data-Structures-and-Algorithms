# Backtracking Easy Problems

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

## 1. Binary Tree Paths

LeetCode: [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

Difficulty: Easy

Pattern: Path Backtracking

Why It Matters: Introduces path push/pop and copying at leaves.

Skills Tested:
- Identify the Path Backtracking signal before choosing a template.
- State the invariant for Binary Tree Paths: introduces path push/pop and copying at leaves.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Binary Tree Paths toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Path Backtracking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Path Sum

LeetCode: [Path Sum](https://leetcode.com/problems/path-sum/)

Difficulty: Easy

Pattern: Recursive Path State

Why It Matters: Practices carrying remaining target down a tree.

Skills Tested:
- Identify the Recursive Path State signal before choosing a template.
- State the invariant for Path Sum: practices carrying remaining target down a tree.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Path Sum toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Recursive Path State invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Sum of All Subset XOR Totals

LeetCode: [Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)

Difficulty: Easy

Pattern: Subset Enumeration

Why It Matters: Small enumeration problem with subset choices.

Skills Tested:
- Identify the Subset Enumeration signal before choosing a template.
- State the invariant for Sum of All Subset XOR Totals: small enumeration problem with subset choices.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sum of All Subset XOR Totals toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Subset Enumeration invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
