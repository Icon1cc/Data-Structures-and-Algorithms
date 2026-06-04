# Sliding Window Cheatsheet

Fast revision notes for sliding window before interviews.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Fixed window | O(n) |
| Variable window | O(n) when each pointer moves forward |
| Window with balanced tree | O(n log k) |
| Deque maximum | O(n) |

## Formulas And Invariants

- Define the invariant before writing loops or recursion.
- Track exactly what state means at each step.
- Prefer deterministic boundary rules over intuition.
- Re-check empty input, one item, duplicate values, and maximum-size constraints.

## Pattern Summary

| Pattern | Use When |
|---|---|
| Fixed Size Window | Use for average, sum, max vowels, and fixed-length substrings. |
| Variable Size Window | Use for longest or shortest contiguous ranges under a constraint. |
| At Most K | Use when the phrase says at most k or can be transformed to exactly k. |
| Exactly K via At Most | Use for subarray count problems with distinct elements or odds. |
| Minimum Valid Window | Use for covering characters, words, or required frequencies. |
| Monotonic Deque Window | Use for sliding maximum or minimum. |

## Common Templates

### Fixed Size Window

```text
for right, x in enumerate(nums):
    add x
    if right >= k: remove nums[right-k]
    if right >= k-1: record
```

### Variable Size Window

```text
left = 0
for right in range(n):
    add right
    while invalid(): remove left; left += 1
    record
```

### At Most K

```text
while distinct > k:
    remove nums[left]
    left += 1
```

## Recognition Hints

Look for contiguous subarray, substring, longest, shortest, fixed length k, at most k, exactly k, or streaming range wording.

## Common Traps

- Using sliding window with negative sums when monotonicity is required.
- Not removing left-side state when shrinking.
- Confusing at most k with exactly k.

## Interview Reminders

- Say the brute force solution first.
- Explain why the optimized pattern removes repeated work.
- Test at least one normal case, one edge case, and one failure case.
- Include auxiliary space in the final complexity.


---

## Navigation

[Previous](../sliding-window/README.md) | [Home](../README.md) | [Next](../sliding-window/PATTERNS.md)
