# Heap / Priority Queue Easy Problems

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

## 1. Last Stone Weight

LeetCode: [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

Difficulty: Easy

Pattern: Max Heap Simulation

Why It Matters: Baseline repeated maximum extraction.

Skills Tested:
- Identify the Max Heap Simulation signal before choosing a template.
- State the invariant for Last Stone Weight: baseline repeated maximum extraction.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Last Stone Weight toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Max Heap Simulation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Kth Largest Element in a Stream

LeetCode: [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

Difficulty: Easy

Pattern: Top K Heap

Why It Matters: Maintains kth largest under streaming updates.

Skills Tested:
- Identify the Top K Heap signal before choosing a template.
- State the invariant for Kth Largest Element in a Stream: maintains kth largest under streaming updates.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Kth Largest Element in a Stream toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Top K Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Relative Ranks

LeetCode: [Relative Ranks](https://leetcode.com/problems/relative-ranks/)

Difficulty: Easy

Pattern: Heap Or Sort Ranking

Why It Matters: Connects priority ordering to ranked output.

Skills Tested:
- Identify the Heap Or Sort Ranking signal before choosing a template.
- State the invariant for Relative Ranks: connects priority ordering to ranked output.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Relative Ranks toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Heap Or Sort Ranking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Take Gifts From the Richest Pile

LeetCode: [Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)

Difficulty: Easy

Pattern: Max Heap Simulation

Why It Matters: Practices repeated best-item updates.

Skills Tested:
- Identify the Max Heap Simulation signal before choosing a template.
- State the invariant for Take Gifts From the Richest Pile: practices repeated best-item updates.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Take Gifts From the Richest Pile toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Max Heap Simulation invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
