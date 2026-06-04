# Binary Search Cheatsheet

Fast revision notes for binary search before interviews.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Search array | O(log n) |
| Binary search over answer | O(log R * check) |
| Matrix binary search | O(log(mn)) |
| Rotated array search | O(log n) when duplicates do not break order |

## Formulas And Invariants

- Define the invariant before writing loops or recursion.
- Track exactly what state means at each step.
- Prefer deterministic boundary rules over intuition.
- Re-check empty input, one item, duplicate values, and maximum-size constraints.

## Pattern Summary

| Pattern | Use When |
|---|---|
| Classic Target Search | Use for sorted arrays and exact lookup. |
| Lower Bound | Use for insertion point and first occurrence. |
| Upper Bound | Use for counts, ranges, and rightmost occurrence. |
| Search Rotated Array | Use when an originally sorted array has one rotation pivot. |
| Binary Search on Answer | Use for capacity, speed, maximum minimum distance, and allocation. |
| Matrix Search | Use for sorted matrices. |

## Common Templates

### Classic Target Search

```text
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
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

## Recognition Hints

Look for sorted data, minimum feasible capacity, maximum allowed value, first bad version, peak, rotation, or any phrase like smallest possible maximum.

## Common Traps

- Infinite loops from unchanged boundaries.
- Returning mid instead of the boundary.
- Using binary search without a monotonic predicate.

## Interview Reminders

- Say the brute force solution first.
- Explain why the optimized pattern removes repeated work.
- Test at least one normal case, one edge case, and one failure case.
- Include auxiliary space in the final complexity.


---

## Navigation

[Previous](../binary-search/README.md) | [Home](../README.md) | [Next](../binary-search/PATTERNS.md)
