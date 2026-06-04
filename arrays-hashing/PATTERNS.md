# Arrays & Hashing Patterns

Patterns are the bridge between theory and interview execution. Read these before solving the curated problems.
## Pattern: Frequency Counting

### Intuition

Count how often each value appears so later decisions are direct lookups.

### When To Use It

Use when the question asks about duplicates, anagrams, majority, or exact occurrence counts.

### When Not To Use It

Do not use when order-sensitive positions are the main signal and counts lose needed detail.

### Recognition Signals

- duplicates
- frequency
- anagram
- majority

### Problem Examples

- Valid Anagram
- Top K Frequent Elements

### Common Mistakes

- Forgetting to decrement counts
- Comparing maps before all updates are applied

### Reusable Template Or Pseudocode

```text
for value in values:
    count[value] += 1
```

## Pattern: Hash Lookup

### Intuition

Store values already seen so a future value can find its complement or matching state.

### When To Use It

Use for pair sums, seen states, membership, and first occurrence lookup.

### When Not To Use It

Do not use when sorted order gives a simpler two-pointer solution with less memory.

### Recognition Signals

- target pair
- contains
- seen before
- complement

### Problem Examples

- Two Sum
- Contains Duplicate

### Common Mistakes

- Storing after lookup when current value can match itself
- Overwriting first index

### Reusable Template Or Pseudocode

```text
for i, x in enumerate(nums):
    need = target - x
    if need in seen: return [seen[need], i]
    seen[x] = i
```

## Pattern: Prefix Sum

### Intuition

Convert range sums into differences between cumulative values.

### When To Use It

Use for subarray sum, range query, and balance problems.

### When Not To Use It

Do not use alone when the operation is not invertible, such as range minimum.

### Recognition Signals

- subarray sum
- range sum
- exactly k
- balance

### Problem Examples

- Subarray Sum Equals K
- Range Sum Query Immutable

### Common Mistakes

- Off-by-one prefix length
- Not counting prefix zero

### Reusable Template Or Pseudocode

```text
prefix = 0
seen = {0: 1}
for x in nums:
    prefix += x
    answer += seen[prefix - target]
    seen[prefix] += 1
```

## Pattern: Grouping by Canonical Key

### Intuition

Normalize equivalent values to the same key, then group originals.

### When To Use It

Use for anagrams, equivalent strings, signatures, and normalized coordinates.

### When Not To Use It

Do not use when normalization is more expensive than direct comparison for tiny inputs.

### Recognition Signals

- group
- same pattern
- anagram
- equivalent

### Problem Examples

- Group Anagrams
- Valid Sudoku

### Common Mistakes

- Using mutable objects as keys
- Choosing a key that collides for non-equivalent data

### Reusable Template Or Pseudocode

```text
key = tuple(sorted(word))
groups[key].append(word)
```

## Pattern: Bucket Counting

### Intuition

Use value ranges or frequencies as direct bucket indexes.

### When To Use It

Use when counts are bounded or top-k can avoid full sorting.

### When Not To Use It

Do not use when the value domain is enormous and sparse unless buckets are compressed.

### Recognition Signals

- bounded values
- frequency buckets
- top k

### Problem Examples

- Top K Frequent Elements
- Sort Characters By Frequency

### Common Mistakes

- Allocating buckets for huge domains
- Forgetting ties

### Reusable Template Or Pseudocode

```text
buckets = [[] for _ in range(len(nums) + 1)]
for value, freq in count.items():
    buckets[freq].append(value)
```

## Pattern: In-place Marking

### Intuition

Use the input array as a visited marker when values map to indices.

### When To Use It

Use when values are in the range 1..n and extra space is restricted.

### When Not To Use It

Do not use when the input must remain unchanged.

### Recognition Signals

- constant space
- values 1 to n
- missing positive

### Problem Examples

- First Missing Positive
- Find All Numbers Disappeared in an Array

### Common Mistakes

- Index conversion errors
- Destroying values needed later

### Reusable Template Or Pseudocode

```text
for x in nums:
    i = abs(x) - 1
    if 0 <= i < len(nums): nums[i] = -abs(nums[i])
```

---

## Navigation

[Previous](../arrays-hashing/CHEATSHEET.md) | [Home](../README.md) | [Next](../arrays-hashing/easy.md)
