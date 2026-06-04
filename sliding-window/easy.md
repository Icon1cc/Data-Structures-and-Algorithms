# Sliding Window Easy Problems

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

## 1. Best Time to Buy and Sell Stock

LeetCode: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Difficulty: Easy

Pattern: One-pass Window Minimum

Why It Matters: Builds the idea of retaining the best left boundary.

Skills Tested:
- Identify the One-pass Window Minimum signal before choosing a template.
- State the invariant for Best Time to Buy and Sell Stock: builds the idea of retaining the best left boundary.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Best Time to Buy and Sell Stock toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the One-pass Window Minimum invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Contains Duplicate II

LeetCode: [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

Difficulty: Easy

Pattern: Fixed Distance Window

Why It Matters: Tests membership within a moving index range.

Skills Tested:
- Identify the Fixed Distance Window signal before choosing a template.
- State the invariant for Contains Duplicate II: tests membership within a moving index range.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Contains Duplicate II toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Fixed Distance Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Maximum Average Subarray I

LeetCode: [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

Difficulty: Easy

Pattern: Fixed Window Sum

Why It Matters: The baseline fixed-size window problem.

Skills Tested:
- Identify the Fixed Window Sum signal before choosing a template.
- State the invariant for Maximum Average Subarray I: the baseline fixed-size window problem.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Maximum Average Subarray I toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Fixed Window Sum invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Longest Harmonious Subsequence

LeetCode: [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/)

Difficulty: Easy

Pattern: Frequency Range Window

Why It Matters: Uses counts over adjacent values after grouping.

Skills Tested:
- Identify the Frequency Range Window signal before choosing a template.
- State the invariant for Longest Harmonious Subsequence: uses counts over adjacent values after grouping.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Harmonious Subsequence toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Frequency Range Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Minimum Recolors to Get K Consecutive Black Blocks

LeetCode: [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)

Difficulty: Easy

Pattern: Fixed Window Count

Why It Matters: Small fixed-window problem with direct state update.

Skills Tested:
- Identify the Fixed Window Count signal before choosing a template.
- State the invariant for Minimum Recolors to Get K Consecutive Black Blocks: small fixed-window problem with direct state update.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Recolors to Get K Consecutive Black Blocks toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Fixed Window Count invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
