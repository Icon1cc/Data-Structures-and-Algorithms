# 2-D Dynamic Programming Medium Problems

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

## 1. Unique Paths

LeetCode: [Unique Paths](https://leetcode.com/problems/unique-paths/)

Difficulty: Medium

Pattern: Grid DP

Why It Matters: Baseline grid path count.

Skills Tested:
- Identify the Grid DP signal before choosing a template.
- State the invariant for Unique Paths: baseline grid path count.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Unique Paths toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Grid DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Unique Paths II

LeetCode: [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

Difficulty: Medium

Pattern: Grid DP With Obstacles

Why It Matters: Adds blocked cells and base-case care.

Skills Tested:
- Identify the Grid DP With Obstacles signal before choosing a template.
- State the invariant for Unique Paths II: adds blocked cells and base-case care.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Unique Paths II toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Grid DP With Obstacles invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Minimum Path Sum

LeetCode: [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

Difficulty: Medium

Pattern: Grid Min Cost DP

Why It Matters: Uses top/left minimum recurrence.

Skills Tested:
- Identify the Grid Min Cost DP signal before choosing a template.
- State the invariant for Minimum Path Sum: uses top/left minimum recurrence.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Path Sum toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Grid Min Cost DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Longest Common Subsequence

LeetCode: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

Difficulty: Medium

Pattern: Two String DP

Why It Matters: The most important two-string DP pattern.

Skills Tested:
- Identify the Two String DP signal before choosing a template.
- State the invariant for Longest Common Subsequence: the most important two-string DP pattern.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Common Subsequence toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Two String DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Coin Change II

LeetCode: [Coin Change II](https://leetcode.com/problems/coin-change-ii/)

Difficulty: Medium

Pattern: Knapsack Table

Why It Matters: Counts combinations with item/capacity dimensions.

Skills Tested:
- Identify the Knapsack Table signal before choosing a template.
- State the invariant for Coin Change II: counts combinations with item/capacity dimensions.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Coin Change II toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Knapsack Table invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Target Sum

LeetCode: [Target Sum](https://leetcode.com/problems/target-sum/)

Difficulty: Medium

Pattern: Knapsack Transform

Why It Matters: Converts signs into subset count.

Skills Tested:
- Identify the Knapsack Transform signal before choosing a template.
- State the invariant for Target Sum: converts signs into subset count.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Target Sum toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Knapsack Transform invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Interleaving String

LeetCode: [Interleaving String](https://leetcode.com/problems/interleaving-string/)

Difficulty: Medium

Pattern: Two String DP

Why It Matters: Uses two indices to match a third string.

Skills Tested:
- Identify the Two String DP signal before choosing a template.
- State the invariant for Interleaving String: uses two indices to match a third string.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Interleaving String toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Two String DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Longest Palindromic Substring

LeetCode: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Difficulty: Medium

Pattern: Interval-Like String DP

Why It Matters: Builds palindrome truth by length.

Skills Tested:
- Identify the Interval-Like String DP signal before choosing a template.
- State the invariant for Longest Palindromic Substring: builds palindrome truth by length.
- Handle empty dimensions, boundary initialization, diagonal fill order, and compressed-row overwrites.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Palindromic Substring toward 1-D DP, BFS on state graph, greedy, backtracking, or trie search?
- Which empty dimensions case would break the first implementation?
- Can the Interval-Like String DP invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
