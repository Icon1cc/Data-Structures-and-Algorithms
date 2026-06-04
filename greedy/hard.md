# Greedy Hard Problems

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

## 1. Candy

LeetCode: [Candy](https://leetcode.com/problems/candy/)

Difficulty: Hard

Pattern: Two-Pass Local Constraints

Why It Matters: Satisfies local neighbor constraints both directions.

Skills Tested:
- Recognize that "every higher-rated neighbor must get more candy" decomposes into a left-to-right pass enforcing left neighbor, then a right-to-left pass enforcing right neighbor.
- State the invariant: after both passes, `candy[i] = max(leftPass[i], rightPass[i])`, satisfying both local constraints.
- One-pass O(1)-space variant exists by tracking up/down runs; explain the trade-off.
- Time O(n), space O(n) for the two-pass version.

Common Follow-Ups:
- What if equal ratings can take equal candy.
- Generalize to bidirectional constraints with magnitudes.
- Streaming variant where new ratings arrive at the right end.

## 2. Maximum Performance of a Team

LeetCode: [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

Difficulty: Hard

Pattern: Sort By Bottleneck Plus Heap Of Top Speeds

Why It Matters: Combines a sorted bottleneck metric with a heap of best supporting candidates.

Skills Tested:
- Recognize that sorting engineers by efficiency descending fixes the bottleneck; for each candidate efficiency, the best team uses the top-k speeds among engineers whose efficiency is at least the bottleneck.
- State the invariant: a min-heap of speeds with size at most `k`; for each engineer, push speed, evict if size exceeds `k`, compute candidate score.
- Track running speed sum; total mod 1e9 + 7.
- Time O(n log n), space O(k).

Common Follow-Ups:
- IPO (LC 502) is a related sort-plus-heap greedy.
- What if speeds and efficiencies trade off non-linearly.
- Generalize to multi-attribute team selection.

## 3. Minimum Number of Refueling Stops

LeetCode: [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

Difficulty: Hard

Pattern: Lazy Best-First Refuel

Why It Matters: Chooses best previous station only when needed.

Skills Tested:
- Recognize that you only need to refuel when the tank cannot reach the next station; the optimal refuel is the largest tank among stations already passed.
- State the invariant: a max-heap of fuel amounts at stations passed; whenever the running tank is insufficient for the next station, pop the heap and add the fuel.
- Track current position and fuel; loop over stations and the destination.
- Time O(n log n), space O(n).

Common Follow-Ups:
- Cheapest Gas Stations under capacity constraints.
- What if refuels have time cost.
- Generalize to multi-vehicle refueling.

## 4. Create Maximum Number

LeetCode: [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/)

Difficulty: Hard

Pattern: Best Subsequence Plus Merge

Why It Matters: Builds best subsequences and merges them.

Skills Tested:
- Recognize that the max number is built by choosing `i` digits from `nums1` and `k - i` from `nums2` (each as the lexicographically largest subsequence of that length), then merging by lexicographic comparison.
- State the invariant: the largest subsequence of length `L` from a single array is found by a monotonic-decreasing stack with a "remaining can pop" budget.
- The merge picks the array whose remaining suffix is lexicographically larger, breaking ties by lookahead.
- Time O(k * (m + n + k)), space O(m + n).

Common Follow-Ups:
- Largest Number (LC 179) is the smaller pure-string variant.
- What if values can be combined (sum or product).
- Generalize to merging more than two sequences.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
