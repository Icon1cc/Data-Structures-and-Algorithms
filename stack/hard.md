# Stack Hard Problems

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

## 1. Largest Rectangle in Histogram

LeetCode: [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

Difficulty: Hard

Pattern: Monotonic Increasing Stack

Why It Matters: The classic width computation stack problem.

Skills Tested:
- Identify the Monotonic Increasing Stack signal before choosing a template.
- State the invariant for Largest Rectangle in Histogram: the classic width computation stack problem.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Largest Rectangle in Histogram toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Monotonic Increasing Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Basic Calculator

LeetCode: [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

Difficulty: Hard

Pattern: Expression Stack

Why It Matters: Tests signs, parentheses, and streaming parse state.

Skills Tested:
- Identify the Expression Stack signal before choosing a template.
- State the invariant for Basic Calculator: tests signs, parentheses, and streaming parse state.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Basic Calculator toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Expression Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Maximal Rectangle

LeetCode: [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

Difficulty: Hard

Pattern: Histogram Stack Per Row

Why It Matters: Reduces a 2-D matrix to repeated histogram problems.

Skills Tested:
- Identify the Histogram Stack Per Row signal before choosing a template.
- State the invariant for Maximal Rectangle: reduces a 2-D matrix to repeated histogram problems.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Maximal Rectangle toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Histogram Stack Per Row invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Parsing A Boolean Expression

LeetCode: [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)

Difficulty: Hard

Pattern: Nested Expression Stack

Why It Matters: Practices parsing nested logical expressions.

Skills Tested:
- Identify the Nested Expression Stack signal before choosing a template.
- State the invariant for Parsing A Boolean Expression: practices parsing nested logical expressions.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Parsing A Boolean Expression toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Nested Expression Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
