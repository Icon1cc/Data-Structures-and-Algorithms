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

Pattern: Pruned Search

Why It Matters: Classic constraints over columns and diagonals.

Skills Tested:
- Identify the Pruned Search signal before choosing a template.
- State the invariant for N-Queens: classic constraints over columns and diagonals.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push N-Queens toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Pruned Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Sudoku Solver

LeetCode: [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

Difficulty: Hard

Pattern: Constraint Grid Search

Why It Matters: Tests pruning and mutable board state.

Skills Tested:
- Identify the Constraint Grid Search signal before choosing a template.
- State the invariant for Sudoku Solver: tests pruning and mutable board state.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sudoku Solver toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Constraint Grid Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. 24 Game

LeetCode: [24 Game](https://leetcode.com/problems/24-game/)

Difficulty: Hard

Pattern: Expression Search With Pruning

Why It Matters: Explores all arithmetic pair combinations while controlling floating-point tolerance.

Skills Tested:
- Identify the Expression Search With Pruning signal before choosing a template.
- State the invariant for 24 Game: explores all arithmetic pair combinations while controlling floating-point tolerance.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push 24 Game toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Expression Search With Pruning invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Expression Add Operators

LeetCode: [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

Difficulty: Hard

Pattern: Partition And Evaluate

Why It Matters: Hard expression-generation state management.

Skills Tested:
- Identify the Partition And Evaluate signal before choosing a template.
- State the invariant for Expression Add Operators: hard expression-generation state management.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Expression Add Operators toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Partition And Evaluate invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
