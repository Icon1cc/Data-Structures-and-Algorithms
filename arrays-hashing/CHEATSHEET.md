# Arrays & Hashing Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

An array is an indexed sequence with O(1) random access. A hash table maps keys to values with expected O(1) insert, lookup, and delete through hashing and collision handling.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Index access | O(1) |
| Full scan | O(n) |
| Hash lookup average | O(1) |
| Hash lookup worst case | O(n) |
| Sort then scan | O(n log n) |

## Space Table

| Case | Complexity |
|---|---:|
| In-place scan | O(1) |
| Hash set or map | O(k) distinct keys |
| Prefix array | O(n) |
| Bucket array | O(n) when indexed by frequency |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Frequency Counting | Use when multiplicity matters, not only existence. |
| Hash Lookup | Use for pair sums, membership, first occurrence, and deduplication. |
| Prefix Sum | Use for subarray sums, ranges, balance counts, and exactly-k totals. |
| Bucket Counting | Use when counts are bounded by n or the value domain is small. |
| Sorting Plus Hashing | Use when both canonical ordering and lookup are helpful. |
| Grouping by Canonical Key | Use for anagrams, isomorphism, normalized coordinates, and pattern strings. |
| In-place Index Marking | Use for missing positive or disappeared number questions with strict space limits. |

## Recognition Hints

Look for duplicates, pairs, anagrams, grouping, subarray sums, longest consecutive runs, first occurrence, or a brute force loop that repeatedly asks whether a previous value exists.

## Pattern Choice Checklist

- If the question asks for earlier information, try seen-set or map lookup first.
- If it asks for exact subarray totals with negatives, use prefix sums rather than a window.
- If values or frequencies are bounded, compare bucket counting against sorting.
- If strings need grouping, define a canonical key that preserves equivalence.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run duplicates, empty input, negative values, missing keys, and key overwrite order before submitting.

## Templates

### Frequency Counting

```text
for x in values:
    freq[x] = freq.get(x, 0) + 1
```

### Hash Lookup

```text
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

### Prefix Sum

```text
prefix = 0
count = {0: 1}
for x in nums:
    prefix += x
    answer += count.get(prefix - k, 0)
    count[prefix] = count.get(prefix, 0) + 1
```

### Bucket Counting

```text
buckets = [[] for _ in range(len(nums) + 1)]
for value, freq in counts.items():
    buckets[freq].append(value)
```

## Common Traps

- Using a list membership scan when a set is required.
- Overwriting first-index information too early.
- Forgetting prefix zero for subarray counts.
- Ignoring negative values when choosing sliding window instead of prefix sums.

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
