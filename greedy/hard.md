# Greedy Hard Problems

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

## 1. Candy

LeetCode: [Candy](https://leetcode.com/problems/candy/)

Difficulty: Hard

Pattern: Two Pass Greedy

Why It Matters: Satisfies local neighbor constraints both directions.

Skills Tested:
- Identify the Two Pass Greedy signal before choosing a template.
- State the invariant for Candy: satisfies local neighbor constraints both directions.
- Handle counterexamples, tie-breaking, proof gaps, and sorted-order assumptions.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Candy toward dynamic programming, heap scheduling, interval sweep, binary search, or backtracking?
- Which counterexamples case would break the first implementation?
- Can the Two Pass Greedy invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Maximum Performance of a Team

LeetCode: [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

Difficulty: Hard

Pattern: Sort Plus Heap Greedy

Why It Matters: Combines a sorted bottleneck metric with a heap of best supporting candidates.

Skills Tested:
- Identify the Sort Plus Heap Greedy signal before choosing a template.
- State the invariant for Maximum Performance of a Team: combines a sorted bottleneck metric with a heap of best supporting candidates.
- Handle counterexamples, tie-breaking, proof gaps, and sorted-order assumptions.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Maximum Performance of a Team toward dynamic programming, heap scheduling, interval sweep, binary search, or backtracking?
- Which counterexamples case would break the first implementation?
- Can the Sort Plus Heap Greedy invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Minimum Number of Refueling Stops

LeetCode: [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

Difficulty: Hard

Pattern: Heap-Assisted Greedy

Why It Matters: Chooses best previous station only when needed.

Skills Tested:
- Identify the Heap-Assisted Greedy signal before choosing a template.
- State the invariant for Minimum Number of Refueling Stops: chooses best previous station only when needed.
- Handle counterexamples, tie-breaking, proof gaps, and sorted-order assumptions.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Minimum Number of Refueling Stops toward dynamic programming, heap scheduling, interval sweep, binary search, or backtracking?
- Which counterexamples case would break the first implementation?
- Can the Heap-Assisted Greedy invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Create Maximum Number

LeetCode: [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/)

Difficulty: Hard

Pattern: Monotonic Greedy

Why It Matters: Builds best subsequences and merges them.

Skills Tested:
- Identify the Monotonic Greedy signal before choosing a template.
- State the invariant for Create Maximum Number: builds best subsequences and merges them.
- Handle counterexamples, tie-breaking, proof gaps, and sorted-order assumptions.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Create Maximum Number toward dynamic programming, heap scheduling, interval sweep, binary search, or backtracking?
- Which counterexamples case would break the first implementation?
- Can the Monotonic Greedy invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
