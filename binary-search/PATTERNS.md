# Binary Search Patterns

Patterns are the bridge between theory and interview execution. Read these before solving the curated problems.
## Pattern: Classic Target Search

### Intuition

Compare the middle element with a target and discard half.

### When To Use It

Use for sorted arrays and exact lookup.

### When Not To Use It

Do not use when data is not sorted or monotonic.

### Recognition Signals

- sorted
- target
- lookup

### Problem Examples

- Binary Search
- Search Insert Position

### Common Mistakes

- Off-by-one bounds
- Overflow in mid in fixed-width languages

### Reusable Template Or Pseudocode

```text
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
```

## Pattern: Lower Bound

### Intuition

Find the first position where a predicate is true.

### When To Use It

Use for insertion point and first occurrence.

### When Not To Use It

Do not use when any matching index is enough and simpler search is clearer.

### Recognition Signals

- first
- at least
- leftmost
- insert

### Problem Examples

- First Bad Version
- Find First and Last Position

### Common Mistakes

- Returning hi after exclusive bounds confusion
- Skipping equality handling

### Reusable Template Or Pseudocode

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid
    else: lo = mid + 1
```

## Pattern: Upper Bound

### Intuition

Find the first position greater than a value or the last true boundary.

### When To Use It

Use for counts, ranges, and rightmost occurrence.

### When Not To Use It

Do not use without defining inclusive or exclusive semantics.

### Recognition Signals

- rightmost
- greater than
- last valid

### Problem Examples

- Find First and Last Position
- H-Index II

### Common Mistakes

- Mixing first greater with first greater-or-equal
- Returning one past the answer unintentionally

### Reusable Template Or Pseudocode

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] <= target: lo = mid + 1
    else: hi = mid
```

## Pattern: Search Rotated Array

### Intuition

Use the sorted half of a rotated array to decide which side to discard.

### When To Use It

Use when an originally sorted array has one rotation pivot.

### When Not To Use It

Do not use unchanged when duplicates destroy the ability to identify the sorted side.

### Recognition Signals

- rotated
- pivot
- sorted half

### Problem Examples

- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

### Common Mistakes

- Wrong equality behavior with duplicates
- Searching both halves unnecessarily

### Reusable Template Or Pseudocode

```text
if nums[lo] <= nums[mid]: left half is sorted
else: right half is sorted
```

## Pattern: Binary Search on Answer

### Intuition

Search a numeric answer range with a feasibility check.

### When To Use It

Use for capacity, speed, maximum minimum distance, and allocation.

### When Not To Use It

Do not use when feasibility is not monotonic.

### Recognition Signals

- minimum feasible
- capacity
- speed
- maximize minimum

### Problem Examples

- Koko Eating Bananas
- Capacity To Ship Packages Within D Days

### Common Mistakes

- Predicate not monotonic
- Wrong low and high answer bounds

### Reusable Template Or Pseudocode

```text
lo, hi = min_answer, max_answer
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
```

## Pattern: Matrix Search

### Intuition

Treat matrix order as either flattened sorted data or row-column monotonic data.

### When To Use It

Use for sorted matrices.

### When Not To Use It

Do not use the flattened approach unless rows globally continue into the next row.

### Recognition Signals

- sorted matrix
- row and column sorted

### Problem Examples

- Search a 2D Matrix
- Search a 2D Matrix II

### Common Mistakes

- Assuming global order when only rows and columns are sorted
- Index conversion errors

### Reusable Template Or Pseudocode

```text
r, c = 0, cols - 1
while r < rows and c >= 0:
    compare matrix[r][c]
```

---

## Navigation

[Previous](../binary-search/CHEATSHEET.md) | [Home](../README.md) | [Next](../binary-search/easy.md)
