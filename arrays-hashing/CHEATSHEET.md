# Arrays & Hashing Cheatsheet

Fast revision notes for arrays and hashing before interviews.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Array index access | O(1) |
| Array scan | O(n) |
| Hash lookup average | O(1) |
| Hash lookup worst case | O(n) |
| Sorting before scan | O(n log n) |

## Formulas And Invariants

- Define the invariant before writing loops or recursion.
- Track exactly what state means at each step.
- Prefer deterministic boundary rules over intuition.
- Re-check empty input, one item, duplicate values, and maximum-size constraints.

## Pattern Summary

| Pattern | Use When |
|---|---|
| Frequency Counting | Use when the question asks about duplicates, anagrams, majority, or exact occurrence counts. |
| Hash Lookup | Use for pair sums, seen states, membership, and first occurrence lookup. |
| Prefix Sum | Use for subarray sum, range query, and balance problems. |
| Grouping by Canonical Key | Use for anagrams, equivalent strings, signatures, and normalized coordinates. |
| Bucket Counting | Use when counts are bounded or top-k can avoid full sorting. |
| In-place Marking | Use when values are in the range 1..n and extra space is restricted. |

## Common Templates

### Frequency Counting

```text
for value in values:
    count[value] += 1
```

### Hash Lookup

```text
for i, x in enumerate(nums):
    need = target - x
    if need in seen: return [seen[need], i]
    seen[x] = i
```

### Prefix Sum

```text
prefix = 0
seen = {0: 1}
for x in nums:
    prefix += x
    answer += seen[prefix - target]
    seen[prefix] += 1
```

## Recognition Hints

Look for duplicates, pairs with a target, anagrams, subarray sums, longest consecutive ranges, or repeated work caused by nested loops.

## Common Traps

- Forgetting that hash-table worst cases exist.
- Using a list membership scan where a set is intended.
- Losing first-index information by overwriting too early.

## Interview Reminders

- Say the brute force solution first.
- Explain why the optimized pattern removes repeated work.
- Test at least one normal case, one edge case, and one failure case.
- Include auxiliary space in the final complexity.


---

## Navigation

[Previous](../arrays-hashing/README.md) | [Home](../README.md) | [Next](../arrays-hashing/PATTERNS.md)
