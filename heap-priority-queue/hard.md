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

Pattern: K-way Merge

Why It Matters: Most common heap merge problem.

Skills Tested:
- Identify the K-way Merge signal before choosing a template.
- State the invariant for Merge k Sorted Lists: most common heap merge problem.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Merge k Sorted Lists toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the K-way Merge invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Find Median from Data Stream

LeetCode: [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

Difficulty: Hard

Pattern: Two Heaps

Why It Matters: Core streaming order statistic design.

Skills Tested:
- Identify the Two Heaps signal before choosing a template.
- State the invariant for Find Median from Data Stream: core streaming order statistic design.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find Median from Data Stream toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Two Heaps invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. IPO

LeetCode: [IPO](https://leetcode.com/problems/ipo/)

Difficulty: Hard

Pattern: Heap-Assisted Greedy

Why It Matters: Selects best affordable project at each step.

Skills Tested:
- Identify the Heap-Assisted Greedy signal before choosing a template.
- State the invariant for IPO: selects best affordable project at each step.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push IPO toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Heap-Assisted Greedy invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Sliding Window Median

LeetCode: [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

Difficulty: Hard

Pattern: Two Heaps With Lazy Deletion

Why It Matters: Combines balance, stale removal, and window movement.

Skills Tested:
- Identify the Two Heaps With Lazy Deletion signal before choosing a template.
- State the invariant for Sliding Window Median: combines balance, stale removal, and window movement.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sliding Window Median toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Two Heaps With Lazy Deletion invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
