# 2-D Dynamic Programming Easy Problems

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

## 1. Pascal's Triangle II

LeetCode: [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

Difficulty: Easy

Pattern: Row DP

Why It Matters: Small row-based table construction.

Skills Tested:
- Identify the Row DP signal before choosing a template.
- State the invariant for Pascal's Triangle II: small row-based table construction.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Pascal's Triangle II toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Row DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Range Sum Query 2D - Immutable

LeetCode: [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

Difficulty: Easy

Pattern: 2-D Prefix Sum

Why It Matters: Introduces two-dimensional cumulative sums.

Skills Tested:
- Identify the 2-D Prefix Sum signal before choosing a template.
- State the invariant for Range Sum Query 2D - Immutable: introduces two-dimensional cumulative sums.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Range Sum Query 2D - Immutable toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the 2-D Prefix Sum invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
