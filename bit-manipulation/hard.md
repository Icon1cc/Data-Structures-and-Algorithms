# Bit Manipulation Hard Problems

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

## 1. Minimum Number of K Consecutive Bit Flips

LeetCode: [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)

Difficulty: Hard

Pattern: Difference Array Of Active Flips

Why It Matters: Tracks active flips efficiently.

Skills Tested:
- Recognize that flipping a length-K window is greedy: scan left to right, flip whenever `nums[i] xor active_flips == 0`.
- State the invariant: `active_flips` is the parity of flips currently affecting position `i`; a difference array signals when each flip's effect ends.
- Handle the failure case where a needed flip extends past the array (return `-1`).
- Time O(n), space O(n).

Common Follow-Ups:
- Generalize to flips of different sizes per position.
- What if values are not binary.
- Stream the input and answer feasibility online.

## 2. Maximum XOR With an Element From Array

LeetCode: [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

Difficulty: Hard

Pattern: Offline Bit Trie With Size Constraint

Why It Matters: Adds offline constraints to bit-trie search.

Skills Tested:
- Recognize that "max XOR of `query` with any `nums[i] <= m_i`" is solved offline: sort numbers and queries, insert numbers into a bit trie up to each query's bound, then perform the standard greedy bit-trie XOR query.
- State the invariant: the trie always contains exactly the numbers `<= m_i`; queries process in sorted-`m` order so insertions are append-only.
- Handle empty trie at query time (return `-1`).
- Time O((n + q) * 31), space O(n * 31).

Common Follow-Ups:
- Maximum XOR of Two Numbers in Array (LC 421) is the no-constraint version.
- Stream queries online with a persistent trie.
- Generalize to k-th largest XOR.

## 3. Count Pairs With XOR in a Range

LeetCode: [Count Pairs With XOR in a Range](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/)

Difficulty: Hard

Pattern: Bit Trie Counting With Range

Why It Matters: Counts pairs by bounded XOR.

Skills Tested:
- Recognize that "count pairs with XOR `< K`" is the building block; the answer to `[low, high]` is `f(high + 1) - f(low)`.
- State the invariant: a bit trie stores past numbers with subtree counts; for each `nums[i]`, descend bit-by-bit deciding subtrees using the bits of `K - 1`.
- Carefully handle equality cases at each bit.
- Time O(n * 16), space O(n * 16) for trie nodes.

Common Follow-Ups:
- Maximum XOR of Two Numbers in Array (LC 421) is the maximum-only sibling.
- Pairs with XOR in a range with size constraints.
- Stream values and answer online.

## 4. Smallest Sufficient Team

LeetCode: [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)

Difficulty: Hard

Pattern: Bitmask DP On Skills

Why It Matters: Uses skills as a set mask.

Skills Tested:
- Recognize that skills can be encoded as a bitmask (up to 16 skills); `dp[mask]` is the smallest team covering exactly the skills in `mask`.
- State the invariant: for each person with skill set `pSkills`, transition `dp[mask | pSkills] = min(dp[mask | pSkills], dp[mask] + [person])`.
- Reconstruct the actual team by storing the predecessor mask and chosen person at each state.
- Time O(2^skills * people), space O(2^skills).

Common Follow-Ups:
- Travelling Salesperson DP (LC 943) uses the same bitmask state.
- What if skills have weights (weighted set cover).
- Generalize to multi-set coverage with overlap costs.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
