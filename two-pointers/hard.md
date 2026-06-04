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
- Identify the Two Pointers With Boundary Max signal before choosing a template.
- State the invariant for Trapping Rain Water: requires proving which side can be finalized.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Trapping Rain Water toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Two Pointers With Boundary Max invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Find K-th Smallest Pair Distance

LeetCode: [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

Difficulty: Hard

Pattern: Pair Distance Counting Window

Why It Matters: Uses sorted pair counting to support binary search over answer distance.

Skills Tested:
- Identify the Pair Distance Counting Window signal before choosing a template.
- State the invariant for Find K-th Smallest Pair Distance: uses sorted pair counting to support binary search over answer distance.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find K-th Smallest Pair Distance toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Pair Distance Counting Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Maximum Score of a Good Subarray

LeetCode: [Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/)

Difficulty: Hard

Pattern: Center Expansion Two Pointers

Why It Matters: Expands from a required index while preserving the best minimum value times width.

Skills Tested:
- Identify the Center Expansion Two Pointers signal before choosing a template.
- State the invariant for Maximum Score of a Good Subarray: expands from a required index while preserving the best minimum value times width.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Maximum Score of a Good Subarray toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Center Expansion Two Pointers invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Count Subarrays With Fixed Bounds

LeetCode: [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

Difficulty: Hard

Pattern: Boundary Tracking Window

Why It Matters: Tracks last invalid, minimum, and maximum positions to count valid subarrays in one pass.

Skills Tested:
- Identify the Boundary Tracking Window signal before choosing a template.
- State the invariant for Count Subarrays With Fixed Bounds: tracks last invalid, minimum, and maximum positions to count valid subarrays in one pass.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Count Subarrays With Fixed Bounds toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Boundary Tracking Window invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
