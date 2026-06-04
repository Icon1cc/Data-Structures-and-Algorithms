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

Pattern: Two-String Edit DP

Why It Matters: Classic insert/delete/replace recurrence.

Skills Tested:
- Recognize the three-way transition: `dp[i][j] = dp[i - 1][j - 1]` if characters match, else `1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])`.
- State the invariant: `dp[i][j]` is the minimum operations to transform `word1[:i]` into `word2[:j]`.
- Initialize `dp[i][0] = i` and `dp[0][j] = j` (delete or insert all).
- Time O(M * N), space O(min(M, N)) compressed.

Common Follow-Ups:
- One Edit Distance (LC 161) is the boolean special case.
- Damerau-Levenshtein adds adjacent-transpose.
- Reconstruct the actual edit script.

## 2. Regular Expression Matching

LeetCode: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

Difficulty: Hard

Pattern: Pattern DP With Star

Why It Matters: Hard pattern matching state transitions.

Skills Tested:
- Recognize that `*` can mean "zero of preceding" (skip two pattern chars) or "extend current" (advance string by one if it matches the preceding pattern char).
- State the invariant: `dp[i][j]` is true iff `s[:i]` matches `p[:j]`.
- Initialize the first row to handle prefix-of-pattern matches like `a*b*c*`.
- Time O(M * N), space O(M * N).

Common Follow-Ups:
- Wildcard Matching (LC 44) replaces `.*` semantics with `?` and `*` of any-char.
- Build a generic DP over a small regex grammar.
- Stream the input and answer online.

## 3. Burst Balloons

LeetCode: [Burst Balloons](https://leetcode.com/problems/burst-balloons/)

Difficulty: Hard

Pattern: Interval DP On Last-Burst

Why It Matters: Canonical split-point interval DP.

Skills Tested:
- Recognize that picking which balloon bursts *last* in `(left, right)` decouples the two subintervals (because that balloon's neighbors are exactly `left` and `right`).
- State the invariant: `dp[l][r]` is the maximum coins from the open interval `(l, r)`; iterate over the last-burst index `k` in between.
- Pad the array with virtual `1`s on both ends.
- Time O(n^3), space O(n^2).

Common Follow-Ups:
- Minimum Cost to Merge Stones (LC 1000) is a related interval DP.
- Optimal Binary Search Tree uses the same last-pick decomposition.
- Stream balloons and add new ones (no longer interval DP).

## 4. Distinct Subsequences

LeetCode: [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

Difficulty: Hard

Pattern: Two-String Counting DP

Why It Matters: Counts ways to form a target subsequence.

Skills Tested:
- Recognize the recurrence: `dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]` if `s[i - 1] == t[j - 1]`, else `dp[i - 1][j]`.
- State the invariant: `dp[i][j]` counts distinct ways `s[:i]` produces `t[:j]` as a subsequence.
- Initialize `dp[i][0] = 1` (the empty target is always findable).
- Time O(M * N), space O(N) compressed.

Common Follow-Ups:
- Longest Common Subsequence (LC 1143) shares the prefix-DP pattern.
- What if the count is bounded modulo a prime.
- Reconstruct one actual matching sequence.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
