# Arrays & Hashing Medium Problems

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

## 1. Group Anagrams

LeetCode: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Difficulty: Medium

Pattern: Grouping by Canonical Key

Why It Matters: Turns equivalence into a key and is a core hashmap grouping interview pattern.

Skills Tested:
- Identify the Grouping by Canonical Key signal before choosing a template.
- State the invariant for Group Anagrams: turns equivalence into a key and is a core hashmap grouping interview pattern.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Group Anagrams toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Grouping by Canonical Key invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Contiguous Array

LeetCode: [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

Difficulty: Medium

Pattern: Prefix Sum Balance

Why It Matters: Converts equal 0/1 counts into repeated prefix states and tests balance reasoning.

Skills Tested:
- Identify the Prefix Sum Balance signal before choosing a template.
- State the invariant for Contiguous Array: converts equal 0/1 counts into repeated prefix states and tests balance reasoning.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Contiguous Array toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Prefix Sum Balance invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Product of Array Except Self

LeetCode: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Difficulty: Medium

Pattern: Prefix And Suffix Products

Why It Matters: Forces left/right accumulated state and careful zero handling.

Skills Tested:
- Identify the Prefix And Suffix Products signal before choosing a template.
- State the invariant for Product of Array Except Self: forces left/right accumulated state and careful zero handling.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Product of Array Except Self toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Prefix And Suffix Products invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Encode and Decode Strings

LeetCode: [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

Difficulty: Medium

Pattern: Length Prefix Encoding

Why It Matters: Teaches delimiter-safe serialization and edge cases around empty strings.

Skills Tested:
- Identify the Length Prefix Encoding signal before choosing a template.
- State the invariant for Encode and Decode Strings: teaches delimiter-safe serialization and edge cases around empty strings.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Encode and Decode Strings toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Length Prefix Encoding invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Longest Consecutive Sequence

LeetCode: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

Difficulty: Medium

Pattern: Hash Set Boundary Scan

Why It Matters: Shows how to start work only at sequence boundaries to stay linear.

Skills Tested:
- Identify the Hash Set Boundary Scan signal before choosing a template.
- State the invariant for Longest Consecutive Sequence: shows how to start work only at sequence boundaries to stay linear.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Consecutive Sequence toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Hash Set Boundary Scan invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Subarray Sum Equals K

LeetCode: [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Difficulty: Medium

Pattern: Prefix Sum With Counts

Why It Matters: A high-frequency prefix-sum problem, especially important with negative numbers.

Skills Tested:
- Identify the Prefix Sum With Counts signal before choosing a template.
- State the invariant for Subarray Sum Equals K: a high-frequency prefix-sum problem, especially important with negative numbers.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Subarray Sum Equals K toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Prefix Sum With Counts invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Valid Sudoku

LeetCode: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

Difficulty: Medium

Pattern: Set Membership By Region

Why It Matters: Practices mapping rows, columns, and boxes to constraint sets.

Skills Tested:
- Identify the Set Membership By Region signal before choosing a template.
- State the invariant for Valid Sudoku: practices mapping rows, columns, and boxes to constraint sets.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Valid Sudoku toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Set Membership By Region invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Insert Delete GetRandom O(1)

LeetCode: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Difficulty: Medium

Pattern: Array Plus Hash Map

Why It Matters: Combines indexed storage with direct lookup and swap-delete mutation.

Skills Tested:
- Identify the Array Plus Hash Map signal before choosing a template.
- State the invariant for Insert Delete GetRandom O(1): combines indexed storage with direct lookup and swap-delete mutation.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Insert Delete GetRandom O(1) toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Array Plus Hash Map invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
