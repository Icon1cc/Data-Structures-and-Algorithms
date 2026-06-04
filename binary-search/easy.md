# Binary Search Easy Problems

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

## 1. Binary Search

LeetCode: [Binary Search](https://leetcode.com/problems/binary-search/)

Difficulty: Easy

Pattern: Classic Target Search

Why It Matters: Baseline exact lookup with clear inclusive bounds.

Skills Tested:
- Recognize that a sorted array plus exact-match query is the textbook `[lo, hi]` bisection over comparisons.
- State the invariant: the answer, if any, lies in `[lo, hi]`, and `mid = lo + (hi - lo) // 2` avoids the integer overflow that `(lo + hi) // 2` causes in lower-level languages.
- Handle empty arrays, missing targets (return `-1`), and very large indices.
- Time O(log n), space O(1), and contrast with linear scan O(n).

Common Follow-Ups:
- Search Insert Position (LC 35) returns the lower-bound index instead of `-1`.
- Find First and Last Position of Element in Sorted Array (LC 34) reuses two binary searches.
- What if the array is sorted but stored externally and only the comparator is exposed.

## 2. Search Insert Position

LeetCode: [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Difficulty: Easy

Pattern: Lower Bound

Why It Matters: Turns missing targets into insertion boundaries.

Skills Tested:
- Recognize that "where would `target` go to keep the array sorted" is exactly `bisect_left` over the array.
- State the invariant: `lo` always points to the smallest index whose value is `>= target`, and `hi` is the smallest known index that is `> target` (or `n`).
- Handle a target smaller than all values (return 0), larger than all (return `n`), and equal to an existing value (return that index).
- Time O(log n), space O(1), and explain why a `<= target` mid-condition shifts to `bisect_right`.

Common Follow-Ups:
- Find First and Last Position (LC 34) is `lower_bound` paired with `upper_bound`.
- How would you support online inserts that keep the array sorted (skip list or balanced BST).
- What if duplicates must be inserted at a specific occurrence index.

## 3. First Bad Version

LeetCode: [First Bad Version](https://leetcode.com/problems/first-bad-version/)

Difficulty: Easy

Pattern: First True Predicate

Why It Matters: The cleanest monotonic predicate example.

Skills Tested:
- Recognize that "find the smallest version where `isBad(v)` is true" is binary search over a monotone boolean predicate.
- State the invariant: `lo` is the smallest possibly-bad version, `hi` is a known bad version, so the loop ends with `lo == hi == answer`.
- Avoid `(lo + hi) // 2` overflow on very large `n` by computing `lo + (hi - lo) // 2`.
- Time O(log n), space O(1), and minimize calls to `isBadVersion` since each call is the API cost.

Common Follow-Ups:
- Find Peak Element (LC 162) replaces the boolean predicate with a slope-based one.
- What if `isBad` is sometimes flaky and you need to retry queries.
- Generalize to "first version satisfying any monotone predicate".

## 4. Guess Number Higher or Lower

LeetCode: [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

Difficulty: Easy

Pattern: Three-Way Compare Search

Why It Matters: Practices halving based on comparison feedback.

Skills Tested:
- Recognize that the API returns -1, 0, 1, which is a three-way comparator over the search range.
- State the invariant: the secret number is always inside `[lo, hi]`, narrowed by the API's response.
- Handle the boundary correctly when `lo == hi` (the only candidate must be the answer if the API says 0).
- Time O(log n), space O(1), and discuss the API call budget if it were limited.

Common Follow-Ups:
- Guess Number Higher or Lower II (LC 375) optimizes the worst-case cost using DP.
- What if the comparator can lie with a known probability.
- How does the analysis change when guesses cost different amounts.

## 5. Sqrt(x)

LeetCode: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Difficulty: Easy

Pattern: Binary Search On Answer

Why It Matters: Introduces numeric answer search with overflow awareness.

Skills Tested:
- Recognize that `floor(sqrt(x))` is the largest integer `r` with `r * r <= x`, a monotone predicate solved by binary search on `r`.
- State the invariant: `lo` is a candidate that could be the answer, `hi` is one larger than the worst-case answer; the loop returns `hi - 1` (or `lo`) depending on the chosen template.
- Handle overflow on `r * r` by using `r > x / r` instead in lower-level languages.
- Time O(log x), space O(1), and contrast with Newton's method which is faster but harder to bound.

Common Follow-Ups:
- Valid Perfect Square (LC 367) replaces the floor with an exact check.
- Implement integer cube root with the same skeleton.
- How does the algorithm extend to fixed-point sqrt with `k` decimal digits.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
