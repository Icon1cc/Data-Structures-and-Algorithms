# 1-D Dynamic Programming Hard Problems

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

## 1. Word Break II

LeetCode: [Word Break II](https://leetcode.com/problems/word-break-ii/)

Difficulty: Hard

Pattern: DP Plus Backtracking With Memoization

Why It Matters: Combines DP feasibility with output generation.

Skills Tested:
- Recognize that returning every decomposition is exponential in the worst case, but memoizing on suffix lets repeated suffix decompositions reuse cached lists.
- State the invariant: `solve(i)` returns the list of all decompositions of `s[i:]`; cache it.
- Prune with a feasibility pass (LC 139) before enumeration to skip unreachable suffixes.
- Time O(2^n) worst case, space O(unique suffixes * average decomposition count).

Common Follow-Ups:
- Word Break (LC 139) is the feasibility prerequisite.
- Concatenated Words (LC 472) reuses the same skeleton with a self-built dictionary.
- Stream output without buffering all decompositions.

## 2. Longest Valid Parentheses

LeetCode: [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

Difficulty: Hard

Pattern: DP Or Stack Of Indices

Why It Matters: String DP with tricky base cases.

Skills Tested:
- Recognize the DP recurrence: `dp[i]` is the length of the longest valid string ending at `i`; `s[i] == ')'` triggers a case split on `s[i - 1]`.
- State the invariant (stack): the stack holds indices of unmatched characters; the longest valid is bounded by the distance between the current index and the top of the stack after a pop.
- Both approaches handle the empty-prefix case via a sentinel index `-1` (stack) or `dp[0] = 0` (DP).
- Time O(n), space O(n) for either approach.

Common Follow-Ups:
- Generate Parentheses (LC 22) is the constructive cousin.
- Maximum Length of Pair Chain (LC 646) reuses interval-end DP.
- Two-pass O(1) space variant by left-to-right plus right-to-left counting.

## 3. Best Time to Buy and Sell Stock IV

LeetCode: [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

Difficulty: Hard

Pattern: State Machine DP With K Transactions

Why It Matters: Optimizes over transaction count.

Skills Tested:
- Recognize that the state is `(day, transactions used, holding stock)`, so the DP is `dp[i][k][0/1]` over up to `k` transactions.
- State the invariant: `dp[i][k][1]` is the best profit with stock at end of day `i` having opened up to `k` transactions; transitions are `hold` or `buy/sell`.
- Compress space to `O(k)` by iterating days as the outer loop.
- Time O(n * k), space O(k); when `k >= n / 2`, the problem reduces to unlimited transactions (LC 122).

Common Follow-Ups:
- Best Time to Buy and Sell Stock with Cooldown (LC 309) and With Fee (LC 714).
- What if transactions have non-uniform fees.
- Generalize to multiple stocks.

## 4. Frog Jump

LeetCode: [Frog Jump](https://leetcode.com/problems/frog-jump/)

Difficulty: Hard

Pattern: Memoized State Search

Why It Matters: Uses position and jump size as state.

Skills Tested:
- Recognize that the state `(stoneIndex, lastJump)` determines future moves; with `jump - 1`, `jump`, `jump + 1` as options.
- State the invariant: `reachable[stone]` is the set of jump sizes used to land there; the last stone is reachable iff its set is non-empty.
- Skip negative jumps and zero jumps.
- Time O(n^2), space O(n^2).

Common Follow-Ups:
- Jump Game (LC 55) is reachability with no jump-size constraint.
- Jump Game II (LC 45) minimizes jump count.
- What if stones move dynamically.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
