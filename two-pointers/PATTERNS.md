# Two Pointers Patterns

Patterns are the bridge between theory and interview execution. Read these before solving the curated problems.
## Pattern: Opposite Ends

### Intuition

Use left and right boundaries that move inward.

### When To Use It

Use for palindromes, sorted pair sums, and area problems.

### When Not To Use It

Do not use when valid candidates are not ordered by either end.

### Recognition Signals

- palindrome
- both ends
- sorted pair
- container

### Problem Examples

- Valid Palindrome
- Container With Most Water

### Common Mistakes

- Moving the wrong limiting side
- Skipping duplicate handling

### Reusable Template Or Pseudocode

```text
left, right = 0, len(a) - 1
while left < right:
    # inspect a[left], a[right]
    left += 1 or right -= 1
```

## Pattern: Fast and Slow

### Intuition

Move two pointers at different speeds to reveal structure.

### When To Use It

Use for cycles, middle nodes, and nth-from-end gaps.

### When Not To Use It

Do not use when random access indices are simpler and available.

### Recognition Signals

- cycle
- middle
- nth from end

### Problem Examples

- Linked List Cycle
- Middle of the Linked List

### Common Mistakes

- Dereferencing null fast.next
- Starting phase two incorrectly

### Reusable Template Or Pseudocode

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Pattern: Sorted Pair Search

### Intuition

Sort, then move pointers based on whether the current sum is too small or large.

### When To Use It

Use for 2Sum variants, 3Sum, 4Sum, and triangle checks.

### When Not To Use It

Do not use when original indices must be preserved unless you store them.

### Recognition Signals

- pair sum
- triplets
- sorted array

### Problem Examples

- 3Sum
- Two Sum II

### Common Mistakes

- Not skipping duplicates
- Returning sorted positions instead of original indices

### Reusable Template Or Pseudocode

```text
nums.sort()
left, right = i + 1, len(nums) - 1
while left < right:
    s = nums[i] + nums[left] + nums[right]
```

## Pattern: Merge Pointers

### Intuition

Advance through multiple sorted sources in order.

### When To Use It

Use for merging arrays, intervals, lists, or streams.

### When Not To Use It

Do not use when data is unsorted and no ordering invariant exists.

### Recognition Signals

- merge sorted
- two sorted lists
- intersection

### Problem Examples

- Merge Sorted Array
- Interval List Intersections

### Common Mistakes

- Dropping tail elements
- Incorrect tie handling

### Reusable Template Or Pseudocode

```text
while i < len(a) and j < len(b):
    take smaller next item
```

## Pattern: Partition Pointers

### Intuition

Maintain regions for values already classified.

### When To Use It

Use for Dutch national flag, remove element, and compaction.

### When Not To Use It

Do not use when stable ordering is required and swaps break it.

### Recognition Signals

- partition
- sort colors
- remove in place

### Problem Examples

- Sort Colors
- Remove Element

### Common Mistakes

- Advancing after swap before inspecting new value
- Breaking stable order requirements

### Reusable Template Or Pseudocode

```text
low = mid = 0; high = len(nums) - 1
while mid <= high:
    classify nums[mid]
```

## Pattern: Cycle Detection

### Intuition

Detect loops by comparing a fast pointer and a slow pointer.

### When To Use It

Use for linked-list cycles and functional graphs.

### When Not To Use It

Do not use when graph nodes have many outgoing edges without adaptation.

### Recognition Signals

- cycle
- repeated state
- functional graph

### Problem Examples

- Linked List Cycle II
- Find the Duplicate Number

### Common Mistakes

- Stopping too early
- Not resetting one pointer to head for entry detection

### Reusable Template Or Pseudocode

```text
slow = f(x); fast = f(f(x))
while slow != fast:
    slow = f(slow); fast = f(f(fast))
```

---

## Navigation

[Previous](../two-pointers/CHEATSHEET.md) | [Home](../README.md) | [Next](../two-pointers/easy.md)
