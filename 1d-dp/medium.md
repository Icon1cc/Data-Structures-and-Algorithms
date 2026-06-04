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

Pattern: Choose Or Skip Linear DP

Why It Matters: Core non-adjacent choice recurrence.

Skills Tested:
- Recognize that the maximum non-adjacent sum at index `i` is `max(rob(i - 1), rob(i - 2) + nums[i])`.
- State the invariant: `dp[i]` is the best loot using houses `0..i`; the recurrence captures the rob-or-skip decision.
- Compress to two rolling variables for O(1) space.
- Time O(n), space O(1), and contrast with brute O(2^n) subset enumeration.

Common Follow-Ups:
- House Robber II (LC 213) handles a circular street.
- House Robber III (LC 337) is on a tree.
- What if the constraint is "no three consecutive" instead.

## 2. House Robber II

LeetCode: [House Robber II](https://leetcode.com/problems/house-robber-ii/)

Difficulty: Medium

Pattern: Linear DP On Two Cases

Why It Matters: Handles circular adjacency by splitting cases.

Skills Tested:
- Recognize that the circle constraint forbids picking both house 0 and the last house, so the answer is `max(rob(0..n-2), rob(1..n-1))`.
- State the invariant: each linear subproblem reuses House Robber's recurrence on a half-open range.
- Handle `n == 1` (return `nums[0]`) and `n == 2` (return `max(nums)`) before splitting.
- Time O(n), space O(1).

Common Follow-Ups:
- Delete and Earn (LC 740) maps values to count-weighted house-rob.
- What if the circle is bidirectional but with weights.
- Generalize to k forbidden adjacencies.

## 3. Coin Change

LeetCode: [Coin Change](https://leetcode.com/problems/coin-change/)

Difficulty: Medium

Pattern: Unbounded Min DP

Why It Matters: Classic unbounded minimization DP.

Skills Tested:
- Recognize that the minimum coins to make amount `a` is `1 + min(dp[a - c] for c in coins if c <= a)` with `dp[0] = 0`.
- State the invariant: `dp[a]` is the minimum coin count for amount `a`, or `inf` if not possible.
- Iterate amounts in ascending order so smaller subproblems are solved first.
- Time O(amount * coins.length), space O(amount), and contrast with greedy which fails on non-canonical coin sets.

Common Follow-Ups:
- Coin Change II (LC 518) counts ways instead of minimum coins.
- What if coins can be used at most `k` times (bounded knapsack).
- BFS over states gives the same answer with explicit unweighted shortest paths.

## 4. Longest Increasing Subsequence

LeetCode: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

Difficulty: Medium

Pattern: Subsequence DP Or Patience Sort

Why It Matters: Core ordered subsequence optimization.

Skills Tested:
- Recognize the O(n^2) DP `dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])` and the O(n log n) patience-sort variant with `tails[k]` tracking the smallest possible tail of an LIS of length `k + 1`.
- State the invariant (patience): `tails` is sorted; `bisect_left(tails, nums[i])` gives the position to update.
- Reconstruct the actual LIS by storing predecessor indices in the O(n^2) version.
- Time O(n log n) or O(n^2), space O(n).

Common Follow-Ups:
- Number of Longest Increasing Subsequence (LC 673) counts how many LIS exist.
- Russian Doll Envelopes (LC 354) maps LIS onto sorted 2-D pairs.
- What if non-strict increase is allowed (use `bisect_right`).

## 5. Word Break

LeetCode: [Word Break](https://leetcode.com/problems/word-break/)

Difficulty: Medium

Pattern: Boolean Prefix DP

Why It Matters: Tests prefix feasibility and dictionary lookup.

Skills Tested:
- Recognize that `s[0..i]` is breakable iff there exists `j` such that `s[0..j]` is breakable and `s[j..i]` is in the dictionary.
- State the invariant: `dp[i]` is true iff the first `i` characters break into dictionary words; `dp[0] = true` as the empty prefix.
- Use a hash set for O(1) word lookups; iterate `j` only up to the maximum word length to prune.
- Time O(n^2) or O(n * maxWordLen), space O(n + dictionary).

Common Follow-Ups:
- Word Break II (LC 140) returns all decompositions via backtracking with memoization.
- Concatenated Words (LC 472) extends to a vocabulary built from itself.
- Use a trie of words for the lookup step.

## 6. Decode Ways

LeetCode: [Decode Ways](https://leetcode.com/problems/decode-ways/)

Difficulty: Medium

Pattern: String DP With Two Step Transitions

Why It Matters: Requires careful zero handling.

Skills Tested:
- Recognize that decoding `s[0..i]` either takes one digit (if `s[i - 1] != '0'`) or two digits (if `s[i - 2..i]` is in `[10, 26]`).
- State the invariant: `dp[i]` is the number of ways to decode the first `i` characters; `dp[0] = 1` for the empty prefix.
- Treat `'0'` carefully: it can never start a valid one-digit decode and must be paired with `'1'` or `'2'`.
- Time O(n), space O(1) with rolling variables.

Common Follow-Ups:
- Decode Ways II (LC 639) introduces wildcards.
- What if the alphabet has more than 26 letters or supports multi-digit codes.
- Generalize to weighted decoding with priorities.

## 7. Combination Sum IV

LeetCode: [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

Difficulty: Medium

Pattern: Order-Sensitive Counting DP

Why It Matters: Highlights order-sensitive count DP.

Skills Tested:
- Recognize that ordered combinations require iterating amounts in the outer loop and candidates in the inner loop, the opposite of Coin Change II.
- State the invariant: `dp[a] = sum(dp[a - c] for c in nums if c <= a)`; `dp[0] = 1` as the empty sequence.
- Confirm whether the problem asks for ordered or unordered counts before choosing the loop order.
- Time O(target * len(nums)), space O(target).

Common Follow-Ups:
- Coin Change II (LC 518) is the unordered counting variant.
- Climbing Stairs (LC 70) is the special case `nums = [1, 2]`.
- Modular arithmetic when counts can be huge.

## 8. Partition Equal Subset Sum

LeetCode: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

Difficulty: Medium

Pattern: 0/1 Knapsack Boolean DP

Why It Matters: Classic target-capacity DP.

Skills Tested:
- Recognize that "can we split into two equal-sum subsets" reduces to "can we form `total // 2` from a subset", a 0/1 knapsack feasibility.
- State the invariant: `dp[s]` is true iff some subset sums to `s`; iterate items and update from high `s` down to low `s` to enforce 0/1 (no reuse).
- Quick reject when `total` is odd.
- Time O(n * total), space O(total).

Common Follow-Ups:
- Subset Sum count problems generalize the boolean to integers.
- Last Stone Weight II (LC 1049) is partition-into-two-with-min-difference.
- Target Sum (LC 494) reframes signs as a partition.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
