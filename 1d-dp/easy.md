# 1-D Dynamic Programming Easy Problems

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

## 1. Climbing Stairs

LeetCode: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

Difficulty: Easy

Pattern: Linear Recurrence

Why It Matters: The baseline recurrence for ways to reach state i.

Skills Tested:
- Recognize that ways to reach step `i` equals ways to reach `i - 1` plus ways to reach `i - 2`, the Fibonacci recurrence.
- State the invariant: `dp[i]` is the count of distinct paths to reach step `i`; `dp[0] = dp[1] = 1`.
- Compress to two rolling variables for O(1) space.
- Time O(n), space O(1), and contrast with naive recursion which is exponential.

Common Follow-Ups:
- Min Cost Climbing Stairs (LC 746) layers a cost on each step.
- What if 1, 2, or `k` steps are allowed each move (Combination Sum IV with ordered counting).
- Closed-form via Binet's formula and matrix exponentiation.

## 2. Min Cost Climbing Stairs

LeetCode: [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

Difficulty: Easy

Pattern: Linear Min Cost DP

Why It Matters: Adds costs and minimum transition choice.

Skills Tested:
- Recognize that the cost to reach step `i` is `cost[i] + min(reach(i - 1), reach(i - 2))`, with both step 0 and step 1 as valid starts.
- State the invariant: `dp[i]` is the minimum cost to *stand on* step `i`; the answer is `min(dp[n - 1], dp[n - 2])` (one beyond the top is free).
- Compress to two rolling variables for O(1) space.
- Time O(n), space O(1), and explain the choice of "cost on arrival" versus "cost on departure" framing.

Common Follow-Ups:
- Climbing Stairs (LC 70) is the count-only version.
- What if some steps are forbidden.
- Generalize to a graph with arbitrary node costs.

## 3. Fibonacci Number

LeetCode: [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

Difficulty: Easy

Pattern: Memoization Or Tabulation

Why It Matters: Simple overlapping-subproblem example.

Skills Tested:
- Recognize that the recursive formula `F(n) = F(n - 1) + F(n - 2)` has overlapping subproblems, which DP eliminates.
- State the invariant: `dp[i]` is the i-th Fibonacci number; tabulate from `dp[0] = 0, dp[1] = 1`.
- Compress to two rolling variables for O(1) space.
- Time O(n), space O(1), and contrast with O(2^n) naive recursion and O(log n) matrix exponentiation.

Common Follow-Ups:
- N-th Tribonacci (LC 1137) extends the recurrence to three terms.
- Implement matrix-power Fibonacci for O(log n) time.
- What changes for very large `n` modulo a prime.

## 4. N-th Tribonacci Number

LeetCode: [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

Difficulty: Easy

Pattern: Rolling Three-State

Why It Matters: Practices recurrence with three previous states.

Skills Tested:
- Recognize that `T(n) = T(n - 1) + T(n - 2) + T(n - 3)` requires three rolling variables, not two.
- State the invariant: at every step, `(a, b, c)` represents `(T(i - 2), T(i - 1), T(i))`.
- Initialize `T(0) = 0, T(1) = 1, T(2) = 1` carefully, especially for small `n`.
- Time O(n), space O(1).

Common Follow-Ups:
- Generalize to k-bonacci with a window of `k` rolling variables.
- What if some indices are missing and must be inferred.
- How does the recurrence behave under modular arithmetic.

## 5. Pascal's Triangle

LeetCode: [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

Difficulty: Easy

Pattern: Row-Based Recurrence

Why It Matters: Builds each row from previous row state.

Skills Tested:
- Recognize that row `r` is built from row `r - 1` via `C(r, k) = C(r - 1, k - 1) + C(r - 1, k)` with `C(r, 0) = C(r, r) = 1`.
- State the invariant: at iteration `r`, the previous row holds the binomial coefficients for `r - 1`.
- Build each row left-to-right from the previous row to avoid in-place overwrites.
- Time O(numRows^2), space O(numRows^2) for the full triangle.

Common Follow-Ups:
- Pascal's Triangle II (LC 119) returns only the k-th row in O(k) space.
- Binomial coefficient computation modulo a large prime.
- What if entries must be computed offline with memoization.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
