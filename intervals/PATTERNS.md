# Intervals Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Merge Intervals | merge | Do not compare every pair after sorting |
| Insert Interval | insert | Do not sort again if one linear pass is enough |
| Sweep Line | events | Do not use when simple merging is enough |
| Meeting Rooms | rooms | Do not allocate a new room before checking the earliest end |
| Difference Array | range update | Do not allocate by huge raw coordinate ranges |
| Greedy Erase Overlap | remove overlap | Do not keep the longer interval just because it starts earlier |

## Pattern: Merge Intervals

### Beginner Intuition

Sort by start and absorb every interval that overlaps the current one.

### When To Use It

Use for union of ranges.

### When Not To Use It

Do not compare every pair after sorting.

### Recognition Signals

- merge
- overlap
- ranges

### Example Problems

- Merge Intervals

### Common Mistakes

- Updating `current.end = interval.end` on an overlap; this loses the larger end when intervals nest. Use `max(current.end, interval.end)`.
- Forgetting to append the final `current` after the loop ends; the last merged interval gets lost.
- Sorting by both start and end and assuming overlap detection is automatic; only sort by start, then check overlap explicitly.

### Pseudocode Or Template

```text
sort intervals by start
current = first
for interval in rest:
    if interval.start <= current.end: current.end = max(current.end, interval.end)
    else: output current; current = interval
```

### Complexity Notes

O(n log n) time, O(n) output.

### Interview Explanation

Sorting makes overlaps adjacent.

## Pattern: Insert Interval

### Beginner Intuition

Add intervals before, merge overlaps with the new interval, then append the rest.

### When To Use It

Use when existing intervals are sorted and non-overlapping.

### When Not To Use It

Do not sort again if one linear pass is enough.

### Recognition Signals

- insert
- sorted non-overlap
- new interval

### Example Problems

- Insert Interval

### Common Mistakes

- Sorting the input again; the input is already sorted, so re-sort wastes O(n log n) and may move equal-start intervals.
- Stopping after the first overlap; multiple existing intervals may overlap with the new one.
- Forgetting the after-tail; intervals strictly after the merged block must still be appended.

### Pseudocode Or Template

```text
append intervals ending before new starts
merge while overlap
append remaining intervals
```

### Complexity Notes

O(n) time, O(n) output.

### Interview Explanation

The sorted invariant lets the input split into before, overlapping, and after.

## Pattern: Sweep Line

### Beginner Intuition

Turn starts and ends into events and scan active count.

### When To Use It

Use for meeting rooms, calendars, and maximum overlap.

### When Not To Use It

Do not use when simple merging is enough.

### Recognition Signals

- events
- active count
- timeline

### Example Problems

- Meeting Rooms II
- My Calendar III

### Common Mistakes

- Tie-breaking starts before ends at the same timestamp; for half-open intervals, ends should be processed before starts so a meeting ending at 10 frees a room for a meeting starting at 10.
- Storing events as `(time, +1)` and `(time, -1)` without a deterministic tie-breaker; sorted output is non-deterministic on ties.
- Mixing inclusive and exclusive endpoint conventions across events; pick one convention and apply it everywhere.

### Pseudocode Or Template

```text
events = [(start, +1), (end, -1)]
for time, delta in sorted(events): active += delta
```

### Complexity Notes

O(n log n) time, O(n) space.

### Interview Explanation

The active count changes only at endpoints.

## Pattern: Meeting Rooms

### Beginner Intuition

Track the earliest ending active meeting to know if a room is freed.

### When To Use It

Use for minimum rooms and resource reuse.

### When Not To Use It

Do not allocate a new room before checking the earliest end.

### Recognition Signals

- rooms
- earliest end
- min heap

### Example Problems

- Meeting Rooms II

### Common Mistakes

- Allocating a new room without first checking if the earliest-ending meeting has ended; you over-count rooms.
- Using a max-heap of end times; a min-heap is needed to expose the earliest free room.
- Comparing the heap top against the new start with `<` versus `<=`; choose based on whether touching meetings share a room.

### Pseudocode Or Template

```text
sort meetings by start
heap = end times
if heap[0] <= start: pop
push end
```

### Complexity Notes

O(n log n) time.

### Interview Explanation

The earliest ending room is the only one that can free first.

## Pattern: Difference Array

### Beginner Intuition

Add range deltas and prefix them to recover active counts.

### When To Use It

Use when coordinates are bounded or compressed.

### When Not To Use It

Do not allocate by huge raw coordinate ranges.

### Recognition Signals

- range update
- difference
- bookings

### Example Problems

- Car Pooling
- Corporate Flight Bookings

### Common Mistakes

- Forgetting `diff[end] -= value` at the exclusive end; the active count never drops back down.
- For inclusive ends, decrementing at `end + 1` instead of `end`; off-by-one is the most common bug.
- Skipping coordinate compression for sparse domains; allocating a huge array wastes memory.

### Pseudocode Or Template

```text
diff[start] += value
diff[end] -= value
running += diff[i]
```

### Complexity Notes

O(n + range) or O(n log n) with coordinate compression.

### Interview Explanation

Range updates become two endpoint changes.

## Pattern: Greedy Erase Overlap

### Beginner Intuition

Keep the interval with the earliest end when overlaps conflict.

### When To Use It

Use to remove the fewest intervals or shoot minimum arrows.

### When Not To Use It

Do not keep the longer interval just because it starts earlier.

### Recognition Signals

- remove overlap
- earliest end
- arrows

### Example Problems

- Non-overlapping Intervals
- Minimum Number of Arrows to Burst Balloons

### Common Mistakes

- Sorting by start and keeping the first overlap; activity selection is "earliest finish", not "earliest start".
- For arrows, comparing `start > last_end` versus `start >= last_end`; whether touching balloons share an arrow is problem-specific.
- Updating `last_end` to the new interval's end when keeping; once kept, `last_end` should not regress.

### Pseudocode Or Template

```text
sort by end
count = 0
last_end = -inf
for interval in intervals:
    if interval.start >= last_end: keep and update
```

### Complexity Notes

O(n log n) time.

### Interview Explanation

Earliest end leaves the most room for future intervals.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
