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
- Identify the Opposite Direction Pointers signal before choosing a template.
- State the invariant for Valid Palindrome: builds pointer movement and character skipping without extra memory.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Valid Palindrome toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Opposite Direction Pointers invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Merge Sorted Array

LeetCode: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

Difficulty: Easy

Pattern: Merge From End

Why It Matters: Tests in-place merging while protecting unread values.

Skills Tested:
- Identify the Merge From End signal before choosing a template.
- State the invariant for Merge Sorted Array: tests in-place merging while protecting unread values.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Merge Sorted Array toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Merge From End invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Remove Duplicates from Sorted Array

LeetCode: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Difficulty: Easy

Pattern: Same Direction Pointers

Why It Matters: Introduces read/write invariants on sorted data.

Skills Tested:
- Identify the Same Direction Pointers signal before choosing a template.
- State the invariant for Remove Duplicates from Sorted Array: introduces read/write invariants on sorted data.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Remove Duplicates from Sorted Array toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Same Direction Pointers invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Move Zeroes

LeetCode: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

Difficulty: Easy

Pattern: Stable Compaction

Why It Matters: Practices separating kept values from filler values.

Skills Tested:
- Identify the Stable Compaction signal before choosing a template.
- State the invariant for Move Zeroes: practices separating kept values from filler values.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Move Zeroes toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Stable Compaction invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Squares of a Sorted Array

LeetCode: [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Difficulty: Easy

Pattern: Opposite Ends Merge

Why It Matters: Uses sorted absolute values to fill output from the back.

Skills Tested:
- Identify the Opposite Ends Merge signal before choosing a template.
- State the invariant for Squares of a Sorted Array: uses sorted absolute values to fill output from the back.
- Handle off-by-one bounds, duplicates, sortedness assumptions, and in-place mutation.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Squares of a Sorted Array toward hash lookup, binary search, sliding window, sorting, or prefix state?
- Which off-by-one bounds case would break the first implementation?
- Can the Opposite Ends Merge invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
