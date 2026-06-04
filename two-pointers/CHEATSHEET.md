# Two Pointers Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Two-pointer algorithms maintain one or more indices whose movement is monotonic. Because each pointer advances a bounded number of times, the scan is usually linear.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Linear pointer scan | O(n) |
| Sorted pair search | O(n) after sort |
| Sort plus pointers | O(n log n) |
| Nested pointer reset | Usually O(n^2), avoid unless intended |

## Space Table

| Case | Complexity |
|---|---:|
| In-place pointer scan | O(1) |
| Output list | O(result size) |
| Sort copy | O(n) if input cannot be mutated |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Opposite Direction Pointers | Use for sorted pair search, palindromes, and container-style bounds. |
| Same Direction Pointers | Use for remove duplicates, move zeroes, and stable filtering. |
| Fast And Slow Pointers | Use for middle node, cycle detection, nth from end, and duplicate-as-cycle tricks. |
| Partitioning | Use for sort colors, quickselect partitions, and Dutch national flag problems. |
| Merge From End | Use when one array has extra capacity at the end. |

## Recognition Hints

Look for sorted input, palindromes, pairs, triplets, in-place removal, merging, cycle detection, or language that says use constant extra space.

## Templates

### Opposite Direction Pointers

```text
left, right = 0, len(nums) - 1
while left < right:
    decide using nums[left], nums[right]
```

### Same Direction Pointers

```text
write = 0
for read, value in enumerate(nums):
    if keep(value):
        nums[write] = value
        write += 1
```

### Fast And Slow Pointers

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Partitioning

```text
low = mid = 0
high = len(nums) - 1
while mid <= high:
    partition nums[mid]
```

## Common Traps

- Moving both pointers without proving it is safe.
- Skipping duplicate handling in 3Sum-style problems.
- Resetting a pointer in a way that restores O(n^2).
- Forgetting that sorting changes original indices.

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
