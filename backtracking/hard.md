# Backtracking Hard Problems

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

## 1. N-Queens

LeetCode: [N-Queens](https://leetcode.com/problems/n-queens/)

Difficulty: Hard

Pattern: Constraint Sets Pruning

Why It Matters: Classic constraints over columns and diagonals.

Skills Tested:
- Recognize that placing one queen per row reduces the search to choosing a column at each row, with three constraint sets (cols, diag1, diag2) eliminating conflicts in O(1).
- State the invariant: at row `r`, sets contain exactly the columns and diagonals occupied by queens in rows `0..r-1`.
- Encode diagonals as `r - c` (anti-diagonal) and `r + c` (diagonal) for O(1) membership.
- Time O(N!) worst case, space O(N) recursion plus board copy at solutions.

Common Follow-Ups:
- N-Queens II (LC 52) only counts solutions, removing the board copy.
- What if the board is non-square or has blocked cells.
- Symmetry reductions: count fundamental solutions only.

## 2. Sudoku Solver

LeetCode: [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

Difficulty: Hard

Pattern: Constraint Backtracking With In-Place Mutation

Why It Matters: Tests pruning and mutable board state.

Skills Tested:
- Recognize that Sudoku has 9 row sets, 9 column sets, and 9 box sets; placing a digit succeeds only if the digit is absent from all three relevant sets.
- State the invariant: as the recursion explores `(r, c)`, the three sets reflect every digit placed in rows `0..r` and prior columns within row `r`.
- Backtrack: place a digit, recurse to the next empty cell, undo on failure.
- Time O(9^M) where M is the count of empty cells, space O(81) for sets.

Common Follow-Ups:
- Valid Sudoku (LC 36) is the validation-only variant.
- Optimize with the Most-Constrained-Variable heuristic.
- Generalize to NxN with sqrt(N) box width.

## 3. 24 Game

LeetCode: [24 Game](https://leetcode.com/problems/24-game/)

Difficulty: Hard

Pattern: Pair-Combine Recursion With Floating-Point Tolerance

Why It Matters: Explores all arithmetic pair combinations while controlling floating-point tolerance.

Skills Tested:
- Recognize that combining four numbers to 24 is a recursion: pick two values, apply each of `+ - * /`, replace them with the result, recurse on the smaller list.
- State the invariant: at each recursion, the list is the current operand multiset; success when the list has one value within tolerance of 24.
- Avoid divide-by-zero and use a small epsilon (1e-6) on float comparisons.
- Time O(constant) given fixed input size 4, but conceptually O(N^2 * 4 * 2 ^ N) for N operands.

Common Follow-Ups:
- Generalize to N operands and an arbitrary target.
- Forbid integer division (only multiplication, addition, subtraction).
- Use rational arithmetic to avoid floating-point error.

## 4. Expression Add Operators

LeetCode: [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

Difficulty: Hard

Pattern: String Partition With Operator Choice

Why It Matters: Hard expression-generation state management.

Skills Tested:
- Recognize that at each split position, three operators (+, -, *) plus "no-op" (concatenation, only at the start) define the branching factor.
- State the invariant: track the running value and the previous operand to undo and replace it when handling `*`'s precedence.
- Forbid leading zeros on multi-digit operands.
- Time O(4^n), space O(n) recursion.

Common Follow-Ups:
- Different Ways to Add Parentheses (LC 241) explores expression-tree groupings.
- Basic Calculator III (LC 772) evaluates expressions with full precedence.
- What if the operator set is user-supplied.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
