# 1-D Dynamic Programming Medium Problems

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

## 1. House Robber

LeetCode: [House Robber](https://leetcode.com/problems/house-robber/)

Difficulty: Medium

Pattern: Choose Or Skip DP

Why It Matters: Core non-adjacent choice recurrence.

Skills Tested:
- Identify the Choose Or Skip DP signal before choosing a template.
- State the invariant for House Robber: core non-adjacent choice recurrence.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push House Robber toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Choose Or Skip DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. House Robber II

LeetCode: [House Robber II](https://leetcode.com/problems/house-robber-ii/)

Difficulty: Medium

Pattern: Circular DP Split

Why It Matters: Handles circular adjacency by splitting cases.

Skills Tested:
- Identify the Circular DP Split signal before choosing a template.
- State the invariant for House Robber II: handles circular adjacency by splitting cases.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push House Robber II toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Circular DP Split invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Coin Change

LeetCode: [Coin Change](https://leetcode.com/problems/coin-change/)

Difficulty: Medium

Pattern: Min Coins DP

Why It Matters: Classic unbounded minimization DP.

Skills Tested:
- Identify the Min Coins DP signal before choosing a template.
- State the invariant for Coin Change: classic unbounded minimization DP.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Coin Change toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Min Coins DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Longest Increasing Subsequence

LeetCode: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

Difficulty: Medium

Pattern: Subsequence DP

Why It Matters: Core ordered subsequence optimization.

Skills Tested:
- Identify the Subsequence DP signal before choosing a template.
- State the invariant for Longest Increasing Subsequence: core ordered subsequence optimization.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Increasing Subsequence toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Subsequence DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Word Break

LeetCode: [Word Break](https://leetcode.com/problems/word-break/)

Difficulty: Medium

Pattern: Boolean DP

Why It Matters: Tests prefix feasibility and dictionary lookup.

Skills Tested:
- Identify the Boolean DP signal before choosing a template.
- State the invariant for Word Break: tests prefix feasibility and dictionary lookup.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Word Break toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Boolean DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Decode Ways

LeetCode: [Decode Ways](https://leetcode.com/problems/decode-ways/)

Difficulty: Medium

Pattern: String DP

Why It Matters: Requires careful zero handling.

Skills Tested:
- Identify the String DP signal before choosing a template.
- State the invariant for Decode Ways: requires careful zero handling.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Decode Ways toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the String DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Combination Sum IV

LeetCode: [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

Difficulty: Medium

Pattern: Counting Ordered Combinations

Why It Matters: Highlights order-sensitive count DP.

Skills Tested:
- Identify the Counting Ordered Combinations signal before choosing a template.
- State the invariant for Combination Sum IV: highlights order-sensitive count DP.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Combination Sum IV toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Counting Ordered Combinations invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Partition Equal Subset Sum

LeetCode: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

Difficulty: Medium

Pattern: 0/1 Knapsack

Why It Matters: Classic target-capacity DP.

Skills Tested:
- Identify the 0/1 Knapsack signal before choosing a template.
- State the invariant for Partition Equal Subset Sum: classic target-capacity DP.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Partition Equal Subset Sum toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the 0/1 Knapsack invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
