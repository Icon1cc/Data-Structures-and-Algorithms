# Sliding Window Medium Problems

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

## 1. Longest Substring Without Repeating Characters

LeetCode: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Difficulty: Medium

Pattern: Variable Frequency Window

Why It Matters: The core longest-valid-substring pattern.

Skills Tested:
- Identify the Variable Frequency Window signal before choosing a template.
- State the invariant for Longest Substring Without Repeating Characters: the core longest-valid-substring pattern.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Substring Without Repeating Characters toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Variable Frequency Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Longest Repeating Character Replacement

LeetCode: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Difficulty: Medium

Pattern: Frequency Window

Why It Matters: Tests maintaining a max frequency while shrinking.

Skills Tested:
- Identify the Frequency Window signal before choosing a template.
- State the invariant for Longest Repeating Character Replacement: tests maintaining a max frequency while shrinking.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Repeating Character Replacement toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Frequency Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Permutation in String

LeetCode: [Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Difficulty: Medium

Pattern: Frequency Window

Why It Matters: Fixed-length anagram matching with counts.

Skills Tested:
- Identify the Frequency Window signal before choosing a template.
- State the invariant for Permutation in String: fixed-length anagram matching with counts.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Permutation in String toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Frequency Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Find All Anagrams in a String

LeetCode: [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Difficulty: Medium

Pattern: Frequency Window

Why It Matters: Collects every matching fixed-length window.

Skills Tested:
- Identify the Frequency Window signal before choosing a template.
- State the invariant for Find All Anagrams in a String: collects every matching fixed-length window.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find All Anagrams in a String toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Frequency Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Minimum Size Subarray Sum

LeetCode: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

Difficulty: Medium

Pattern: Variable Sum Window

Why It Matters: Classic shortest valid positive-sum window.

Skills Tested:
- Identify the Variable Sum Window signal before choosing a template.
- State the invariant for Minimum Size Subarray Sum: classic shortest valid positive-sum window.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Size Subarray Sum toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Variable Sum Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Max Consecutive Ones III

LeetCode: [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

Difficulty: Medium

Pattern: At Most K Window

Why It Matters: Transforms flips into a count of invalid values.

Skills Tested:
- Identify the At Most K Window signal before choosing a template.
- State the invariant for Max Consecutive Ones III: transforms flips into a count of invalid values.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Max Consecutive Ones III toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the At Most K Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Fruit Into Baskets

LeetCode: [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

Difficulty: Medium

Pattern: At Most Two Distinct

Why It Matters: The standard at-most-k distinct window.

Skills Tested:
- Identify the At Most Two Distinct signal before choosing a template.
- State the invariant for Fruit Into Baskets: the standard at-most-k distinct window.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Fruit Into Baskets toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the At Most Two Distinct invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Frequency of the Most Frequent Element

LeetCode: [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

Difficulty: Medium

Pattern: Sorted Window Cost

Why It Matters: Combines sorting with a window cost invariant.

Skills Tested:
- Identify the Sorted Window Cost signal before choosing a template.
- State the invariant for Frequency of the Most Frequent Element: combines sorting with a window cost invariant.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Frequency of the Most Frequent Element toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Sorted Window Cost invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
