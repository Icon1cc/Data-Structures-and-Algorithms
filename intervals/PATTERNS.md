# Intervals Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

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

- Forgetting to append the final active interval.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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

- Missing intervals after the merged block.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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

- Ordering start and end events incorrectly at the same time.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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

- Comparing against the latest end instead of earliest end.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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

- Forgetting to subtract at the exclusive end.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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

- Updating end to max instead of min on an overlap conflict.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

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
