# Sliding Window Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: Fixed Window

### Beginner Intuition

Keep exactly k items and update the answer as the window slides one step.

### When To Use It

Use for fixed length averages, sums, and counts.

### When Not To Use It

Do not use if valid window length changes based on content.

### Recognition Signals

- length k
- fixed size
- average

### Example Problems

- Maximum Average Subarray I
- Contains Duplicate II

### Common Mistakes

- Updating answer before the first full window exists.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
window = 0
for right, x in enumerate(nums):
    window += x
    if right >= k: window -= nums[right - k]
    if right >= k - 1: update_answer(window)
```

### Complexity Notes

O(n) time, O(1) or O(k) space depending on state.

### Interview Explanation

The invariant is that the state describes the last k elements exactly.

## Pattern: Variable Window

### Beginner Intuition

Expand until useful, then shrink while the invariant allows or requires it.

### When To Use It

Use for longest or shortest contiguous segments under a condition.

### When Not To Use It

Do not use when removing left does not predictably improve validity.

### Recognition Signals

- longest
- shortest
- contiguous
- shrink

### Example Problems

- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters

### Common Mistakes

- Shrinking only once when the window may still be invalid.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
left = 0
for right in range(n):
    add(right)
    while invalid():
        remove(left)
        left += 1
    record()
```

### Complexity Notes

O(n) time because each side moves at most n times.

### Interview Explanation

I maintain a valid window before recording the best answer.

## Pattern: Frequency Window

### Beginner Intuition

Track character or value counts inside the current window.

### When To Use It

Use for permutations, anagrams, replacement, and at-most-k distinct problems.

### When Not To Use It

Do not leave zero-count keys that make distinct counts wrong.

### Recognition Signals

- counts
- anagram
- permutation
- distinct

### Example Problems

- Permutation in String
- Find All Anagrams in a String

### Common Mistakes

- Comparing full maps too often when a matched counter would be cleaner.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
counts[x] += 1
while too_many():
    counts[left_value] -= 1
    left += 1
```

### Complexity Notes

O(n) expected time, O(alphabet or k) space.

### Interview Explanation

The map is the window, so every move of a boundary updates the map.

## Pattern: At Most K Window

### Beginner Intuition

Count windows with at most k, then derive exactly k by subtraction.

### When To Use It

Use when exactly k is hard but at most k is monotonic.

### When Not To Use It

Do not use when at most k is not monotonic under shrinking.

### Recognition Signals

- at most k
- exactly k
- distinct count

### Example Problems

- Fruit Into Baskets
- Max Consecutive Ones III

### Common Mistakes

- Forgetting exactly(k) = at_most(k) - at_most(k - 1).
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
def at_most(k):
    left = answer = 0
    for right in range(n):
        add(right)
        while invalid(k): shrink()
        answer += right - left + 1
```

### Complexity Notes

O(n) for each at-most pass.

### Interview Explanation

I transform exactly into two monotonic counts because that is easier to maintain.

## Pattern: Monotonic Window

### Beginner Intuition

Use a deque to keep the best candidate in the current window.

### When To Use It

Use for sliding maximum, minimum, and bounded absolute difference.

### When Not To Use It

Do not use a heap unless stale deletion is handled.

### Recognition Signals

- max in window
- deque
- monotonic
- absolute diff

### Example Problems

- Sliding Window Maximum
- Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Common Mistakes

- Forgetting to evict indices that leave the window.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
while deque and nums[deque[-1]] <= x: deque.pop()
deque.append(right)
while deque[0] <= right - k: deque.popleft()
```

### Complexity Notes

O(n) amortized time, O(k) space.

### Interview Explanation

The deque stores only candidates that can still become the answer.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
