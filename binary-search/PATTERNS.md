# Binary Search Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern: Classic Target Search

### Beginner Intuition

Find an exact target in sorted data by comparing with the middle.

### When To Use It

Use when the input is sorted and any matching index is enough.

### When Not To Use It

Do not use when the input is unsorted or the predicate is not monotonic.

### Recognition Signals

- sorted
- exact target
- lookup

### Example Problems

- Binary Search
- Search Insert Position

### Common Mistakes

- Changing the wrong boundary after equality.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    compare nums[mid] with target
```

### Complexity Notes

O(log n) time, O(1) space.

### Interview Explanation

The target, if present, always remains between lo and hi.

## Pattern: Lower Bound

### Beginner Intuition

Find the first index where a condition becomes true.

### When To Use It

Use for first occurrence, insertion point, and minimum feasible answer.

### When Not To Use It

Do not use without defining what true means at each index.

### Recognition Signals

- first true
- leftmost
- at least
- insert

### Example Problems

- First Bad Version
- Search Insert Position

### Common Mistakes

- Returning hi in one template and lo in another without knowing why.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid
    else: lo = mid + 1
```

### Complexity Notes

O(log n) predicate calls.

### Interview Explanation

False values are left of the answer and true values start at the answer.

## Pattern: Upper Bound

### Beginner Intuition

Find the first index greater than a value or one past the rightmost valid position.

### When To Use It

Use for range counts and right boundary queries.

### When Not To Use It

Do not mix greater-than with greater-or-equal semantics.

### Recognition Signals

- rightmost
- first greater
- count range

### Example Problems

- Find First and Last Position of Element in Sorted Array
- Time Based Key-Value Store

### Common Mistakes

- Returning the first invalid index when the caller expects the last valid index.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] <= target: lo = mid + 1
    else: hi = mid
```

### Complexity Notes

O(log n) time, O(1) space.

### Interview Explanation

I return the boundary, then subtract one only if the problem asks for the last valid index.

## Pattern: Rotated Sorted Search

### Beginner Intuition

Use the sorted half of a rotated array to discard impossible candidates.

### When To Use It

Use when a sorted array has one rotation pivot.

### When Not To Use It

Do not use unchanged when duplicates make both halves ambiguous.

### Recognition Signals

- rotated
- pivot
- sorted half

### Example Problems

- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

### Common Mistakes

- Testing the target against the unsorted half.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
if nums[lo] <= nums[mid]:
    left side is sorted
else:
    right side is sorted
```

### Complexity Notes

O(log n) without duplicate ambiguity.

### Interview Explanation

At least one half is sorted, so I use that half to decide whether the target can be there.

## Pattern: Binary Search On Answer

### Beginner Intuition

Search the numeric answer range using a feasibility check.

### When To Use It

Use for minimum capacity, speed, maximum minimum distance, and allocation.

### When Not To Use It

Do not use if feasibility can switch back and forth.

### Recognition Signals

- minimum feasible
- capacity
- speed
- maximize minimum

### Example Problems

- Koko Eating Bananas
- Split Array Largest Sum

### Common Mistakes

- Picking low and high bounds that exclude the answer.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
lo, hi = min_answer, max_answer
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
```

### Complexity Notes

O(log range * cost(check)).

### Interview Explanation

The check answers whether this candidate is enough, so the first enough value is the optimum.

## Pattern: Matrix Binary Search

### Beginner Intuition

Map a matrix position to a one-dimensional sorted order when the matrix is globally sorted.

### When To Use It

Use when each row continues after the previous row or row-column order supports stair-step search.

### When Not To Use It

Do not flatten when rows and columns are sorted independently but not globally.

### Recognition Signals

- sorted matrix
- row column sorted
- flattened

### Example Problems

- Search a 2D Matrix
- Search a 2D Matrix II

### Common Mistakes

- Using the wrong row and column conversion.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
mid = (lo + hi) // 2
r, c = divmod(mid, cols)
```

### Complexity Notes

O(log(mn)) for global order, O(m + n) for stair-step.

### Interview Explanation

I first identify which sorted-matrix promise the problem actually gives.

## Pattern: Peak Search

### Beginner Intuition

Use slope direction to keep a side that must contain a peak.

### When To Use It

Use for local maximum and mountain-array style problems.

### When Not To Use It

Do not use for arbitrary unsorted target lookup.

### Recognition Signals

- peak
- mountain
- local maximum
- slope

### Example Problems

- Find Peak Element
- Peak Index in a Mountain Array

### Common Mistakes

- Comparing to both neighbors when one slope comparison is sufficient.
- Applying the pattern after one keyword match without checking the invariant.
- Ignoring empty input, duplicate values, and boundary cases.

### Pseudocode Or Template

```text
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] < nums[mid + 1]: lo = mid + 1
    else: hi = mid
```

### Complexity Notes

O(log n) time, O(1) space.

### Interview Explanation

If the slope rises to the right, a peak must exist on the right side.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
