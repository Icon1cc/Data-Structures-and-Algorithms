# Intervals Easy Problems

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

## 1. Summary Ranges

LeetCode: [Summary Ranges](https://leetcode.com/problems/summary-ranges/)

Difficulty: Easy

Pattern: Run-Compression Of Sorted Values

Why It Matters: Turns sorted values into disjoint intervals.

Skills Tested:
- Recognize that the input is sorted and unique, so consecutive runs become single intervals like `"a->b"`.
- State the invariant: at each step, the current run starts at some `start`; if `nums[i + 1] != nums[i] + 1`, close the run and start a new one.
- Format singletons (`a == b`) as `"a"` and ranges as `"a->b"`.
- Time O(n), space O(n) for the output.

Common Follow-Ups:
- Missing Ranges (LC 163) prints the gaps.
- What if the input is unsorted (sort first or use a set).
- Streaming variant: emit a range when its successor breaks the run.

## 2. Meeting Rooms

LeetCode: [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

Difficulty: Easy

Pattern: Sort By Start, Check Adjacency

Why It Matters: Baseline interval conflict detection.

Skills Tested:
- Recognize that one person attends all meetings iff no pair overlaps, which is checked by sorting by start and verifying every adjacent pair.
- State the invariant: after sorting, if `intervals[i].start < intervals[i - 1].end`, an overlap exists.
- Decide whether to use `<` or `<=` based on whether touching endpoints conflict (problem-specific).
- Time O(n log n), space O(1) extra.

Common Follow-Ups:
- Meeting Rooms II (LC 253) returns the minimum rooms needed.
- What if meetings can be moved within their windows.
- Generalize to k people sharing meetings.

## 3. Merge Similar Items

LeetCode: [Merge Similar Items](https://leetcode.com/problems/merge-similar-items/)

Difficulty: Easy

Pattern: Counter Aggregation Then Sort

Why It Matters: Small range-like aggregation warm-up.

Skills Tested:
- Recognize that this is essentially a counter on values, summing weights for repeated keys, then sorting by value.
- State the invariant: a hash map from value to summed weight is built in one pass; sort the items at the end.
- Handle cases where a value appears in only one of the two lists.
- Time O((n + m) log (n + m)), space O(n + m).

Common Follow-Ups:
- Generalize to multi-list merging with arbitrary aggregation.
- Streaming variant: maintain the merged list under online inserts.
- What if the aggregation is max instead of sum.

## 4. Maximum Population Year

LeetCode: [Maximum Population Year](https://leetcode.com/problems/maximum-population-year/)

Difficulty: Easy

Pattern: Sweep Line On Years

Why It Matters: Introduces the standard sweep-line counter without merging.

Skills Tested:
- Recognize that life intervals can be folded into delta events: `delta[birth] += 1`, `delta[death] -= 1`, then prefix sum to get population per year.
- State the invariant: after the prefix sweep, `population[y] = total alive during year y`.
- Tie-break by earliest year when multiple years share the maximum.
- Time O(year range + n), space O(year range).

Common Follow-Ups:
- Car Pooling (LC 1094) uses the same delta technique on a route.
- What if the year range is huge (compress timestamps and use sorted events).
- Generalize to sliding-window queries on event counts.

## 5. Determine if Two Events Have Conflict

LeetCode: [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/)

Difficulty: Easy

Pattern: Interval Overlap Predicate

Why It Matters: Cleanest possible interval-overlap predicate.

Skills Tested:
- Recognize that two intervals `(a, b)` and `(c, d)` overlap iff `a <= d` and `c <= b`.
- State the invariant: the negation captures non-overlap (`b < c` or `d < a`); the positive form is the standard formula.
- Convert string times like `"HH:MM"` into integers (`60 * H + M`) before comparing.
- Time O(1), space O(1), and explain why the formula generalizes to closed intervals only.

Common Follow-Ups:
- Meeting Rooms (LC 252) extends to arbitrary numbers of intervals.
- What if intervals are open or half-open.
- Generalize to k events overlapping at any point.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
