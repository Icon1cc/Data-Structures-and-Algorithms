# Heap / Priority Queue Hard Problems

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

## 1. Merge k Sorted Lists

LeetCode: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

Difficulty: Hard

Pattern: K-Way Merge Heap

Why It Matters: Most common heap merge problem.

Skills Tested:
- Recognize that merging k sorted lists is exactly a k-way merge: a min-heap of head pointers, popping the smallest, advancing it.
- State the invariant: the heap holds at most `k` nodes, one per active list head; each pop emits the next smallest into the merged list.
- Handle ties on values by comparing list indices (Python heap requires totally ordered tuples).
- Time O(N log k), space O(k), and contrast with pairwise-merging (O(N k)) and divide-and-conquer-merging (also O(N log k)).

Common Follow-Ups:
- Merge Two Sorted Lists (LC 21) is the base case used by the divide-and-conquer variant.
- Smallest Range Covering Elements From K Lists (LC 632) reuses k-way frontier on counts.
- What if lists are streams of unbounded length.

## 2. Find Median from Data Stream

LeetCode: [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

Difficulty: Hard

Pattern: Two Heaps Balanced

Why It Matters: Core streaming order statistic design.

Skills Tested:
- Recognize that the median is on the boundary between the lower half and the upper half, so a max-heap holds the lower half and a min-heap holds the upper.
- State the invariant: `len(low) == len(high)` or `len(low) == len(high) + 1`; the median is `top(low)` or `(top(low) + top(high)) / 2`.
- Push to the right heap, then rebalance by transferring at most one element across heaps.
- Per-call time O(log n), space O(n), and contrast with sorting on every query (O(n log n)).

Common Follow-Ups:
- Sliding Window Median (LC 480) extends with eviction via lazy deletion.
- What if the stream is bounded by a sliding K (k-window median).
- Generalize to arbitrary order statistics in a stream.

## 3. IPO

LeetCode: [IPO](https://leetcode.com/problems/ipo/)

Difficulty: Hard

Pattern: Sorted Capital Plus Profit Heap

Why It Matters: Selects best affordable project at each step.

Skills Tested:
- Recognize that you should always pick the most profitable project among those whose capital requirement is met by current capital.
- State the invariant: a min-heap of `(capital, profit)` ordered by capital pre-sorts projects by affordability; a max-heap of profits stores currently affordable projects.
- Each round, drain affordable projects from the capital heap into the profit heap, then take the top-profit.
- Time O((n + k) log n), space O(n), and explain the proof of greedy correctness.

Common Follow-Ups:
- Maximum Profit in Job Scheduling (LC 1235) layers DP on top of sorted starts.
- What if projects have time constraints and overlapping windows.
- Generalize to multiple wallets with different starting capitals.

## 4. Sliding Window Median

LeetCode: [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

Difficulty: Hard

Pattern: Two Heaps With Lazy Deletion

Why It Matters: Combines balance, stale removal, and window movement.

Skills Tested:
- Recognize that the streaming-median two-heaps trick must support eviction; lazy deletion (mark stale and skip on top) is the standard adapter.
- State the invariant: heap sizes still satisfy the median balance, ignoring stale entries; tops are cleaned before each query.
- Use a hash map of pending removals to detect stale entries when they reach the top.
- Per-call amortized O(log k), space O(k).

Common Follow-Ups:
- Find Median from Data Stream (LC 295) is the eviction-free version.
- What if the median must be exact under ties (use sorted multiset).
- Generalize to streaming percentiles (multiple heaps or t-digest).

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
