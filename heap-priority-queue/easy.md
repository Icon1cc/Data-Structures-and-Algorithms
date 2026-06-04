# Heap / Priority Queue Easy Problems

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

## 1. Last Stone Weight

LeetCode: [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

Difficulty: Easy

Pattern: Max Heap Simulation

Why It Matters: Baseline repeated maximum extraction.

Skills Tested:
- Recognize that "smash the two heaviest stones" repeats max-extract twice and may push the diff back, which is a max-heap simulation.
- State the invariant: the heap always holds the unsmashed stones; popping the top twice yields the two heaviest.
- Use Python's `heapq` (min-heap) by negating values, or the `max-heap` directly in languages that support it.
- Time O(n log n), space O(n), and explain why repeatedly sorting is O(n^2 log n).

Common Follow-Ups:
- Last Stone Weight II (LC 1049) becomes a subset-sum DP problem.
- What if smashes can be batched in pairs.
- How does the answer change with a heap that supports decrease-key.

## 2. Kth Largest Element in a Stream

LeetCode: [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

Difficulty: Easy

Pattern: Min-Heap Of Size K

Why It Matters: Maintains kth largest under streaming updates.

Skills Tested:
- Recognize that the kth largest at any moment is the minimum of the top-k largest seen so far, which is a min-heap of size `k`.
- State the invariant: the heap always contains the k largest elements seen, so the heap top is the answer to every query.
- On each `add`, push and pop only when size exceeds `k`.
- Per-call time O(log k), space O(k), and contrast with sorting on every add (O(n log n)).

Common Follow-Ups:
- Kth Largest Element in an Array (LC 215) is the offline counterpart.
- Sliding-Window K Largest reuses the heap idea with eviction.
- What if `k` itself can change between calls.

## 3. Relative Ranks

LeetCode: [Relative Ranks](https://leetcode.com/problems/relative-ranks/)

Difficulty: Easy

Pattern: Sort Or Heap Ranking

Why It Matters: Connects priority ordering to ranked output.

Skills Tested:
- Recognize that ranks are determined by sorting the scores and walking from largest to smallest, but a heap can also stream ranks online.
- State the invariant: pairs of `(score, original_index)` sorted descending by score yield rank assignments in order.
- Handle ties (the problem guarantees unique scores; state the assumption).
- Time O(n log n), space O(n), and discuss why a heap is overkill in the offline setting.

Common Follow-Ups:
- Top K Frequent Elements (LC 347) extends the sort-by-key idea with frequencies.
- What if scores can update online.
- Generalize to fractional ranks under ties.

## 4. Take Gifts From the Richest Pile

LeetCode: [Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)

Difficulty: Easy

Pattern: Max Heap Simulation

Why It Matters: Practices repeated best-item updates.

Skills Tested:
- Recognize that each round operates only on the current maximum pile, which is exactly a max-heap pop and push.
- State the invariant: after each round, the heap contains all piles, with the most recently floored value pushed back.
- Apply `floor(sqrt(top))` correctly using integer math (`isqrt` or `int(top ** 0.5)`).
- Time O((n + k) log n), space O(n), and contrast with iterating the array each round (O(k * n)).

Common Follow-Ups:
- Maximum Subsequence Score (LC 2542) reuses max-heap simulation with a paired weight.
- What if the operation depends on the second-largest as well.
- How does the answer change for `k` very large compared to `n`.

## 5. The K Weakest Rows in a Matrix

LeetCode: [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)

Difficulty: Easy

Pattern: Min-Heap By Composite Key

Why It Matters: Pairs sorted-row reasoning with a top-k heap and binary search per row.

Skills Tested:
- Recognize that each row's "strength" is the count of leading ones (binary search on `0`), and the answer is the k smallest by `(strength, index)`.
- State the invariant: a heap of `(strength, index)` ordered ascending yields the k weakest with `nlargest`/`nsmallest` style extraction.
- Use binary search (each row is sorted: ones then zeros) to compute the strength in O(log n) per row.
- Time O(m log n + m log k), space O(m), and contrast with sorting all rows directly which is O(m log m).

Common Follow-Ups:
- K Closest Points to Origin (LC 973) reuses the same min-heap-of-tuples pattern.
- What if rows are unsorted (each row's count requires O(n)).
- How would you stream rows and maintain the top-k.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
