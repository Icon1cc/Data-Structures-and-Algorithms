# Greedy Medium Problems

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

## 1. Jump Game

LeetCode: [Jump Game](https://leetcode.com/problems/jump-game/)

Difficulty: Medium

Pattern: Farthest Reach Greedy

Why It Matters: Core reachability greedy.

Skills Tested:
- Recognize that the farthest reachable index from any prefix is `max(i + nums[i])`; if that ever falls behind `i`, no jump can cross.
- State the invariant: at every index `i`, `farthest >= i` means `i` is reachable.
- Loop until `i > farthest` (failure) or `farthest >= n - 1` (success).
- Time O(n), space O(1), and contrast with O(n^2) DP that tracks reachability per cell.

Common Follow-Ups:
- Jump Game II (LC 45) returns the minimum number of jumps.
- Jump Game III (LC 1306) uses BFS over reachable indices.
- What if jumps can be made backward as well as forward.

## 2. Jump Game II

LeetCode: [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

Difficulty: Medium

Pattern: Range Frontier Greedy

Why It Matters: Finds minimum jumps by current frontier.

Skills Tested:
- Recognize that BFS in disguise: each "level" of jumps covers indices in `[currentEnd, farthest]`; bumping `jumps` happens when `i` reaches `currentEnd`.
- State the invariant: at every step, `farthest = max(farthest, i + nums[i])`; when `i == currentEnd`, advance `currentEnd = farthest` and increment `jumps`.
- Stop early when `currentEnd >= n - 1`.
- Time O(n), space O(1), and contrast with DP O(n^2).

Common Follow-Ups:
- Jump Game (LC 55) is the boolean reachability variant.
- What if some indices double the jump distance.
- Generalize to weighted moves (Dijkstra).

## 3. Gas Station

LeetCode: [Gas Station](https://leetcode.com/problems/gas-station/)

Difficulty: Medium

Pattern: Total Sum Plus Reset On Deficit

Why It Matters: Uses deficit reasoning to choose a start.

Skills Tested:
- Recognize that a circular tour exists iff `sum(gas) >= sum(cost)`; if it does, the start is the index right after the last point where the running tank dropped below zero.
- State the invariant: scanning from any start, if the tank goes negative at index `i`, no start in `[start, i]` works; reset `start = i + 1` and `tank = 0`.
- Track `total` separately to verify the existence condition.
- Time O(n), space O(1), and contrast with O(n^2) brute force over every start.

Common Follow-Ups:
- What if the tour can be in either direction.
- Generalize to multiple stops with capacity refilling.
- Online variant where stations are added incrementally.

## 4. Partition Labels

LeetCode: [Partition Labels](https://leetcode.com/problems/partition-labels/)

Difficulty: Medium

Pattern: Last Occurrence Greedy

Why It Matters: Cuts segments when all active characters close.

Skills Tested:
- Recognize that a label can close a partition only when every character within has its last occurrence inside the partition.
- State the invariant: precompute `lastIndex[c]` for every character; while scanning, extend the partition's right boundary to `max(end, lastIndex[s[i]])`.
- Cut when `i == end`; record the partition length.
- Time O(n), space O(alphabet).

Common Follow-Ups:
- Generalize to k-color partitioning where each color must be contiguous.
- What if partitions must have minimum length.
- Stream the input and yield partitions online.

## 5. Queue Reconstruction by Height

LeetCode: [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

Difficulty: Medium

Pattern: Sort By Height Then Insert By K

Why It Matters: Tests whether a sorted processing order can make a global placement constraint local.

Skills Tested:
- Recognize that taller people are unaffected by shorter ones in the front, so processing tallest-first turns a global constraint (`k` taller-or-equal in front) into a local insert at index `k`.
- State the invariant: at the time of inserting `(h, k)`, every person already in the result is taller-or-equal-than `h`, so `k` is exactly the desired insertion position.
- Tie-break tallest-first by smaller `k` first to avoid violations.
- Time O(n^2) using `list.insert`, space O(n).

Common Follow-Ups:
- Reconstruct under different constraints (e.g., k shorter in front).
- Use a Fenwick tree for O(n log n) insertion if `n` is large.
- What if `k` allows ties to count differently.

## 6. Hand of Straights

LeetCode: [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

Difficulty: Medium

Pattern: Counter Plus Smallest-First Greedy

Why It Matters: Builds consecutive groups from smallest available card.

Skills Tested:
- Recognize that the smallest available card must start a group of `groupSize` consecutive cards; if any consecutive number is missing in count, the answer is false.
- State the invariant: a sorted-key counter; pop the smallest, decrement counts of `[smallest, smallest + groupSize)`, repeat.
- Use `OrderedDict` or sorted unique keys to avoid scanning.
- Time O(n log n), space O(n).

Common Follow-Ups:
- Divide Array in Sets of K Consecutive Numbers (LC 1296) is the same problem.
- What if the group size must equal a divisor of `len(hand)`.
- Generalize to multi-set-with-replacement greedy.

## 7. Boats to Save People

LeetCode: [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

Difficulty: Medium

Pattern: Sorted Two-Pointer Pairing

Why It Matters: Uses sorted extremes to prove each boat placement is locally safe.

Skills Tested:
- Recognize that pairing the heaviest with the lightest (when feasible) is provably optimal because the heaviest must always sit alone or with the lightest.
- State the invariant: two pointers, `light` and `heavy`; if `people[light] + people[heavy] <= limit`, both go on a boat and advance both; else only `heavy` goes alone.
- Handle equal weights (the loop terminates when `light > heavy`).
- Time O(n log n) for sort plus O(n) two-pointer, space O(1).

Common Follow-Ups:
- Container With Most Water (LC 11) shares the converging-pointers skeleton.
- What if a boat can fit three people (more complex DP).
- Generalize to weighted-cost boats with budgets.

## 8. Wiggle Subsequence

LeetCode: [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

Difficulty: Medium

Pattern: Direction Change Counting

Why It Matters: Compresses local direction changes into a global longest alternating subsequence.

Skills Tested:
- Recognize that a wiggle subsequence's length equals `1 + count of direction changes`, where flat segments do not count.
- State the invariant: keep `up` and `down` counts, where `up` is the wiggle length ending in an upward move, `down` is the same for downward.
- On each `nums[i] > nums[i - 1]`, set `up = down + 1`; symmetric on the downward direction.
- Time O(n), space O(1), and contrast with the O(n^2) DP that tracks longest wiggle ending at each index.

Common Follow-Ups:
- Longest Increasing Subsequence (LC 300) drops the alternating constraint.
- What if you must allow `k` non-wiggle moves.
- Generalize to wiggle by a threshold delta.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
