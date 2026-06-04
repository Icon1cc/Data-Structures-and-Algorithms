# 2-D Dynamic Programming Hard Problems

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

## 1. Edit Distance

LeetCode: [Edit Distance](https://leetcode.com/problems/edit-distance/)

Difficulty: Hard

Pattern: Two String DP

Why It Matters: Classic insert/delete/replace recurrence.

Skills Tested:
- Identify the Two String DP signal before choosing a template.
- State the invariant for Edit Distance: classic insert/delete/replace recurrence.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Edit Distance toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Two String DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Regular Expression Matching

LeetCode: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

Difficulty: Hard

Pattern: Two String DP With Operators

Why It Matters: Hard pattern matching state transitions.

Skills Tested:
- Identify the Two String DP With Operators signal before choosing a template.
- State the invariant for Regular Expression Matching: hard pattern matching state transitions.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Regular Expression Matching toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Two String DP With Operators invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Burst Balloons

LeetCode: [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

Difficulty: Hard

Pattern: Interval DP

Why It Matters: Canonical split-point interval DP.

Skills Tested:
- Identify the Interval DP signal before choosing a template.
- State the invariant for Burst Balloons: canonical split-point interval DP.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Burst Balloons toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Interval DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Distinct Subsequences

LeetCode: [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

Difficulty: Hard

Pattern: Two String Counting DP

Why It Matters: Counts ways to form a target subsequence.

Skills Tested:
- Identify the Two String Counting DP signal before choosing a template.
- State the invariant for Distinct Subsequences: counts ways to form a target subsequence.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Distinct Subsequences toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Two String Counting DP invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
