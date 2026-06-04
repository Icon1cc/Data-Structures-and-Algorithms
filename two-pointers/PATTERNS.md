# Two Pointers Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: Opposite Direction Pointers

### Beginner Intuition

Start at both ends and discard one side based on a monotonic comparison.

### When To Use It

Use for sorted pair search, palindromes, and container-style bounds.

### When Not To Use It

Do not use if moving one side cannot be justified by an ordering rule.

### Recognition Signals

- sorted
- pair
- palindrome
- ends

### Example Problems

- Valid Palindrome
- Two Sum II
- Container With Most Water

### Common Mistakes

- Moving the pointer with the larger value in container problems.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
left, right = 0, len(nums) - 1
while left < right:
    decide using nums[left], nums[right]
```

### Complexity Notes

O(n) time and O(1) space.

### Interview Explanation

I can discard one endpoint because no candidate using it can beat the remaining search space.

## Pattern: Same Direction Pointers

### Beginner Intuition

Use a read pointer to scan and a write pointer to compact or build a valid prefix.

### When To Use It

Use for remove duplicates, move zeroes, and stable filtering.

### When Not To Use It

Do not use when relative order does not matter and partitioning is simpler.

### Recognition Signals

- read write
- compact
- remove in place

### Example Problems

- Remove Duplicates from Sorted Array
- Move Zeroes

### Common Mistakes

- Incrementing write before the assignment is complete.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
write = 0
for read, value in enumerate(nums):
    if keep(value):
        nums[write] = value
        write += 1
```

### Complexity Notes

O(n) time and O(1) extra space.

### Interview Explanation

I maintain that everything before write is already valid.

## Pattern: Fast And Slow Pointers

### Beginner Intuition

Move pointers at different speeds to encode distance or detect cycles.

### When To Use It

Use for middle node, cycle detection, nth from end, and duplicate-as-cycle tricks.

### When Not To Use It

Do not use if the structure has no linked movement or next relation.

### Recognition Signals

- cycle
- middle
- nth from end
- tortoise hare

### Example Problems

- Linked List Cycle
- Find the Duplicate Number

### Common Mistakes

- Failing to separate cycle detection from locating the cycle entrance.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Complexity Notes

O(n) time and O(1) space.

### Interview Explanation

The faster pointer creates a provable distance relationship without extra storage.

## Pattern: Partitioning

### Beginner Intuition

Maintain regions such as less than, equal to, and greater than while scanning.

### When To Use It

Use for sort colors, quickselect partitions, and Dutch national flag problems.

### When Not To Use It

Do not use if stable ordering is required and the swaps would break it.

### Recognition Signals

- three regions
- colors
- pivot
- in place

### Example Problems

- Sort Colors
- Partition List

### Common Mistakes

- Advancing the current pointer after swapping with an unknown region.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
low = mid = 0
high = len(nums) - 1
while mid <= high:
    partition nums[mid]
```

### Complexity Notes

O(n) time and O(1) space.

### Interview Explanation

I define the meaning of each region before coding so pointer moves are mechanical.

## Pattern: Merge From End

### Beginner Intuition

Fill the output from the back to avoid overwriting unread values.

### When To Use It

Use when one array has extra capacity at the end.

### When Not To Use It

Do not use when output order or memory layout does not protect unread values.

### Recognition Signals

- merge sorted
- extra space at end
- overwrite risk

### Example Problems

- Merge Sorted Array
- Squares of a Sorted Array

### Common Mistakes

- Writing from the front and destroying needed values.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
i, j, w = m - 1, n - 1, m + n - 1
while j >= 0:
    place larger value at w
```

### Complexity Notes

O(n + m) time and O(1) extra space.

### Interview Explanation

I fill from the back because the largest remaining value belongs at the last open slot.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
