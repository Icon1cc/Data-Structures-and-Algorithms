# Arrays & Hashing Hard Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Hard order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. First Missing Positive

LeetCode: [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

Difficulty: Hard

Pattern: In-place Index Marking

Why It Matters: Classic constant-space array indexing problem with difficult boundary handling.

Skills Tested:
- Identify the In-place Index Marking signal before choosing a template.
- State the invariant for First Missing Positive: classic constant-space array indexing problem with difficult boundary handling.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push First Missing Positive toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the In-place Index Marking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Longest Duplicate Substring

LeetCode: [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

Difficulty: Hard

Pattern: Rolling Hash With Binary Search

Why It Matters: Combines hashing, collision awareness, and answer search over substring length.

Skills Tested:
- Identify the Rolling Hash With Binary Search signal before choosing a template.
- State the invariant for Longest Duplicate Substring: combines hashing, collision awareness, and answer search over substring length.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Longest Duplicate Substring toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Rolling Hash With Binary Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Count of Smaller Numbers After Self

LeetCode: [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

Difficulty: Hard

Pattern: Ordered Counting

Why It Matters: Forces prefix-style counting with an ordered structure rather than plain hashing.

Skills Tested:
- Identify the Ordered Counting signal before choosing a template.
- State the invariant for Count of Smaller Numbers After Self: forces prefix-style counting with an ordered structure rather than plain hashing.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Count of Smaller Numbers After Self toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Ordered Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Count of Range Sum

LeetCode: [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

Difficulty: Hard

Pattern: Prefix Sum With Ordered Counting

Why It Matters: Advanced prefix reasoning where counting prior prefixes requires ordered structure.

Skills Tested:
- Identify the Prefix Sum With Ordered Counting signal before choosing a template.
- State the invariant for Count of Range Sum: advanced prefix reasoning where counting prior prefixes requires ordered structure.
- Handle duplicates, empty input, negative values, missing keys, and key overwrite order.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Count of Range Sum toward sorting, two pointers, prefix sums, buckets, or in-place marking?
- Which duplicates case would break the first implementation?
- Can the Prefix Sum With Ordered Counting invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
