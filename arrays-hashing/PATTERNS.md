# Arrays & Hashing Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Frequency Counting | duplicates | Do not use counts alone when positions or ordering are the answer |
| Hash Lookup | seen before | Do not use when sorted two pointers gives O(1) space and original order is irrelevant |
| Prefix Sum | subarray sum | Do not use a simple sliding window when numbers can be negative and the sum is not monotonic |
| Bucket Counting | top k | Do not allocate buckets for a huge sparse domain |
| Sorting Plus Hashing | canonical key | Do not sort if original indices must be returned and cannot be preserved |
| Grouping by Canonical Key | group | Do not use a lossy signature that maps different items together |
| In-place Index Marking | constant space | Do not mutate input if the caller needs it unchanged |

## Pattern: Frequency Counting

### Beginner Intuition

Count occurrences so equality, duplicates, and anagram checks become direct comparisons.

### When To Use It

Use when multiplicity matters, not only existence.

### When Not To Use It

Do not use counts alone when positions or ordering are the answer.

### Recognition Signals

- duplicates
- anagram
- majority
- counts

### Example Problems

- Valid Anagram
- Ransom Note
- Majority Element

### Common Mistakes

- Forgetting to decrement counts or remove zero-count keys.
- Ignoring the exclusion case for Frequency Counting: Do not use counts alone when positions or ordering are the answer.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
for x in values:
    freq[x] = freq.get(x, 0) + 1
```

### Complexity Notes

O(n) time and O(k) space for k distinct keys.

### Interview Explanation

I use a frequency map because the repeated work is asking how many of each value exists.

## Pattern: Hash Lookup

### Beginner Intuition

Store what has been seen so the current value can find a complement or prior state immediately.

### When To Use It

Use for pair sums, membership, first occurrence, and deduplication.

### When Not To Use It

Do not use when sorted two pointers gives O(1) space and original order is irrelevant.

### Recognition Signals

- seen before
- complement
- contains
- first index

### Example Problems

- Two Sum
- Contains Duplicate
- Insert Delete GetRandom O(1)

### Common Mistakes

- Checking after insertion when the value could match itself.
- Ignoring the exclusion case for Hash Lookup: Do not use when sorted two pointers gives O(1) space and original order is irrelevant.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

### Complexity Notes

O(n) expected time, O(n) space.

### Interview Explanation

I trade extra memory for constant-time lookup and preserve the invariant that seen contains only earlier items.

## Pattern: Prefix Sum

### Beginner Intuition

Turn every range sum into the difference between two cumulative sums.

### When To Use It

Use for subarray sums, ranges, balance counts, and exactly-k totals.

### When Not To Use It

Do not use a simple sliding window when numbers can be negative and the sum is not monotonic.

### Recognition Signals

- subarray sum
- range sum
- exactly k
- balance

### Example Problems

- Subarray Sum Equals K
- Product of Array Except Self
- Count of Range Sum

### Common Mistakes

- Forgetting the initial prefix value 0.
- Ignoring the exclusion case for Prefix Sum: Do not use a simple sliding window when numbers can be negative and the sum is not monotonic.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
prefix = 0
count = {0: 1}
for x in nums:
    prefix += x
    answer += count.get(prefix - k, 0)
    count[prefix] = count.get(prefix, 0) + 1
```

### Complexity Notes

O(n) expected time, O(n) space.

### Interview Explanation

I define prefix before index i as the sum to the left, so any target subarray is found by a previous prefix.

## Pattern: Bucket Counting

### Beginner Intuition

Use frequency or bounded values as array indices instead of sorting everything.

### When To Use It

Use when counts are bounded by n or the value domain is small.

### When Not To Use It

Do not allocate buckets for a huge sparse domain.

### Recognition Signals

- top k
- bounded range
- frequency bucket

### Example Problems

- Top K Frequent Elements
- Sort Characters By Frequency

### Common Mistakes

- Creating buckets for values instead of frequencies when frequencies are what need ordering.
- Ignoring the exclusion case for Bucket Counting: Do not allocate buckets for a huge sparse domain.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
buckets = [[] for _ in range(len(nums) + 1)]
for value, freq in counts.items():
    buckets[freq].append(value)
```

### Complexity Notes

O(n) time and O(n) space when bucket count is proportional to input.

### Interview Explanation

I avoid full sorting because frequencies are bounded by n, so buckets give direct frequency order.

## Pattern: Sorting Plus Hashing

### Beginner Intuition

Sort to expose order, then use hashing for grouped or quick membership decisions.

### When To Use It

Use when both canonical ordering and lookup are helpful.

### When Not To Use It

Do not sort if original indices must be returned and cannot be preserved.

### Recognition Signals

- canonical key
- sorted signature
- grouped records

### Example Problems

- Group Anagrams
- Longest Consecutive Sequence

### Common Mistakes

- Forgetting that sorting each long string adds L log L cost.
- Ignoring the exclusion case for Sorting Plus Hashing: Do not sort if original indices must be returned and cannot be preserved.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
key = tuple(sorted(word))
groups.setdefault(key, []).append(word)
```

### Complexity Notes

Usually O(n log n) for sorting, or O(total_chars log alphabet) for strings.

### Interview Explanation

I make equivalent values share a canonical key, then group by that key.

## Pattern: Grouping by Canonical Key

### Beginner Intuition

Convert each item into a stable signature so equivalent items land together.

### When To Use It

Use for anagrams, isomorphism, normalized coordinates, and pattern strings.

### When Not To Use It

Do not use a lossy signature that maps different items together.

### Recognition Signals

- group
- equivalent
- normalized
- signature

### Example Problems

- Group Anagrams
- Isomorphic Strings
- Valid Sudoku

### Common Mistakes

- Using a mutable list as a key.
- Ignoring the exclusion case for Grouping by Canonical Key: Do not use a lossy signature that maps different items together.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
signature = tuple(counts)
groups.setdefault(signature, []).append(item)
```

### Complexity Notes

O(n * key_cost) time and O(n) space.

### Interview Explanation

I explain what makes two items equivalent, then encode exactly that property in the key.

## Pattern: In-place Index Marking

### Beginner Intuition

Use values as pointers into the same array when the input range is 1..n.

### When To Use It

Use for missing positive or disappeared number questions with strict space limits.

### When Not To Use It

Do not mutate input if the caller needs it unchanged.

### Recognition Signals

- constant space
- values 1..n
- missing number

### Example Problems

- First Missing Positive
- Find All Numbers Disappeared in an Array

### Common Mistakes

- Mixing value and index by forgetting the minus one conversion.
- Ignoring the exclusion case for In-place Index Marking: Do not mutate input if the caller needs it unchanged.
- Failing to test duplicates, empty input, negative values, missing keys, and key overwrite order against the stated invariant.

### Pseudocode Or Template

```text
for x in nums:
    i = abs(x) - 1
    if 0 <= i < len(nums):
        nums[i] = -abs(nums[i])
```

### Complexity Notes

O(n) time and O(1) auxiliary space.

### Interview Explanation

I use the array as a visited table because each valid value maps to exactly one index.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
