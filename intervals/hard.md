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

Pattern: K-Way Merge Then Gaps

Why It Matters: Finds gaps after merging busy intervals.

Skills Tested:
- Recognize that free time is the complement of the union of busy intervals; build the union via Merge Intervals applied across all employees.
- State the invariant: after merging, free time consists of gaps `(merged[i].end, merged[i + 1].start)`.
- A min-heap of `(start, employeeIdx, intervalIdx)` enables k-way merging in O(N log K).
- Time O(N log K) where N is total intervals and K is employees, space O(N).

Common Follow-Ups:
- Merge Intervals (LC 56) is the underlying primitive.
- What if employees have different time zones.
- Generalize to k-employee free-time intersection (everyone simultaneously free).

## 2. Data Stream as Disjoint Intervals

LeetCode: [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

Difficulty: Hard

Pattern: Online Disjoint Interval Maintenance

Why It Matters: Maintains intervals under online insertions.

Skills Tested:
- Recognize that on each `addNum`, you must merge with the predecessor and successor intervals if they touch the new value.
- State the invariant: a sorted-by-start ordered map; insert finds at most two neighboring intervals to potentially merge into.
- Use `SortedList` (Python) or `TreeMap` (Java) for O(log n) per insert.
- Per-add time O(log n), getIntervals O(n) to materialize.

Common Follow-Ups:
- Range Module (LC 715) supports both add and remove.
- Stream output as ranges become finalized.
- What if duplicates can decrement counts.

## 3. Count Integers in Intervals

LeetCode: [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/)

Difficulty: Hard

Pattern: Online Merge With Total Count

Why It Matters: Tracks covered counts after merges.

Skills Tested:
- Recognize that each `add(left, right)` may swallow several existing intervals; track a running total of integers covered.
- State the invariant: a sorted-by-start ordered map of disjoint intervals; on an add, remove every overlapping interval, subtract its size from the total, then insert the merged super-interval and add its size.
- Use `SortedList` for O(log n) lookup and removal.
- Per-add amortized O(log n + k) where k is intervals removed; total operations bounded by total inserts.

Common Follow-Ups:
- My Calendar III (LC 732) tracks max overlap rather than total covered.
- Range Module (LC 715) adds remove operations.
- Stream coverage queries online.

## 4. My Calendar III

LeetCode: [My Calendar III](https://leetcode.com/problems/my-calendar-iii/)

Difficulty: Hard

Pattern: Sweep Line With Sorted Map

Why It Matters: Returns maximum concurrent bookings online.

Skills Tested:
- Recognize that the running max of overlap can be maintained via a sorted-map of `time -> delta`; the answer is the running maximum after each insert.
- State the invariant: a `SortedDict` where each key holds the change in active bookings at that time; iterating in sorted order gives the running active count.
- For online queries with many inserts, use a segment tree with lazy propagation for O(log T) per insert.
- Per-call time O(n log n) with sorted dict, space O(n).

Common Follow-Ups:
- My Calendar I (LC 729) and II (LC 731) are simpler variants.
- Range Add and Range Max queries with a segment tree.
- What if inserts can be undone.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
