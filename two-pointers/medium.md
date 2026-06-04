# Two Pointers Medium Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Medium order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Two Sum II - Input Array Is Sorted

LeetCode: [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Difficulty: Medium

Pattern: Opposite Direction Pointers

Why It Matters: The clearest sorted pair-search pattern.

Skills Tested:
- Recognize that sorted input plus a target sum is the textbook converging-pointers signal.
- State the invariant: every pair outside `[left, right]` either sums above `target` (right too far) or below (left too far), so the answer lies inside.
- Move `left` up when the sum is too small and `right` down when too large, never both at once.
- Achieve O(n) time, O(1) space, and contrast with the unsorted Two Sum which requires O(n) extra space for a hash map.

Common Follow-Ups:
- 3Sum (LC 15) and 4Sum (LC 18) reduce k-sum to repeated pair-search.
- Two Sum Less Than K (LC 1099) replaces equality with a less-than predicate.
- What if duplicates are allowed and you must report all pairs (skip duplicates after each match).

## 2. 3Sum

LeetCode: [3Sum](https://leetcode.com/problems/3sum/)

Difficulty: Medium

Pattern: Sort Plus Two Pointers

Why It Matters: Tests duplicate skipping and reducing 3-way search to pair search.

Skills Tested:
- Recognize that fixing one element and running two pointers on the rest converts a 3-way search into n independent pair searches.
- State the invariant: after sorting, identical neighbors must be skipped at every level so duplicate triples never enter the result.
- Handle the early-break when `nums[i] > 0` (no positive triple can sum to zero) and skip-duplicates after every successful match.
- Time O(n^2), space O(1) extra (ignoring output), and explain why hash-based 3Sum can hit worst-case O(n^2) memory.

Common Follow-Ups:
- 3Sum Closest (LC 16) replaces equality with a min-distance objective.
- 3Sum Smaller (LC 259) counts triples below a threshold.
- 4Sum (LC 18) extends with one more outer loop and requires careful duplicate handling at every level.

## 3. Container With Most Water

LeetCode: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Difficulty: Medium

Pattern: Opposite Direction Greedy Pointers

Why It Matters: Forces a proof for moving the shorter wall.

Skills Tested:
- Recognize that area is `min(height[left], height[right]) * (right - left)` and the only safe direction is to move the shorter wall.
- State the invariant: every pair where the shorter wall sits at one of the discarded indices has area no larger than the current candidate, so dropping that side never loses an optimal answer.
- Argue why moving the taller wall is provably non-optimal (width shrinks and the height ceiling does not rise).
- Time O(n), space O(1), and contrast with brute force O(n^2) over all pairs.

Common Follow-Ups:
- Trapping Rain Water (LC 42) layers prefix-max reasoning on the same converging-pointer skeleton.
- Largest Rectangle in Histogram (LC 84) trades two pointers for a monotonic stack.
- What if the array is streamed - can the answer be maintained online (no, the proof requires global knowledge).

## 4. Sort Colors

LeetCode: [Sort Colors](https://leetcode.com/problems/sort-colors/)

Difficulty: Medium

Pattern: Dutch National Flag Partition

Why It Matters: Classic Dutch national flag pointer regions.

Skills Tested:
- Recognize that three values 0, 1, 2 partition the array into three contiguous regions, which is the Dutch flag set up.
- State the invariant: `nums[0..low)` is all 0, `nums[low..mid)` is all 1, `nums[high..n)` is all 2, and `nums[mid..high]` is unprocessed.
- Move pointers correctly: swap-with-low advances both low and mid, swap-with-high only decrements high (the pulled-in value still needs to be inspected).
- Achieve O(n) time, O(1) space, and contrast with counting sort which costs an extra pass.

Common Follow-Ups:
- Wiggle Sort (LC 280, 324) reuses partition reasoning for a different layout.
- What if there are k buckets instead of 3 (multi-way partition).
- How would you make the algorithm stable.

## 5. Next Permutation

LeetCode: [Next Permutation](https://leetcode.com/problems/next-permutation/)

Difficulty: Medium

Pattern: Suffix Scan And Reverse

Why It Matters: Tests in-place sequence manipulation from the right.

Skills Tested:
- Recognize that the next lexicographic permutation needs the rightmost ascending pair `nums[i] < nums[i+1]`, then a swap with the smallest right value larger than `nums[i]`, then reversing the suffix.
- State the invariant: after the swap, the suffix is non-increasing, so reversing it makes it the smallest possible continuation.
- Handle the wrap-around case where the array is fully descending (return its reverse, the smallest permutation).
- Time O(n), space O(1) - explain why generating all permutations is factorial and unacceptable.

Common Follow-Ups:
- Permutation Sequence (LC 60) jumps directly to the k-th permutation using factorials.
- Previous Permutation With One Swap (LC 1053) swaps the predicate direction.
- How would you support next-permutation queries online over a long stream of arrays.

## 6. Find the Duplicate Number

LeetCode: [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

Difficulty: Medium

Pattern: Floyd Cycle Detection

Why It Matters: Models array values as linked pointers for cycle detection.

Skills Tested:
- Recognize that values in `[1, n]` over an array of length `n + 1` define a function `i -> nums[i]` whose cycle entry is the duplicate.
- State the invariant: a tortoise-and-hare phase detects a meeting inside the cycle, then a second walk from start and meeting point lands at the cycle entry.
- Handle the constraint "do not modify input" and "use only O(1) extra space" - both forbid hash sets and sorting.
- Time O(n), space O(1), and contrast with binary search on value (O(n log n) but read-only friendly).

Common Follow-Ups:
- Linked List Cycle II (LC 142) is the same algorithm on an actual linked list.
- Find All Duplicates in an Array (LC 442) returns every duplicate, requires in-place index marking.
- What if multiple duplicates exist with arbitrary multiplicities.

## 7. 4Sum

LeetCode: [4Sum](https://leetcode.com/problems/4sum/)

Difficulty: Medium

Pattern: Sorted K-Sum Pointers

Why It Matters: Extends duplicate-safe two-pointer reasoning.

Skills Tested:
- Recognize that 4Sum is two nested loops fixing two values, then two pointers on the remaining suffix.
- State the invariant: at every level, identical neighbors must be skipped to avoid duplicate quadruples in the result.
- Use early-exit pruning when the smallest possible sum at this level exceeds the target or the largest is below it.
- Time O(n^3), space O(1) extra (ignoring output), and generalize to k-sum with the same recursion.

Common Follow-Ups:
- 4Sum II (LC 454) takes four arrays and uses meet-in-the-middle hashing for O(n^2).
- k-Sum generalization with recursion that bottoms out at the two-pointer base case.
- How would you support online 4Sum queries (offline batching plus sorted maps).

## 8. String Compression

LeetCode: [String Compression](https://leetcode.com/problems/string-compression/)

Difficulty: Medium

Pattern: Read Write Pointers

Why It Matters: Practices grouped writes and length expansion in place.

Skills Tested:
- Recognize that "compress runs in place" is a read pointer that scans equal runs and a write pointer that emits the character followed by the count digits.
- State the invariant: `chars[0..write]` holds the compressed prefix corresponding to the runs already consumed by `read`.
- Handle single-character runs (no count emitted), counts with multiple digits (write each digit), and an empty input.
- Achieve O(n) time, O(1) extra space, and explain why a counter-then-rebuild approach uses O(n) extra.

Common Follow-Ups:
- Decode String (LC 394) inverts the process and pulls in stack-based decoding.
- What if the output must fit in a fixed buffer smaller than the input - early-exit and report.
- Compress runs only when the count is at least `k`, otherwise leave the run unchanged.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
