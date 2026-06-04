# Two Pointers Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Valid Palindrome

LeetCode: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Difficulty: Easy

Pattern: Opposite Direction Pointers

Why It Matters: Builds pointer movement and character skipping without extra memory.

Skills Tested:
- Recognize that "is the cleaned string the same backwards" only needs one left pointer and one right pointer converging, never extra memory.
- State the invariant: at every step, every character outside `[left, right]` already matched its mirror, and any mismatch between `s[left]` and `s[right]` proves false.
- Skip non-alphanumeric characters carefully so neither pointer moves past the other inside the loop.
- Handle empty strings, single characters, and case-insensitive comparison without rebuilding the string.

Common Follow-Ups:
- Valid Palindrome II (LC 680) allows one deletion and forks into two checks at the first mismatch.
- Valid Palindrome IV (LC 2330) and Palindromic Substrings (LC 647) extend the same converging-pointer idea.
- What changes when the input is a singly linked list rather than a string?

## 2. Merge Sorted Array

LeetCode: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

Difficulty: Easy

Pattern: Merge From End

Why It Matters: Tests in-place merging while protecting unread values.

Skills Tested:
- Recognize that merging into `nums1` from the front would overwrite unread values, so the safe direction is from the back where space is free.
- State the invariant: the suffix of `nums1` from `write` onward is sorted and final, while the prefixes still hold unprocessed values.
- Handle `m == 0` (copy `nums2`), `n == 0` (no-op), and trailing leftover from `nums2` after `nums1` is exhausted.
- Achieve O(m + n) time, O(1) extra space, and explain why a naive copy-and-sort costs O((m + n) log (m + n)).

Common Follow-Ups:
- Merge K Sorted Lists (LC 23) generalizes to a heap of head pointers.
- Merge Intervals (LC 56) reuses the merge-from-front idea with overlap reasoning.
- How would you parallelize a merge of very large external sorted runs?

## 3. Remove Duplicates from Sorted Array

LeetCode: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Difficulty: Easy

Pattern: Same Direction Pointers

Why It Matters: Introduces read/write invariants on sorted data.

Skills Tested:
- Recognize that "remove duplicates in place from sorted input" is a write pointer trailing a read pointer that copies only when the value changes.
- State the invariant: the prefix `nums[0..write]` is the deduplicated result, while `read` scans the rest in order.
- Handle empty arrays (return 0), single elements (return 1), and arrays where every value is identical.
- Achieve O(n) time, O(1) extra space, and explain why this pattern fails on unsorted input.

Common Follow-Ups:
- Remove Duplicates from Sorted Array II (LC 80) keeps at most two copies, requiring a comparison against `nums[write - 2]`.
- Remove Element (LC 27) replaces the equality check with a value filter.
- How would you adapt the pattern to a singly linked list (Remove Duplicates from Sorted List, LC 83).

## 4. Move Zeroes

LeetCode: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

Difficulty: Easy

Pattern: Stable Compaction

Why It Matters: Practices separating kept values from filler values.

Skills Tested:
- Recognize that "shift all non-zero values forward, preserve order" is a stable partition with a write pointer that lags the read pointer.
- State the invariant: `nums[0..write]` holds every non-zero value seen so far in original order, and `nums[write..read]` is filler that becomes zero at the end.
- Decide between a two-pass (compact then zero-fill) and a single-pass (swap when read is non-zero) variant, naming the trade-off.
- Handle all-zero arrays, all-non-zero arrays, and arrays of length one without special cases.

Common Follow-Ups:
- Remove Element (LC 27) uses the same stable compaction with an arbitrary value filter.
- Sort Colors (LC 75) generalizes to three regions instead of two.
- What changes if the relative order of zero values must also be preserved (no longer a partition).

## 5. Squares of a Sorted Array

LeetCode: [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Difficulty: Easy

Pattern: Opposite Ends Merge

Why It Matters: Uses sorted absolute values to fill output from the back.

Skills Tested:
- Recognize that the largest square lies at one end of a sorted array, so two pointers from both ends pick the bigger square each step.
- State the invariant: at each step, the larger of `nums[left] ** 2` and `nums[right] ** 2` is placed at the next available rightmost slot of the output.
- Handle all-negative arrays, all-non-negative arrays, and arrays containing zero.
- Achieve O(n) time and O(n) output space, and explain why a naive square-then-sort is O(n log n).

Common Follow-Ups:
- Sort Transformed Array (LC 360) extends to `a*x*x + b*x + c` and forks based on the sign of `a`.
- What if the output had to be in place and the input could be modified.
- How would you handle very large numbers where squaring overflows 64-bit (use big integers or shift to floats with care).

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
