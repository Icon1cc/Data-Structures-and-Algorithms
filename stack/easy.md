# Stack Easy Problems

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

## 1. Valid Parentheses

LeetCode: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Difficulty: Easy

Pattern: Balanced Delimiters

Why It Matters: The baseline stack problem for nested order.

Skills Tested:
- Recognize that nested-bracket matching is LIFO: the most recent open bracket must match the next close bracket.
- State the invariant: at every step, the stack holds the still-open brackets in the order they appeared.
- Handle a leading close bracket (empty stack rejection), mismatched types on pop, and a non-empty stack at end.
- Time O(n), space O(n), and contrast with counter approaches which fail when bracket types differ.

Common Follow-Ups:
- Generate Parentheses (LC 22) inverts the predicate to enumeration.
- Minimum Add to Make Parentheses Valid (LC 921) counts edits instead of validating.
- What changes when there are three bracket types plus quoted strings that contain brackets.

## 2. Baseball Game

LeetCode: [Baseball Game](https://leetcode.com/problems/baseball-game/)

Difficulty: Easy

Pattern: LIFO Simulation

Why It Matters: Practices undo-like operations with recent scores.

Skills Tested:
- Recognize that "C undoes the last", "D doubles the last", "+ adds the last two" all reference recent state, which is exactly a stack.
- State the invariant: the stack always holds the valid scores in the order they were recorded.
- Handle malformed inputs that ask for `+` with fewer than two scores or `D`/`C` with an empty stack (problem guarantees do, but state the assumption).
- Time O(n), space O(n), and explain why an array with index pointers is equivalent.

Common Follow-Ups:
- Design a streaming evaluator where commands arrive one at a time.
- What if commands include "average of all so far" - can the stack still answer in O(1).
- How would you support an undo of an undo (replay log).

## 3. Backspace String Compare

LeetCode: [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

Difficulty: Easy

Pattern: Reverse Two Pointers Or Stack

Why It Matters: Shows how editing behavior can be simulated or optimized.

Skills Tested:
- Recognize that `#` is a "delete previous", which is a stack-pop operation.
- State the invariant: after processing each character, the stack equals the visible string so far.
- Optimize to O(1) extra space by walking both strings from the right and skipping characters owed to backspaces.
- Time O(n + m), space O(1) for the two-pointer variant or O(n + m) for the stack variant.

Common Follow-Ups:
- Build an editor that supports backspace plus insert at cursor.
- What if `#` deletes a character at a stored index, not the most recent.
- How does the answer change when input is streamed and you must answer equality after every step.

## 4. Next Greater Element I

LeetCode: [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

Difficulty: Easy

Pattern: Monotonic Decreasing Stack

Why It Matters: Introduces nearest greater mapping.

Skills Tested:
- Recognize that "for each value in `nums2`, find the first larger value to its right" is the canonical monotonic-decreasing stack scan.
- State the invariant: the stack holds indices (or values) whose next greater has not yet been found, in strictly decreasing order of value.
- Build the next-greater map for `nums2` first, then look up each `nums1[i]` directly.
- Time O(n + m), space O(n), and contrast with O(n * m) brute force.

Common Follow-Ups:
- Next Greater Element II (LC 503) handles a circular array via two passes.
- Next Greater Element III (LC 556) uses a digit-permutation argument.
- Daily Temperatures (LC 739) replaces value with distance.

## 5. Remove All Adjacent Duplicates In String

LeetCode: [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

Difficulty: Easy

Pattern: Stack Cancellation

Why It Matters: Builds cancellation logic with the top element.

Skills Tested:
- Recognize that adjacent duplicates can be folded by checking the top of the stack against each incoming character.
- State the invariant: at every step, the stack contains the prefix after every possible cancellation.
- Handle the case where a cancellation creates a new adjacent duplicate (the loop on the top-of-stack handles it implicitly).
- Time O(n), space O(n), and contrast with repeated string scans that are O(n^2).

Common Follow-Ups:
- Remove All Adjacent Duplicates II (LC 1209) generalizes the duplicate count from 2 to `k`.
- 1209 follow-up: store `(char, count)` pairs to avoid per-character pushes.
- What if the cancellation rule is "any matching pair regardless of distance" (graph matching, much harder).

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
