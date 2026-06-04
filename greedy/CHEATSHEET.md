# Greedy Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A greedy algorithm builds a solution step by step using a locally optimal rule. Correctness usually follows from an exchange argument, staying-ahead proof, or cut property.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Sort and scan | O(n log n) |
| Single pass greedy | O(n) |
| Heap-assisted greedy | O(n log n) |

## Space Table

| Case | Complexity |
|---|---:|
| In-place scan | O(1) |
| Sorted copy | O(n) |
| Heap support | O(n) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Sort And Scan | Use for intervals, cookies, arrows, and pairing. |
| Greedy With Proof | Use for all greedy problems. |
| Interval Greedy | Use for erase overlap, meeting selection, and arrows. |
| Jump Greedy | Use for reachability and minimum jumps. |
| Heap-Assisted Greedy | Use for scheduling, refueling, and selecting best active resource. |
| Monotonic Greedy | Use for lexicographically smallest subsequences and digit removal. |

## Recognition Hints

Look for earliest finish, minimum removals, maximum reach, choose once, local replacement, intervals, scheduling, or problems asking for fewest resources.

## Templates

### Sort And Scan

```text
items.sort(key=key)
for item in items:
    if safe(item): take item
```

### Greedy With Proof

```text
state greedy choice
show any optimal solution can swap to it
```

### Interval Greedy

```text
sort by end
last_end = -inf
for interval in intervals:
    if interval.start >= last_end: take it
```

### Jump Greedy

```text
end = farthest = jumps = 0
for i in range(n - 1):
    farthest = max(farthest, i + nums[i])
    if i == end: jumps += 1; end = farthest
```

## Common Traps

- Using greedy where future choices can invalidate local choice.
- Skipping the proof in interviews.
- Sorting by the wrong key.
- Confusing DP choose-or-skip with greedy safe choice.

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
