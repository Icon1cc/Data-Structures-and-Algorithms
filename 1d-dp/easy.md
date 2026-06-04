# 1-D Dynamic Programming Easy Problems

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

## 1. Climbing Stairs

LeetCode: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

Difficulty: Easy

Pattern: Linear DP

Why It Matters: The baseline recurrence for ways to reach state i.

Skills Tested:
- Identify the Linear DP signal before choosing a template.
- State the invariant for Climbing Stairs: the baseline recurrence for ways to reach state i.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Climbing Stairs toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Linear DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Min Cost Climbing Stairs

LeetCode: [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

Difficulty: Easy

Pattern: Linear Min Cost DP

Why It Matters: Adds costs and minimum transition choice.

Skills Tested:
- Identify the Linear Min Cost DP signal before choosing a template.
- State the invariant for Min Cost Climbing Stairs: adds costs and minimum transition choice.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Min Cost Climbing Stairs toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Linear Min Cost DP invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Fibonacci Number

LeetCode: [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

Difficulty: Easy

Pattern: Memoization Or Tabulation

Why It Matters: Simple overlapping-subproblem example.

Skills Tested:
- Identify the Memoization Or Tabulation signal before choosing a template.
- State the invariant for Fibonacci Number: simple overlapping-subproblem example.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Fibonacci Number toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Memoization Or Tabulation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. N-th Tribonacci Number

LeetCode: [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

Difficulty: Easy

Pattern: Rolling State

Why It Matters: Practices recurrence with three previous states.

Skills Tested:
- Identify the Rolling State signal before choosing a template.
- State the invariant for N-th Tribonacci Number: practices recurrence with three previous states.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push N-th Tribonacci Number toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Rolling State invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Pascal's Triangle

LeetCode: [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

Difficulty: Easy

Pattern: Row DP

Why It Matters: Builds each row from previous row state.

Skills Tested:
- Identify the Row DP signal before choosing a template.
- State the invariant for Pascal's Triangle: builds each row from previous row state.
- Handle base cases, invalid states, iteration order, and memory compression direction.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Pascal's Triangle toward greedy, graph shortest path, backtracking, BFS, or mathematical formula?
- Which base cases case would break the first implementation?
- Can the Row DP invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
