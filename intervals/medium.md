# Intervals Medium Problems

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

## 1. Merge Intervals

LeetCode: [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

Difficulty: Medium

Pattern: Sort By Start, Sweep Merge

Why It Matters: Core sorted merge pattern.

Skills Tested:
- Recognize that after sorting by start, two adjacent intervals merge iff `cur.start <= last.end`.
- State the invariant: the result list is always disjoint and sorted; on a merge, extend `last.end = max(last.end, cur.end)`.
- Decide whether touching intervals (`cur.start == last.end`) merge based on the problem statement.
- Time O(n log n), space O(n) for output.

Common Follow-Ups:
- Insert Interval (LC 57) reuses merge into a sorted list.
- Employee Free Time (LC 759) inverts merged intervals to gaps.
- What if intervals carry weights to be summed on merge.

## 2. Insert Interval

LeetCode: [Insert Interval](https://leetcode.com/problems/insert-interval/)

Difficulty: Medium

Pattern: Three-Phase Sweep

Why It Matters: Linear insertion into sorted disjoint intervals.

Skills Tested:
- Recognize three regions: intervals before the new one (no overlap), intervals overlapping the new one (merge), and intervals after.
- State the invariant: the result is built by appending each region in turn; the merged interval expands to cover all overlapping originals.
- Handle the empty-input case and the new interval lying entirely before or after all originals.
- Time O(n), space O(n) for output.

Common Follow-Ups:
- Merge Intervals (LC 56) is the from-scratch merge.
- Stream interval inserts and maintain the disjoint set.
- Generalize to weighted intervals with sum-on-merge.

## 3. Non-overlapping Intervals

LeetCode: [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

Difficulty: Medium

Pattern: Earliest End Greedy (Activity Selection)

Why It Matters: Classic removal by earliest end.

Skills Tested:
- Recognize that to keep the most non-overlapping intervals, sort by end and greedily keep each interval whose start is at least the last kept end.
- State the invariant: the kept set is the maximum-cardinality non-overlapping subset (provable by exchange argument).
- The answer is `n - kept`.
- Time O(n log n), space O(1) extra.

Common Follow-Ups:
- Minimum Number of Arrows to Burst Balloons (LC 452) flips the problem to interval intersection.
- Activity Selection generalizes with weights.
- Stream intervals and maintain the optimum online.

## 4. Meeting Rooms II

LeetCode: [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

Difficulty: Medium

Pattern: Sweep Line Or Min-Heap

Why It Matters: Computes minimum concurrent resources.

Skills Tested:
- Recognize that the answer equals the maximum overlap, which is found by sweeping events `(time, +1 for start, -1 for end)` and tracking the running maximum.
- State the invariant: at any sweep time `t`, the running counter equals the count of meetings active.
- Handle ties: process end-events before start-events at the same timestamp so a meeting ending exactly when another begins does not require an extra room.
- Time O(n log n), space O(n).

Common Follow-Ups:
- Car Pooling (LC 1094) is a route-based variant.
- Generalize to weighted resources per meeting.
- My Calendar III (LC 732) is the streaming variant.

## 5. Minimum Number of Arrows to Burst Balloons

LeetCode: [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

Difficulty: Medium

Pattern: Earliest-End Interval Greedy

Why It Matters: Uses overlap intersection to minimize shots.

Skills Tested:
- Recognize that one arrow can burst all balloons sharing a common point; minimizing arrows is equivalent to picking points using the earliest-end-greedy.
- State the invariant: sort by end; current arrow position is the smallest end seen; advance only when the next start exceeds that end.
- Handle large coordinates by using 64-bit comparisons.
- Time O(n log n), space O(1) extra.

Common Follow-Ups:
- Non-overlapping Intervals (LC 435) is the inverse formulation.
- What if arrows have a finite radius (cover a range).
- Generalize to k arrows that may merge.

## 6. Car Pooling

LeetCode: [Car Pooling](https://leetcode.com/problems/car-pooling/)

Difficulty: Medium

Pattern: Difference Array

Why It Matters: Models passenger changes over a route.

Skills Tested:
- Recognize that `delta[from] += passengers, delta[to] -= passengers` plus a prefix sum yields the number of passengers at every timestamp.
- State the invariant: after the prefix sum, the running total never exceeds capacity.
- Handle large `to` values by using a hash map (or compressing coordinates) when the route is sparse.
- Time O(n + maxTime), space O(maxTime).

Common Follow-Ups:
- My Calendar III (LC 732) is the streaming sweep-line cousin.
- Generalize to a route with reservations and refunds.
- Multiple cars with different capacities.

## 7. My Calendar I

LeetCode: [My Calendar I](https://leetcode.com/problems/my-calendar-i/)

Difficulty: Medium

Pattern: Online Interval Conflict

Why It Matters: Designs booking without overlap.

Skills Tested:
- Recognize that adding a new booking is rejected iff it overlaps any existing one; an ordered set or balanced BST gives O(log n) per insert.
- State the invariant: stored intervals are disjoint; the floor predecessor and the ceiling successor are the only candidates for conflict.
- Use `SortedList` (Python) or `TreeMap` (Java) to support O(log n) lookups.
- Per-call time O(log n), space O(n).

Common Follow-Ups:
- My Calendar II (LC 731) allows one overlap.
- My Calendar III (LC 732) returns the maximum overlap so far.
- Streaming variant with deletions.

## 8. Interval List Intersections

LeetCode: [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

Difficulty: Medium

Pattern: Two-Pointer Merge On Two Sorted Lists

Why It Matters: Practices advancing the interval whose endpoint expires first while recording overlaps.

Skills Tested:
- Recognize that two sorted disjoint interval lists are walked in parallel; an intersection exists iff `max(a.start, b.start) <= min(a.end, b.end)`.
- State the invariant: the pointer to the interval with the smaller end advances; the other waits for the next overlap.
- Output the intersection only when it is valid; do not emit empty intersections.
- Time O(m + n), space O(m + n) for output.

Common Follow-Ups:
- Merge Intervals (LC 56) is the union counterpart.
- Interval intersection on three sorted lists.
- What if intervals are weighted (sum weights of overlapping pairs).

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
