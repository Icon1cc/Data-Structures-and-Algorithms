# Binary Search Medium Problems

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

## 1. Search in Rotated Sorted Array

LeetCode: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Difficulty: Medium

Pattern: Rotated Sorted Search

Why It Matters: Tests identifying the sorted half.

Skills Tested:
- Recognize that on every step at least one half `[lo, mid]` or `[mid, hi]` is sorted, so you can decide whether `target` lies in the sorted half.
- State the invariant: after deciding which half contains `target`, the search range halves while preserving the rotated-sorted structure.
- Handle the comparison ties at `mid` (no duplicates here, so equality with target wins immediately).
- Time O(log n), space O(1), and contrast with the duplicates variant (LC 81) which falls back to O(n) worst case.

Common Follow-Ups:
- Search in Rotated Sorted Array II (LC 81) handles duplicates by skipping equal endpoints.
- Find Minimum in Rotated Sorted Array (LC 153) finds the pivot itself.
- How would the answer change if rotation is unknown but the array is rotated some count of times.

## 2. Find Minimum in Rotated Sorted Array

LeetCode: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Difficulty: Medium

Pattern: Rotated Pivot Search

Why It Matters: Finds a pivot without scanning.

Skills Tested:
- Recognize that the minimum sits at the rotation pivot, which is the only place where `nums[i] < nums[i - 1]`.
- State the invariant: while `nums[lo] > nums[hi]`, the minimum lies in `(mid, hi]` if `nums[mid] > nums[hi]`, else in `[lo, mid]`.
- Handle a non-rotated array (`nums[0] < nums[-1]`, return `nums[0]`) as an early case.
- Time O(log n), space O(1), and explain why comparing `nums[mid]` to `nums[lo]` is more error-prone than comparing to `nums[hi]`.

Common Follow-Ups:
- Find Minimum in Rotated Sorted Array II (LC 154) handles duplicates by shrinking `hi` when `nums[mid] == nums[hi]`.
- Search in Rotated Sorted Array (LC 33) builds on the pivot idea to find a target.
- How does the algorithm change if rotation count is bounded by a small `k`.

## 3. Time Based Key-Value Store

LeetCode: [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

Difficulty: Medium

Pattern: Floor Lookup

Why It Matters: Uses binary search inside a data structure.

Skills Tested:
- Recognize that `get(key, t)` is "find the largest stored timestamp `<= t`", which is a `bisect_right - 1` over the per-key timestamp list.
- State the invariant: per-key lists are kept sorted by insertion order (timestamps are strictly increasing per problem), so binary search applies directly.
- Handle missing keys (return ""), all timestamps too large (return ""), and exact matches (`bisect_right` returns the index just past).
- Per-call time O(log n), space O(n total entries), and contrast with a flat dict-of-(key, time) which lacks ordering.

Common Follow-Ups:
- Snapshot Array (LC 1146) reuses the same idea over set/snap/get operations.
- What if timestamps can arrive out of order (insert with `bisect.insort`).
- Generalize to range queries: all values for `key` in `[t1, t2]`.

## 4. Koko Eating Bananas

LeetCode: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

Difficulty: Medium

Pattern: Binary Search On Answer

Why It Matters: Classic minimum feasible speed problem.

Skills Tested:
- Recognize that hours required is monotonically non-increasing in eating speed `k`, so binary search on `k` over `[1, max(piles)]`.
- State the invariant: the predicate `hours(k) <= h` is monotone in `k`; the smallest feasible `k` is the answer.
- Compute `hours(k) = sum(ceil(p / k) for p in piles)` correctly using `(p + k - 1) // k`.
- Time O(n log max(piles)), space O(1), and explain why naive linear search costs O(n * max(piles)).

Common Follow-Ups:
- Capacity To Ship Packages Within D Days (LC 1011) uses the same template with a different feasibility predicate.
- Minimum Time to Complete Trips (LC 2187) reuses binary search on time.
- What if eating rates can vary across hours.

## 5. Capacity To Ship Packages Within D Days

LeetCode: [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

Difficulty: Medium

Pattern: Binary Search On Answer

Why It Matters: Tests feasibility over contiguous loading.

Skills Tested:
- Recognize that days required is monotonically non-increasing in ship capacity, so binary search on capacity over `[max(weights), sum(weights)]`.
- State the invariant: feasibility checks via greedy packing run a single pass and count days needed.
- Handle the lower bound `max(weights)` (any smaller capacity cannot fit a single package), and the upper `sum(weights)` (one-day shipment).
- Time O(n log sum(weights)), space O(1), and contrast with DP which is O(n^2 * D).

Common Follow-Ups:
- Split Array Largest Sum (LC 410) is the same problem with k partitions.
- What if packages can be reordered (still the same answer if order does not matter, since min-capacity binds).
- Generalize to multiple ships per day.

## 6. Search a 2D Matrix

LeetCode: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

Difficulty: Medium

Pattern: Flattened Matrix Binary Search

Why It Matters: Practices flattening a globally sorted matrix.

Skills Tested:
- Recognize that the row-major-sorted matrix is conceptually a 1-D sorted array of length `m * n`, so binary search over indices `[0, m*n)`.
- State the invariant: index `idx` maps to cell `(idx // n, idx % n)`, and the comparison resolves on the cell's value.
- Handle empty matrices (`m == 0` or `n == 0`) and large products without overflow.
- Time O(log(m * n)), space O(1), and contrast with two binary searches (find row, then column) which is also O(log m + log n).

Common Follow-Ups:
- Search a 2D Matrix II (LC 240) drops the global-sort property and uses staircase search.
- Kth Smallest Element in a Sorted Matrix (LC 378) layers a heap on top.
- How would you support online insertions that keep the order.

## 7. Find Peak Element

LeetCode: [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

Difficulty: Medium

Pattern: Slope Search

Why It Matters: Uses slope direction rather than exact target.

Skills Tested:
- Recognize that `nums[-1] = nums[n] = -inf` guarantees a peak somewhere; the slope at `mid` decides which half contains a peak.
- State the invariant: a peak always lies in the half whose endpoint is higher, because climbing uphill must eventually plateau or descend.
- Handle equal neighbors (the problem promises distinct adjacent values, but state the assumption clearly).
- Time O(log n), space O(1), and explain why a linear scan is O(n).

Common Follow-Ups:
- Find Peak Element II (LC 1901) extends to a 2-D grid with O(m log n).
- What if multiple peaks exist (return any).
- Generalize to find a local-min in a noisy 1-D function.

## 8. Successful Pairs of Spells and Potions

LeetCode: [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

Difficulty: Medium

Pattern: Lower Bound After Sort

Why It Matters: Combines sorting with boundary counts.

Skills Tested:
- Recognize that for each spell, the count of successful potions is `len(potions) - bisect_left(potions, ceil(success / spell))`.
- State the invariant: after sorting potions, every potion at index `>= threshold` is successful, every potion below is not.
- Handle integer-division ceiling without floating point: use `(success + spell - 1) // spell`.
- Time O((n + m) log m), space O(1) extra, and contrast with the brute O(n * m) pairwise count.

Common Follow-Ups:
- Two Pointers approach when both spells and potions are sorted.
- What if the success threshold varies per spell.
- Generalize to "for each query, count entries in another sorted set above a threshold".

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
