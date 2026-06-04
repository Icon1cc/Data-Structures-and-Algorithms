# Arrays & Hashing Easy Problems

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

## 1. Two Sum

LeetCode: [Two Sum](https://leetcode.com/problems/two-sum/)

Difficulty: Easy

Pattern: Hash Lookup

Why It Matters: The canonical complement lookup problem and the first test of replacing a nested loop with memory.

Skills Tested:
- Identify the Hash Lookup signal before choosing a template.
- State the invariant for Two Sum: the canonical complement lookup problem and the first test of replacing a nested loop with memory.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Two Sum toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Hash Lookup invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Contains Duplicate

LeetCode: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Difficulty: Easy

Pattern: Hash Set Membership

Why It Matters: Builds the simplest seen-set invariant and forces a clean early exit.

Skills Tested:
- Identify the Hash Set Membership signal before choosing a template.
- State the invariant for Contains Duplicate: builds the simplest seen-set invariant and forces a clean early exit.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Contains Duplicate toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Hash Set Membership invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Valid Anagram

LeetCode: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Difficulty: Easy

Pattern: Frequency Counting

Why It Matters: Tests whether counts, not sorting alone, can represent character multiplicity.

Skills Tested:
- Identify the Frequency Counting signal before choosing a template.
- State the invariant for Valid Anagram: tests whether counts, not sorting alone, can represent character multiplicity.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Valid Anagram toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Frequency Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Ransom Note

LeetCode: [Ransom Note](https://leetcode.com/problems/ransom-note/)

Difficulty: Easy

Pattern: Frequency Counting

Why It Matters: Practices decrementing inventory and detecting when a count is exhausted.

Skills Tested:
- Identify the Frequency Counting signal before choosing a template.
- State the invariant for Ransom Note: practices decrementing inventory and detecting when a count is exhausted.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Ransom Note toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Frequency Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Majority Element

LeetCode: [Majority Element](https://leetcode.com/problems/majority-element/)

Difficulty: Easy

Pattern: Frequency Counting Or Voting

Why It Matters: Introduces the idea that frequency structure can sometimes be compressed to constant space.

Skills Tested:
- Identify the Frequency Counting Or Voting signal before choosing a template.
- State the invariant for Majority Element: introduces the idea that frequency structure can sometimes be compressed to constant space.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Majority Element toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Frequency Counting Or Voting invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
