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
- Recognize that the largest rectangle ends at every bar with a height equal to that bar's value, and width is bounded by the previous-smaller and next-smaller indices.
- State the invariant: the stack holds indices in strictly increasing height order; popping yields the rectangle whose height is the popped bar and whose width is `i - stack.top - 1`.
- Append a sentinel `0` at the end (or use `len(heights)` as the right boundary at end-of-loop) to drain the stack cleanly.
- Time O(n), space O(n), and contrast with O(n^2) brute force or divide-and-conquer (O(n log n) average).

Common Follow-Ups:
- Maximal Rectangle (LC 85) repeats this routine over each row's histogram of heights.
- Sum of Subarray Minimums (LC 907) uses next-smaller-on-each-side bounds.
- What if some bar heights are unknown until query time (offline sweep).

## 2. Basic Calculator

LeetCode: [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

Difficulty: Hard

Pattern: Sign Stack

Why It Matters: Tests signs, parentheses, and streaming parse state.

Skills Tested:
- Recognize that without `*` and `/`, you can compute the running result with a sign that toggles by parentheses and a stack that saves the outer (result, sign) on `(`.
- State the invariant: at every moment, `result` is the value of the prefix already parsed, and the stack holds the outer state to restore on `)`.
- Handle multi-digit numbers, unary minus, and whitespace robustly.
- Time O(n), space O(stack depth), and contrast with the Shunting-yard algorithm which uses two stacks.

Common Follow-Ups:
- Basic Calculator II (LC 227) adds `*` and `/` and switches to operator precedence.
- Basic Calculator III (LC 772) combines parentheses with full precedence.
- What if the input is streamed and the parser must yield partial results.

## 3. Maximal Rectangle

LeetCode: [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

Difficulty: Hard

Pattern: Per-Row Histogram Stack

Why It Matters: Reduces a 2-D matrix to repeated histogram problems.

Skills Tested:
- Recognize that for each row, you can compute a histogram of consecutive ones ending at that row, then call Largest Rectangle in Histogram.
- State the invariant: `heights[c]` after processing row `r` equals the count of consecutive ones in column `c` ending at `r`, reset to 0 on a `0`.
- Reuse the monotonic stack scaffolding row by row, returning the maximum rectangle across all rows.
- Time O(rows * cols), space O(cols), and explain why a naive 2-D DP that tries every rectangle is O((rows * cols)^2).

Common Follow-Ups:
- Maximal Square (LC 221) restricts shape to a square and switches to DP.
- Number of Submatrices That Sum to Target (LC 1074) replaces zero/one with arbitrary integers.
- How does the answer change with diagonal-allowed rectangles.

## 4. Parsing A Boolean Expression

LeetCode: [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)

Difficulty: Hard

Pattern: Nested Operator Stack

Why It Matters: Practices parsing nested logical expressions.

Skills Tested:
- Recognize that `&(...)`, `|(...)`, `!(...)` are operators with a list of operands inside, which calls for a stack of operand lists per level.
- State the invariant: the stack always holds the partially-constructed argument list of the most-recent unfinished operator.
- Pop on `)`, evaluate the operator on the operand list, and push the result onto the parent's argument list.
- Time O(n), space O(stack depth), and contrast with recursive descent which has the same complexity but a real call stack.

Common Follow-Ups:
- Mini Parser (LC 385) builds nested integer lists with a similar stack of partials.
- What if the language adds short-circuit evaluation rules (`!()` returns early on the first `false` of `&`).
- How would you compile the expression once and reuse it many times.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
