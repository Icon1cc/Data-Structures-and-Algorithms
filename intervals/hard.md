# Intervals Hard Problems

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

## 1. Employee Free Time

LeetCode: [Employee Free Time](https://leetcode.com/problems/employee-free-time/)

Difficulty: Hard

Pattern: Merge Intervals

Why It Matters: Finds gaps after merging busy intervals.

Skills Tested:
- Identify the Merge Intervals signal before choosing a template.
- State the invariant for Employee Free Time: finds gaps after merging busy intervals.
- Handle equal endpoints, open versus closed intervals, empty interval lists, and event tie order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Employee Free Time toward greedy, heap, difference array, binary search tree, or line sweep?
- Which equal endpoints case would break the first implementation?
- Can the Merge Intervals invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Data Stream as Disjoint Intervals

LeetCode: [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

Difficulty: Hard

Pattern: Dynamic Interval Merge

Why It Matters: Maintains intervals under online insertions.

Skills Tested:
- Identify the Dynamic Interval Merge signal before choosing a template.
- State the invariant for Data Stream as Disjoint Intervals: maintains intervals under online insertions.
- Handle equal endpoints, open versus closed intervals, empty interval lists, and event tie order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Data Stream as Disjoint Intervals toward greedy, heap, difference array, binary search tree, or line sweep?
- Which equal endpoints case would break the first implementation?
- Can the Dynamic Interval Merge invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Count Integers in Intervals

LeetCode: [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/)

Difficulty: Hard

Pattern: Dynamic Interval Counting

Why It Matters: Tracks covered counts after merges.

Skills Tested:
- Identify the Dynamic Interval Counting signal before choosing a template.
- State the invariant for Count Integers in Intervals: tracks covered counts after merges.
- Handle equal endpoints, open versus closed intervals, empty interval lists, and event tie order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Count Integers in Intervals toward greedy, heap, difference array, binary search tree, or line sweep?
- Which equal endpoints case would break the first implementation?
- Can the Dynamic Interval Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. My Calendar III

LeetCode: [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

Difficulty: Hard

Pattern: Sweep Line

Why It Matters: Returns maximum concurrent bookings online.

Skills Tested:
- Identify the Sweep Line signal before choosing a template.
- State the invariant for My Calendar III: returns maximum concurrent bookings online.
- Handle equal endpoints, open versus closed intervals, empty interval lists, and event tie order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push My Calendar III toward greedy, heap, difference array, binary search tree, or line sweep?
- Which equal endpoints case would break the first implementation?
- Can the Sweep Line invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
