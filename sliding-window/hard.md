# Sliding Window Hard Problems

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

## 1. Minimum Window Substring

LeetCode: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

Difficulty: Hard

Pattern: Frequency Window

Why It Matters: The most important hard sliding-window problem.

Skills Tested:
- Identify the Frequency Window signal before choosing a template.
- State the invariant for Minimum Window Substring: the most important hard sliding-window problem.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Window Substring toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Frequency Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Sliding Window Maximum

LeetCode: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

Difficulty: Hard

Pattern: Monotonic Window

Why It Matters: Uses a deque to keep maximum candidates.

Skills Tested:
- Identify the Monotonic Window signal before choosing a template.
- State the invariant for Sliding Window Maximum: uses a deque to keep maximum candidates.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sliding Window Maximum toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Monotonic Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Substring with Concatenation of All Words

LeetCode: [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

Difficulty: Hard

Pattern: Fixed Block Window

Why It Matters: Maintains word counts over aligned chunks.

Skills Tested:
- Identify the Fixed Block Window signal before choosing a template.
- State the invariant for Substring with Concatenation of All Words: maintains word counts over aligned chunks.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Substring with Concatenation of All Words toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Fixed Block Window invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Subarrays with K Different Integers

LeetCode: [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

Difficulty: Hard

Pattern: Exactly K Via At Most K

Why It Matters: Turns an exactly-k requirement into two monotonic sliding-window counts.

Skills Tested:
- Identify the Exactly K Via At Most K signal before choosing a template.
- State the invariant for Subarrays with K Different Integers: turns an exactly-k requirement into two monotonic sliding-window counts.
- Handle zero-count keys, negative values, recording order, and k larger than input.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Subarrays with K Different Integers toward prefix sums, hash maps, binary search, monotonic deque, or sorting?
- Which zero-count keys case would break the first implementation?
- Can the Exactly K Via At Most K invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
