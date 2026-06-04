# Intervals Patterns

This file is the main pattern-recognition reference for intervals. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Merge Intervals

### Intuition

Sort by start and combine intervals that overlap the active interval.

### When To Use It

Use when output should be disjoint ranges.

### When Not To Use It

Do not use merge when overlapping intervals should be counted separately.

### Recognition Signals

- merge intervals
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Merge Intervals
- Meeting Rooms II

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for start, end in sorted(intervals):
    if no overlap: append
    else: extend current end
```

## Pattern: Insert Interval

### Intuition

Copy intervals before the new range, merge overlaps with the new range, then copy the rest.

### When To Use It

Use when inserting one interval into sorted disjoint intervals.

### When Not To Use It

Do not resort everything if existing order can be reused.

### Recognition Signals

- insert interval
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Meeting Rooms II
- The Skyline Problem

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
add intervals ending before new starts
merge overlaps
append remaining intervals
```

## Pattern: Meeting Rooms

### Intuition

Track active intervals by end time to know how many resources are needed.

### When To Use It

Use for room counts, servers, and concurrent bookings.

### When Not To Use It

Do not merge intervals when each overlap needs a separate resource.

### Recognition Signals

- meeting rooms
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- The Skyline Problem
- Merge Intervals

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sort by start
heap stores end times
reuse room if earliest end <= start
```

## Pattern: Sweep Line

### Intuition

Convert starts and ends into events, sort them, and scan active count or state.

### When To Use It

Use for skyline, car pooling, active intervals, and range coverage.

### When Not To Use It

Do not ignore event ordering when coordinates tie.

### Recognition Signals

- sweep line
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Merge Intervals
- Meeting Rooms II

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
events = [(start, +1), (end, -1)]
scan sorted events
```

## Pattern: Interval Scheduling

### Intuition

Choose compatible intervals by a boundary that leaves maximum room for the future.

### When To Use It

Use for maximizing count or minimizing removals.

### When Not To Use It

Do not use it for weighted intervals without DP.

### Recognition Signals

- interval scheduling
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Meeting Rooms II
- The Skyline Problem

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sort by end
if interval.start >= last_end:
    take interval
```

## Pattern: Range Query with Heap

### Intuition

Sort queries and intervals, add intervals that can cover the query, and pop expired ones.

### When To Use It

Use when each point asks for the best covering interval.

### When Not To Use It

Do not scan all intervals per query.

### Recognition Signals

- range query with heap
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- The Skyline Problem
- Merge Intervals

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for q in sorted_queries:
    add intervals with start <= q
    remove intervals with end < q
    answer from heap top
```
---

## Navigation

[Previous](../intervals/CHEATSHEET.md) | [Home](../README.md) | [Next](../intervals/easy.md)
