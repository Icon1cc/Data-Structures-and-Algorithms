# Binary Search Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Binary search repeatedly narrows a monotonic range while preserving an invariant that the answer remains inside the current bounds.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Array search | O(log n) |
| Answer search | O(log R * check_cost) |
| Matrix flattened search | O(log(mn)) |
| Rotated search without duplicate ambiguity | O(log n) |

## Space Table

| Case | Complexity |
|---|---:|
| Iterative | O(1) |
| Recursive | O(log n) call stack |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Classic Target Search | Use when the input is sorted and any matching index is enough. |
| Lower Bound | Use for first occurrence, insertion point, and minimum feasible answer. |
| Upper Bound | Use for range counts and right boundary queries. |
| Rotated Sorted Search | Use when a sorted array has one rotation pivot. |
| Binary Search On Answer | Use for minimum capacity, speed, maximum minimum distance, and allocation. |
| Matrix Binary Search | Use when each row continues after the previous row or row-column order supports stair-step search. |
| Peak Search | Use for local maximum and mountain-array style problems. |

## Recognition Hints

Look for sorted data, first or last valid value, minimum feasible capacity, maximum allowed minimum, rotated arrays, peaks, or the phrase smallest possible maximum.

## Pattern Choice Checklist

- Classic search needs sorted data and exact equality handling.
- Lower bound returns the first index satisfying a predicate.
- Answer search costs O(log R * check_cost).
- Rotated search needs proof of which half is ordered.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries before submitting.

## Templates

### Classic Target Search

```text
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    compare nums[mid] with target
```

### Lower Bound

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid
    else: lo = mid + 1
```

### Upper Bound

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] <= target: lo = mid + 1
    else: hi = mid
```

### Rotated Sorted Search

```text
if nums[lo] <= nums[mid]:
    left side is sorted
else:
    right side is sorted
```

## Common Traps

- Using binary search without a monotonic predicate.
- Changing neither bound on equality.
- Returning mid instead of the converged boundary.
- Choosing low and high bounds that exclude the real answer.

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
