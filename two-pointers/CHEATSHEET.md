# Two Pointers Cheatsheet

Fast revision notes for two pointers before interviews.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Single pass | O(n) |
| Merge two sorted arrays | O(n + m) |
| Sort plus two pointers | O(n log n) |
| Nested pointer reset | Often O(n^2), avoid unless intended |

## Formulas And Invariants

- Define the invariant before writing loops or recursion.
- Track exactly what state means at each step.
- Prefer deterministic boundary rules over intuition.
- Re-check empty input, one item, duplicate values, and maximum-size constraints.

## Pattern Summary

| Pattern | Use When |
|---|---|
| Opposite Ends | Use for palindromes, sorted pair sums, and area problems. |
| Fast and Slow | Use for cycles, middle nodes, and nth-from-end gaps. |
| Sorted Pair Search | Use for 2Sum variants, 3Sum, 4Sum, and triangle checks. |
| Merge Pointers | Use for merging arrays, intervals, lists, or streams. |
| Partition Pointers | Use for Dutch national flag, remove element, and compaction. |
| Cycle Detection | Use for linked-list cycles and functional graphs. |

## Common Templates

### Opposite Ends

```text
left, right = 0, len(a) - 1
while left < right:
    # inspect a[left], a[right]
    left += 1 or right -= 1
```

### Fast and Slow

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Sorted Pair Search

```text
nums.sort()
left, right = i + 1, len(nums) - 1
while left < right:
    s = nums[i] + nums[left] + nums[right]
```

## Recognition Hints

Look for sorted inputs, palindromes, pair sums, removing duplicates, linked-list cycle checks, or a need to compare both ends.

## Common Traps

- Moving both pointers when only one side is justified.
- Using two pointers before sorting when order is required.
- Forgetting duplicate handling after finding a valid pair.

## Interview Reminders

- Say the brute force solution first.
- Explain why the optimized pattern removes repeated work.
- Test at least one normal case, one edge case, and one failure case.
- Include auxiliary space in the final complexity.


---

## Navigation

[Previous](../two-pointers/README.md) | [Home](../README.md) | [Next](../two-pointers/PATTERNS.md)
