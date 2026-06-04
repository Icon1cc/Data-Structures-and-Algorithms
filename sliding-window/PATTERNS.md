# Sliding Window Patterns

Patterns are the bridge between theory and interview execution. Read these before solving the curated problems.
## Pattern: Fixed Size Window

### Intuition

Maintain exactly k elements and update the answer after each step.

### When To Use It

Use for average, sum, max vowels, and fixed-length substrings.

### When Not To Use It

Do not use for variable constraints where shrinking length matters.

### Recognition Signals

- length k
- fixed window
- every k

### Problem Examples

- Maximum Average Subarray I
- Maximum Number of Vowels in a Substring

### Common Mistakes

- Removing the wrong outgoing element
- Recording before reaching k elements

### Reusable Template Or Pseudocode

```text
for right, x in enumerate(nums):
    add x
    if right >= k: remove nums[right-k]
    if right >= k-1: record
```

## Pattern: Variable Size Window

### Intuition

Expand until invalid, then shrink until valid again.

### When To Use It

Use for longest or shortest contiguous ranges under a constraint.

### When Not To Use It

Do not use if values can move the constraint non-monotonically in both directions.

### Recognition Signals

- longest substring
- minimum length
- while invalid

### Problem Examples

- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum

### Common Mistakes

- Shrinking too little
- Forgetting to update answer at the right time

### Reusable Template Or Pseudocode

```text
left = 0
for right in range(n):
    add right
    while invalid(): remove left; left += 1
    record
```

## Pattern: At Most K

### Intuition

Keep a window with no more than k distinct or invalid items.

### When To Use It

Use when the phrase says at most k or can be transformed to exactly k.

### When Not To Use It

Do not use when k is not monotonic with window expansion.

### Recognition Signals

- at most k
- distinct
- replace k

### Problem Examples

- Fruit Into Baskets
- Max Consecutive Ones III

### Common Mistakes

- Not deleting zero counts
- Confusing replacements with distinct count

### Reusable Template Or Pseudocode

```text
while distinct > k:
    remove nums[left]
    left += 1
```

## Pattern: Exactly K via At Most

### Intuition

Count exactly k by subtracting counts of at most k and at most k-1.

### When To Use It

Use for subarray count problems with distinct elements or odds.

### When Not To Use It

Do not use for min or max length objectives directly.

### Recognition Signals

- exactly k
- count subarrays
- distinct

### Problem Examples

- Subarrays with K Different Integers
- Count Number of Nice Subarrays

### Common Mistakes

- Trying to maintain exactly k directly and missing counts
- Not handling k = 0

### Reusable Template Or Pseudocode

```text
exactly(k) = at_most(k) - at_most(k - 1)
```

## Pattern: Minimum Valid Window

### Intuition

Shrink a valid window as much as possible while preserving required counts.

### When To Use It

Use for covering characters, words, or required frequencies.

### When Not To Use It

Do not use when the target is not contiguous.

### Recognition Signals

- minimum window
- contains all
- cover

### Problem Examples

- Minimum Window Substring
- Minimum Window Subsequence

### Common Mistakes

- Counting unique satisfied keys incorrectly
- Dropping required duplicates

### Reusable Template Or Pseudocode

```text
expand right
while window covers target:
    record
    remove left
```

## Pattern: Monotonic Deque Window

### Intuition

Keep candidate indices in a deque ordered by value and inside the window.

### When To Use It

Use for sliding maximum or minimum.

### When Not To Use It

Do not use when the query is not an extremum.

### Recognition Signals

- sliding maximum
- window max
- deque

### Problem Examples

- Sliding Window Maximum
- Constrained Subsequence Sum

### Common Mistakes

- Leaving expired indices
- Storing values instead of indices when duplicates matter

### Reusable Template Or Pseudocode

```text
while deque and deque[0] <= right-k: popleft
while deque and nums[deque[-1]] <= nums[right]: pop
```

---

## Navigation

[Previous](../sliding-window/CHEATSHEET.md) | [Home](../README.md) | [Next](../sliding-window/easy.md)
