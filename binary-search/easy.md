# Binary Search Easy Problems

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

## 1. Binary Search

LeetCode: [Binary Search](https://leetcode.com/problems/binary-search/)

Difficulty: Easy

Pattern: Classic Target Search

Why It Matters: Baseline exact lookup with clear inclusive bounds.

Skills Tested:
- Identify the Classic Target Search signal before choosing a template.
- State the invariant for Binary Search: baseline exact lookup with clear inclusive bounds.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Binary Search toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Classic Target Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Search Insert Position

LeetCode: [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Difficulty: Easy

Pattern: Lower Bound

Why It Matters: Turns missing targets into insertion boundaries.

Skills Tested:
- Identify the Lower Bound signal before choosing a template.
- State the invariant for Search Insert Position: turns missing targets into insertion boundaries.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Search Insert Position toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Lower Bound invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. First Bad Version

LeetCode: [First Bad Version](https://leetcode.com/problems/first-bad-version/)

Difficulty: Easy

Pattern: First True Predicate

Why It Matters: The cleanest monotonic predicate example.

Skills Tested:
- Identify the First True Predicate signal before choosing a template.
- State the invariant for First Bad Version: the cleanest monotonic predicate example.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push First Bad Version toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the First True Predicate invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Guess Number Higher or Lower

LeetCode: [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

Difficulty: Easy

Pattern: Classic Target Search

Why It Matters: Practices halving based on comparison feedback.

Skills Tested:
- Identify the Classic Target Search signal before choosing a template.
- State the invariant for Guess Number Higher or Lower: practices halving based on comparison feedback.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Guess Number Higher or Lower toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Classic Target Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Sqrt(x)

LeetCode: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Difficulty: Easy

Pattern: Binary Search On Answer

Why It Matters: Introduces numeric answer search with overflow awareness.

Skills Tested:
- Identify the Binary Search On Answer signal before choosing a template.
- State the invariant for Sqrt(x): introduces numeric answer search with overflow awareness.
- Handle single-element ranges, equality handling, duplicate ambiguity, and excluded boundaries.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sqrt(x) toward linear scan, two pointers, heap selection, or direct math?
- Which single-element ranges case would break the first implementation?
- Can the Binary Search On Answer invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
