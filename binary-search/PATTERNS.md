# Binary Search Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Classic Target Search | sorted | Do not use when the input is unsorted or the predicate is not monotonic |
| Lower Bound | first true | Do not use without defining what true means at each index |
| Upper Bound | rightmost | Do not mix greater-than with greater-or-equal semantics |
| Rotated Sorted Search | rotated | Do not use unchanged when duplicates make both halves ambiguous |
| Binary Search On Answer | minimum feasible | Do not use if feasibility can switch back and forth |
| Matrix Binary Search | sorted matrix | Do not flatten when rows and columns are sorted independently but not globally |
| Peak Search | peak | Do not use for arbitrary unsorted target lookup |

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

- Computing `mid = (lo + hi) // 2` in languages where `lo + hi` can overflow; use `lo + (hi - lo) // 2` instead.
- Mixing inclusive `[lo, hi]` and exclusive `[lo, hi)` templates in the same function; pick one and stick to it.
- Returning `mid` immediately on equality but never updating bounds, causing an infinite loop on a missing target.

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

- Using `lo <= hi` with `[lo, n]` exclusive; the half-open template needs `lo < hi` to terminate.
- Forgetting that the answer can be `n` (no valid index) when every position is false; return `lo` and let the caller interpret it.
- Updating `lo = mid` instead of `lo = mid + 1` when the predicate is false, which produces an infinite loop.

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

- Returning `lo` when the caller wanted the last index where the value matches; subtract 1 to convert upper-bound to last-equal.
- Using `<=` versus `<` carelessly in the predicate; `<=` makes upper-bound, `<` makes lower-bound.
- Counting `upper_bound(x) - lower_bound(x)` and forgetting that it equals the multiplicity of `x` only on a sorted array.

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

- Comparing `nums[mid]` against `nums[lo]` instead of `nums[hi]`; the latter is more robust for pivot detection because the right end keeps the rotation invariant clean.
- Failing to handle the no-rotation case (`nums[0] < nums[-1]`) before entering the loop; the algorithm still works but a fast path is cleaner.
- Ignoring duplicates: with duplicates, `nums[mid] == nums[hi]` is ambiguous; shrinking `hi` by 1 is the standard fallback.

### Pseudocode Or Template

```text
if nums[lo] <= nums[mid]:
    left side is sorted
else:
    right side is sorted
```

### Complexity Notes

O(log n) without duplicate ambiguity, O(n) worst case with duplicates.

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

- Setting `lo = 1` when the lower bound should be `max(weights)` (the largest single item must fit); the search returns infeasible candidates.
- Using `lo = mid` instead of `lo = mid + 1` after a false `feasible` check, looping forever on plateaus.
- Confirming feasibility direction by guessing; explicitly write down "feasible(mid) implies feasible(mid + 1)" before coding.

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

- Treating LC 240 (row and column sorted but not globally) like LC 74 (globally sorted); flat binary search fails on LC 240.
- Computing `(r, c) = divmod(mid, rows)` instead of `divmod(mid, cols)`; the column count is the divisor.
- Falling back to nested binary search per row when stair-step search from the top-right corner is O(m + n).

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

- Reaching for `nums[mid - 1]` and `nums[mid + 1]` without bounds; comparing `nums[mid]` and `nums[mid + 1]` is enough and avoids the left edge.
- Forgetting that `nums[-1] = nums[n] = -inf` is the existence guarantee; without it, no peak need exist.
- Using equal-value tie-breaking; the algorithm assumes strict inequality between adjacent values.

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
