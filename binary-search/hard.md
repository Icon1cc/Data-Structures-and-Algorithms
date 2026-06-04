# Binary Search Hard Problems

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

## 1. Median of Two Sorted Arrays

LeetCode: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Difficulty: Hard

Pattern: Binary Search Partition

Why It Matters: High-value boundary partition problem.

Skills Tested:
- Recognize that finding the median means partitioning both arrays into left and right halves of the right total size, with `max(leftA, leftB) <= min(rightA, rightB)`.
- State the invariant: binary search the partition `i` in the shorter array; `j = (m + n + 1) // 2 - i` keeps the left side sized correctly.
- Handle empty halves with `+inf` / `-inf` sentinels and ensure the binary search runs over the shorter array (`O(log min(m, n))`).
- Time O(log min(m, n)), space O(1), and contrast with the merge-and-pick approach which is O(m + n).

Common Follow-Ups:
- Find K-th Smallest Element in Two Sorted Arrays.
- Sliding-median problems use a multiset or two heaps.
- How does the algorithm extend to three sorted arrays.

## 2. Split Array Largest Sum

LeetCode: [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

Difficulty: Hard

Pattern: Binary Search On Answer

Why It Matters: Minimizes the largest partition sum with monotonic feasibility.

Skills Tested:
- Recognize that "split into `k` contiguous parts and minimize the largest sum" has a monotone feasibility predicate `canSplit(maxSum) -> bool`, so binary search the answer over `[max(nums), sum(nums)]`.
- State the invariant: `canSplit` greedily packs into the current partition until adding the next number would exceed `maxSum`, then opens a new partition.
- Handle the bounds `lo = max(nums)` (one element must fit) and `hi = sum(nums)` (single partition).
- Time O(n log sum(nums)), space O(1), and contrast with DP which is O(n^2 * k).

Common Follow-Ups:
- Capacity To Ship Packages Within D Days (LC 1011) is the same problem with a different name.
- Painter's Partition is a classic variant.
- What if numbers can be reordered before partitioning (no longer the same problem).

## 3. Find Minimum in Rotated Sorted Array II

LeetCode: [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Difficulty: Hard

Pattern: Rotated Search With Duplicates

Why It Matters: Shows how duplicates weaken logarithmic guarantees.

Skills Tested:
- Recognize that with duplicates, `nums[mid] == nums[hi]` makes neither side certain to contain the minimum, so the safe move is to decrement `hi` by one.
- State the invariant: the minimum still lies in `[lo, hi]` after each step, but the worst case loses log-time when many duplicates collapse the search.
- Handle the case where `nums` is fully constant (the loop degenerates to linear).
- Time O(log n) average, O(n) worst case, and contrast with the no-duplicates LC 153.

Common Follow-Ups:
- Search in Rotated Sorted Array II (LC 81) shares the duplicate-handling trick.
- What is the deterministic worst-case cost over all permutations of duplicates.
- How could randomization improve the expected cost in pathological inputs.

## 4. Kth Smallest Number in Multiplication Table

LeetCode: [Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

Difficulty: Hard

Pattern: Binary Search On Value With Counting

Why It Matters: Searches answer value using a counting predicate.

Skills Tested:
- Recognize that the count of cells `<= v` in an `m x n` multiplication table equals `sum(min(v // i, n) for i in 1..m)`, which is monotone in `v`.
- State the invariant: binary search `v` over `[1, m * n]` and find the smallest value whose count is `>= k`.
- Handle the bound where `count(v - 1) < k <= count(v)` so the answer is exactly `v`.
- Time O(m log(m * n)), space O(1), and contrast with the heap approach (O(k log k)) which is impractical for large `k`.

Common Follow-Ups:
- Find K-th Smallest Pair Distance (LC 719) reuses the binary-search-on-answer-with-counting pattern.
- Kth Smallest Element in a Sorted Matrix (LC 378) extends to a sorted matrix.
- What if entries are weighted with arbitrary scores.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
