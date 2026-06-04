# Sliding Window Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A sliding window keeps two monotonic boundaries and an aggregate over the interval between them. Each boundary moves at most n times.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Standard window | O(n) |
| Window with hash counts | O(n) expected |
| Monotonic deque window | O(n) amortized |
| Bad nested rescan | O(nk) or O(n^2) |

## Space Table

| Case | Complexity |
|---|---:|
| Numeric window | O(1) |
| Frequency map | O(k) distinct values |
| Deque | O(k) window size |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Fixed Window | Use for fixed length averages, sums, and counts. |
| Variable Window | Use for longest or shortest contiguous segments under a condition. |
| Frequency Window | Use for permutations, anagrams, replacement, and at-most-k distinct problems. |
| At Most K Window | Use when exactly k is hard but at most k is monotonic. |
| Monotonic Window | Use for sliding maximum, minimum, and bounded absolute difference. |

## Recognition Hints

Look for contiguous subarray, substring, longest, shortest, at most k, exactly k via at most transforms, fixed length k, or stream-style language.

## Pattern Choice Checklist

- Fixed window records after the first full length k window exists.
- Longest valid window shrinks while invalid, then records.
- Shortest valid window shrinks while valid, recording before removal.
- Exactly k counts often become at_most(k) minus at_most(k - 1).

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run zero-count keys, negative values, recording order, and k larger than input before submitting.

## Templates

### Fixed Window

```text
window = 0
for right, x in enumerate(nums):
    window += x
    if right >= k: window -= nums[right - k]
    if right >= k - 1: update_answer(window)
```

### Variable Window

```text
left = 0
for right in range(n):
    add(right)
    while invalid():
        remove(left)
        left += 1
    record()
```

### Frequency Window

```text
counts[x] += 1
while too_many():
    counts[left_value] -= 1
    left += 1
```

### At Most K Window

```text
def at_most(k):
    left = answer = 0
    for right in range(n):
        add(right)
        while invalid(k): shrink()
        answer += right - left + 1
```

## Common Traps

- Recording the answer before restoring validity.
- Using a window when prefix sums are required for negative numbers.
- Forgetting to remove zero-count keys.
- Confusing exactly k with at most k.

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
