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

Pattern: Grid Path Count DP

Why It Matters: Baseline grid path count.

Skills Tested:
- Recognize that paths into `(i, j)` come only from `(i - 1, j)` or `(i, j - 1)`, so `dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`.
- State the invariant: `dp[i][j]` is the count of distinct paths from `(0, 0)` to `(i, j)`.
- Compress to a single row updated left-to-right since each cell only needs the row above and the cell on the left.
- Time O(M * N), space O(min(M, N)), and contrast with the closed form `C(M + N - 2, M - 1)` which is O(M + N).

Common Follow-Ups:
- Unique Paths II (LC 63) adds blocked cells.
- What if movement is allowed in 4 or 8 directions.
- Count paths with weighted moves.

## 2. Unique Paths II

LeetCode: [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

Difficulty: Medium

Pattern: Grid Path Count With Obstacles

Why It Matters: Adds blocked cells and base-case care.

Skills Tested:
- Recognize that `dp[i][j] = 0` whenever `obstacle[i][j] == 1`, otherwise the same recurrence as Unique Paths.
- State the invariant: blocked cells contribute zero paths to all downstream cells.
- Initialize the first row and first column carefully: a single obstacle blocks every cell beyond it.
- Time O(M * N), space O(N).

Common Follow-Ups:
- Minimum Path Sum (LC 64) replaces count with min cost.
- What if some obstacles are conditional (have probabilities).
- Generalize to k-step moves.

## 3. Minimum Path Sum

LeetCode: [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

Difficulty: Medium

Pattern: Grid Min Cost DP

Why It Matters: Uses top/left minimum recurrence.

Skills Tested:
- Recognize that the minimum cost to reach `(i, j)` is `grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])`.
- State the invariant: `dp[i][j]` is the minimum cost over all paths from `(0, 0)` to `(i, j)`.
- Initialize the first row and column as cumulative sums; in-place mutation of `grid` saves O(M * N) memory.
- Time O(M * N), space O(N) compressed or O(1) extra in place.

Common Follow-Ups:
- Triangle (LC 120) is the same idea on a triangular grid.
- What if some cells multiply rather than add to the cost.
- Generalize to k diagonal moves allowed.

## 4. Longest Common Subsequence

LeetCode: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

Difficulty: Medium

Pattern: Two-String Match-Or-Skip DP

Why It Matters: The most important two-string DP pattern.

Skills Tested:
- Recognize the recurrence: `dp[i][j] = dp[i - 1][j - 1] + 1` if `text1[i - 1] == text2[j - 1]`, else `max(dp[i - 1][j], dp[i][j - 1])`.
- State the invariant: `dp[i][j]` is the LCS length of the prefixes `text1[:i]` and `text2[:j]`.
- Compress to two rows; reconstruction of the LCS itself requires the full `M x N` table.
- Time O(M * N), space O(min(M, N)) compressed.

Common Follow-Ups:
- Edit Distance (LC 72) extends to insert/delete/replace operations.
- Shortest Common Supersequence (LC 1092) reconstructs from LCS.
- What if you must return one actual LCS string.

## 5. Coin Change II

LeetCode: [Coin Change II](https://leetcode.com/problems/coin-change-ii/)

Difficulty: Medium

Pattern: Unbounded Knapsack Counting

Why It Matters: Counts combinations with item/capacity dimensions.

Skills Tested:
- Recognize that ordered counts versus unordered counts differ in loop order: items outer ensures unordered combinations.
- State the invariant: `dp[a]` is the number of unordered ways to make amount `a` using the prefix of coins seen so far.
- Initialize `dp[0] = 1` (one way to make zero) and update `dp[a] += dp[a - coin]`.
- Time O(amount * len(coins)), space O(amount).

Common Follow-Ups:
- Coin Change (LC 322) minimizes coin count.
- Combination Sum IV (LC 377) counts ordered.
- Add a per-coin maximum-use cap (bounded knapsack).

## 6. Target Sum

LeetCode: [Target Sum](https://leetcode.com/problems/target-sum/)

Difficulty: Medium

Pattern: Knapsack Reformulation

Why It Matters: Converts signs into subset count.

Skills Tested:
- Recognize that splitting nums into positive set P and negative set N yields `sum(P) - sum(N) = target` and `sum(P) + sum(N) = total`, so `sum(P) = (total + target) / 2`.
- State the invariant: count subsets summing to that derived target via 0/1 subset-sum DP.
- Quick reject when `total + target` is odd or `abs(target) > total`.
- Time O(n * target), space O(target).

Common Follow-Ups:
- Partition Equal Subset Sum (LC 416) is the boolean variant.
- What if some elements have weights rather than counts.
- Use generating functions for symbolic counts.

## 7. Interleaving String

LeetCode: [Interleaving String](https://leetcode.com/problems/interleaving-string/)

Difficulty: Medium

Pattern: Two-String Pointer DP

Why It Matters: Uses two indices to match a third string.

Skills Tested:
- Recognize that `dp[i][j]` is true iff `s3[:i + j]` is an interleaving of `s1[:i]` and `s2[:j]`.
- State the invariant: `dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])`.
- Quick reject when `len(s1) + len(s2) != len(s3)`.
- Time O(M * N), space O(N).

Common Follow-Ups:
- Distinct Subsequences (LC 115) is a related two-string counting.
- Stream `s3` and answer feasibility online.
- Generalize to k strings.

## 8. Longest Palindromic Substring

LeetCode: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Difficulty: Medium

Pattern: Interval Truth DP Or Center Expansion

Why It Matters: Builds palindrome truth by length.

Skills Tested:
- Recognize that `dp[i][j]` is true iff `s[i..j]` is a palindrome, with the recurrence `s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])`.
- State the invariant: fill the table by increasing length so dependencies are already known.
- Center-expansion alternative: try every index (and every gap) as the center, extend outward while characters match.
- Time O(n^2), space O(n^2) DP or O(1) center expansion; Manacher's algorithm achieves O(n).

Common Follow-Ups:
- Palindromic Substrings (LC 647) counts all palindromic substrings.
- Longest Palindromic Subsequence (LC 516) uses a different two-pointer DP.
- What if multiple longest palindromes exist (return any).

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
