# Intervals Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

An interval represents a continuous range [start, end] or [start, end). Algorithms depend on whether touching endpoints overlap.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Sort intervals | O(n log n) |
| Merge after sort | O(n) scan |
| Sweep line | O(n log n) |
| Difference array with bounded coordinates | O(n + range) |

## Space Table

| Case | Complexity |
|---|---:|
| In-place merge | O(1) extra if output ignored |
| Output merged intervals | O(n) |
| Event list | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Merge Intervals | Use for union of ranges. |
| Insert Interval | Use when existing intervals are sorted and non-overlapping. |
| Sweep Line | Use for meeting rooms, calendars, and maximum overlap. |
| Meeting Rooms | Use for minimum rooms and resource reuse. |
| Difference Array | Use when coordinates are bounded or compressed. |
| Greedy Erase Overlap | Use to remove the fewest intervals or shoot minimum arrows. |

## Recognition Hints

Look for merge, insert, overlap, meeting rooms, minimum removals, arrows, calendar, booking, timeline, or active count.

## Templates

### Merge Intervals

```text
sort intervals by start
current = first
for interval in rest:
    if interval.start <= current.end: current.end = max(current.end, interval.end)
    else: output current; current = interval
```

### Insert Interval

```text
append intervals ending before new starts
merge while overlap
append remaining intervals
```

### Sweep Line

```text
events = [(start, +1), (end, -1)]
for time, delta in sorted(events): active += delta
```

### Meeting Rooms

```text
sort meetings by start
heap = end times
if heap[0] <= start: pop
push end
```

## Common Traps

- Forgetting to sort before merging.
- Mixing closed and half-open endpoint rules.
- Updating the wrong endpoint after overlap.
- Using pairwise comparisons after sorting would give a linear scan.

## Interview Reminders

- Say the brute force approach first in one or two sentences.
- State the invariant before coding.
- Test one normal case, one smallest case, and one adversarial case.
- Include auxiliary space, not only input and output size.
- Mention when the pattern assumptions would fail.

## Final Checklist

- [ ] I can define the topic in plain language.
- [ ] I can identify at least three recognition signals.
- [ ] I can write the main template from memory.
- [ ] I can explain time and space complexity.
- [ ] I can name two common mistakes and how to avoid them.

---

## Navigation

[Previous](README.md) | [Home](../README.md) | [Next](PATTERNS.md)
