# Stack Medium Problems

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

## 1. Min Stack

LeetCode: [Min Stack](https://leetcode.com/problems/min-stack/)

Difficulty: Medium

Pattern: Auxiliary Stack

Why It Matters: Combines stack operations with constant-time minimum queries.

Skills Tested:
- Identify the Auxiliary Stack signal before choosing a template.
- State the invariant for Min Stack: combines stack operations with constant-time minimum queries.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Min Stack toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Auxiliary Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Evaluate Reverse Polish Notation

LeetCode: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Difficulty: Medium

Pattern: Expression Stack

Why It Matters: Exercises operand ordering and operator evaluation.

Skills Tested:
- Identify the Expression Stack signal before choosing a template.
- State the invariant for Evaluate Reverse Polish Notation: exercises operand ordering and operator evaluation.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Evaluate Reverse Polish Notation toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Expression Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Daily Temperatures

LeetCode: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Difficulty: Medium

Pattern: Monotonic Decreasing Stack

Why It Matters: Core next-greater-distance problem.

Skills Tested:
- Identify the Monotonic Decreasing Stack signal before choosing a template.
- State the invariant for Daily Temperatures: core next-greater-distance problem.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Daily Temperatures toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Monotonic Decreasing Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Car Fleet

LeetCode: [Car Fleet](https://leetcode.com/problems/car-fleet/)

Difficulty: Medium

Pattern: Monotonic Arrival Times

Why It Matters: Uses stack-like grouping after sorting by position.

Skills Tested:
- Identify the Monotonic Arrival Times signal before choosing a template.
- State the invariant for Car Fleet: uses stack-like grouping after sorting by position.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Car Fleet toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Monotonic Arrival Times invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Decode String

LeetCode: [Decode String](https://leetcode.com/problems/decode-string/)

Difficulty: Medium

Pattern: Nested Stack State

Why It Matters: Tests nested counters and partial string state.

Skills Tested:
- Identify the Nested Stack State signal before choosing a template.
- State the invariant for Decode String: tests nested counters and partial string state.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Decode String toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Nested Stack State invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Asteroid Collision

LeetCode: [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

Difficulty: Medium

Pattern: LIFO Simulation

Why It Matters: Forces repeated resolution against the most recent survivor.

Skills Tested:
- Identify the LIFO Simulation signal before choosing a template.
- State the invariant for Asteroid Collision: forces repeated resolution against the most recent survivor.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Asteroid Collision toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the LIFO Simulation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Online Stock Span

LeetCode: [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

Difficulty: Medium

Pattern: Monotonic Stack With Counts

Why It Matters: Compresses previous prices into spans.

Skills Tested:
- Identify the Monotonic Stack With Counts signal before choosing a template.
- State the invariant for Online Stock Span: compresses previous prices into spans.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Online Stock Span toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Monotonic Stack With Counts invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Simplify Path

LeetCode: [Simplify Path](https://leetcode.com/problems/simplify-path/)

Difficulty: Medium

Pattern: Path Stack

Why It Matters: Maps filesystem rules to stack operations.

Skills Tested:
- Identify the Path Stack signal before choosing a template.
- State the invariant for Simplify Path: maps filesystem rules to stack operations.
- Handle empty stack, equal values, sentinel handling, and index versus value storage.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Simplify Path toward deque, heap, recursion, counters, or direct simulation?
- Which empty stack case would break the first implementation?
- Can the Path Stack invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
