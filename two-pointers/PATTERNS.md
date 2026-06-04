# Two Pointers Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Opposite Direction Pointers | sorted | Do not use if moving one side cannot be justified by an ordering rule |
| Same Direction Pointers | read write | Do not use when relative order does not matter and partitioning is simpler |
| Fast And Slow Pointers | cycle | Do not use if the structure has no linked movement or next relation |
| Partitioning | three regions | Do not use if stable ordering is required and the swaps would break it |
| Merge From End | merge sorted | Do not use when output order or memory layout does not protect unread values |

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

- Moving the taller wall in Container With Most Water; the height ceiling cannot rise, so the area can only shrink.
- Forgetting to skip duplicates in 3Sum-style problems after each successful match, causing duplicate triples in the result.
- Using `<` versus `<=` carelessly in the loop guard; for converging pair search, `left < right` is correct, while equality would compare a value with itself.

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

- Incrementing `write` before assigning, which leaves a stale value at the new write index.
- Comparing against `nums[read]` instead of `nums[write - 1]` for sorted-deduplication; the kept boundary lives behind `write`, not at `read`.
- Returning the array length instead of the count of kept elements; problem statements often want the new logical length.

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

- Stopping cycle detection at `fast.next` without also guarding `fast.next.next`, which crashes on null in odd-length lists.
- Returning the meeting point as the cycle entrance; the meeting point lies somewhere inside the cycle, and a second walk from head plus meeting locates the entrance.
- Using fast/slow on Find the Duplicate Number when the array contains value 0; the algorithm requires values in `[1, n]` for the index-mapping trick.

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

- Advancing `mid` after swapping with the high region; the value pulled from high has not been inspected yet and may belong to the low region.
- Confusing the four region invariants (less, equal, unprocessed, greater); write each boundary's meaning down before coding.
- Picking partitioning when stable order matters; partitioning swaps freely and breaks the relative order within regions.

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

- Stopping the loop on `i >= 0` only; if `j` outlasts `i`, the remaining `nums2` values must still be copied.
- Writing from the front, which destroys `nums1[i]` before it has been compared.
- Squaring values in place before merging; the negative-then-positive ordering disappears, breaking the sorted-merge assumption.

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
