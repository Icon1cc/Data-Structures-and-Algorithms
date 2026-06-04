# Two Pointers Hard Problems

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

## 1. Trapping Rain Water

LeetCode: [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Difficulty: Hard

Pattern: Two Pointers With Boundary Max

Why It Matters: Requires proving which side can be finalized.

Skills Tested:
- Recognize that water at index `i` is `min(maxLeft[i], maxRight[i]) - height[i]`, and a two-pointer pass can avoid materializing both prefix-max arrays.
- State the invariant: while `height[left] < height[right]`, the left side's bottleneck is `leftMax`, so water at `left` is determined; symmetric for the right.
- Argue why advancing the side with the smaller height is provably safe even though the other prefix-max has not been computed.
- Time O(n), space O(1), and contrast with the prefix-max array O(n) space variant or the monotonic stack variant.

Common Follow-Ups:
- Trapping Rain Water II (LC 407) extends to a 2D grid and switches to a min-heap of border cells.
- Container With Most Water (LC 11) shares the converging-pointer skeleton with a different objective.
- What changes when heights are non-integer or arrive in a stream.

## 2. Find K-th Smallest Pair Distance

LeetCode: [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

Difficulty: Hard

Pattern: Pair Distance Counting Window

Why It Matters: Uses sorted pair counting to support binary search over answer distance.

Skills Tested:
- Recognize that "k-th smallest pair distance" is monotone in distance, so binary search the distance and count pairs with distance `<= mid` via a sliding window over sorted input.
- State the invariant: for sorted `nums`, fix `right` and find the smallest `left` with `nums[right] - nums[left] <= mid`; count of qualifying pairs ending at `right` is `right - left`.
- Handle duplicates (distance zero is valid), large arrays (counting must stay linear per binary-search step), and the binary-search bounds `[0, max - min]`.
- Time O(n log n + n log(max - min)), space O(1) extra, and contrast with a heap of all pairs which is O(n^2 log n).

Common Follow-Ups:
- Find K-th Smallest Sum of Two Sorted Arrays generalizes to two-array pair sums (LC 373 variant).
- Count of Smaller Numbers After Self (LC 315) counts a different pair predicate using a Fenwick tree.
- What if pair distance uses `|x - y|` modulo some value (the predicate stops being monotone).

## 3. Maximum Score of a Good Subarray

LeetCode: [Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/)

Difficulty: Hard

Pattern: Center Expansion Two Pointers

Why It Matters: Expands from a required index while preserving the best minimum value times width.

Skills Tested:
- Recognize that "the subarray must contain index `k`" plus "score is min times length" suggests expanding outward from `k` and always keeping the side that does not lower the running minimum more than the other.
- State the invariant: at every step, the current `[left, right]` contains `k` and its running minimum cannot be improved by retracting either side.
- Decide which side to extend by comparing `nums[left - 1]` against `nums[right + 1]` and growing toward the larger neighbor.
- Time O(n), space O(1), and contrast with monotonic-stack approaches that compute minimum-bounded rectangles globally.

Common Follow-Ups:
- Largest Rectangle in Histogram (LC 84) computes the same min-times-width score across all subarrays.
- Maximum of Minimum Values in All Subarrays of Size K (LC 239 variant).
- How does the answer change when the score is `sum(window) * min(window)`.

## 4. Count Subarrays With Fixed Bounds

LeetCode: [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

Difficulty: Hard

Pattern: Boundary Tracking Window

Why It Matters: Tracks last invalid, minimum, and maximum positions to count valid subarrays in one pass.

Skills Tested:
- Recognize that a subarray is valid only when its min equals `minK` and max equals `maxK`, which means tracking three indices: last out-of-range, last `minK`, last `maxK`.
- State the invariant: for each `right`, the count of valid subarrays ending at `right` is `max(0, min(lastMin, lastMax) - lastBad)`.
- Handle out-of-range values that reset `lastBad`, equal-bound cases (`minK == maxK`), and very long arrays without overflow.
- Time O(n), space O(1), and contrast with O(n^2) brute force that checks every pair.

Common Follow-Ups:
- Number of Subarrays with Bounded Maximum (LC 795) uses a similar three-pointer accounting.
- Count Subarrays Where Max Element Appears at Least K Times (LC 2962) reuses the boundary-counting trick.
- What if the bounds are dynamic and queries arrive online (offline sweep with Fenwick tree).

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
