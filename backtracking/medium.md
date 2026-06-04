# Backtracking Medium Problems

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

## 1. Subsets

LeetCode: [Subsets](https://leetcode.com/problems/subsets/)

Difficulty: Medium

Pattern: Subsets

Why It Matters: The baseline choose-or-skip decision tree.

Skills Tested:
- Identify the Subsets signal before choosing a template.
- State the invariant for Subsets: the baseline choose-or-skip decision tree.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Subsets toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Subsets invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Combination Sum

LeetCode: [Combination Sum](https://leetcode.com/problems/combination-sum/)

Difficulty: Medium

Pattern: Combinations

Why It Matters: Tests reusable choices and target pruning.

Skills Tested:
- Identify the Combinations signal before choosing a template.
- State the invariant for Combination Sum: tests reusable choices and target pruning.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Combination Sum toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Combinations invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Permutations

LeetCode: [Permutations](https://leetcode.com/problems/permutations/)

Difficulty: Medium

Pattern: Permutations

Why It Matters: Builds used-set recursion where order matters.

Skills Tested:
- Identify the Permutations signal before choosing a template.
- State the invariant for Permutations: builds used-set recursion where order matters.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Permutations toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Permutations invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Word Search

LeetCode: [Word Search](https://leetcode.com/problems/word-search/)

Difficulty: Medium

Pattern: Constraint Grid Search

Why It Matters: Core board DFS with visited state.

Skills Tested:
- Identify the Constraint Grid Search signal before choosing a template.
- State the invariant for Word Search: core board DFS with visited state.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Word Search toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Constraint Grid Search invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Generate Parentheses

LeetCode: [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

Difficulty: Medium

Pattern: Constrained Backtracking

Why It Matters: Uses counts to prune invalid prefix strings.

Skills Tested:
- Identify the Constrained Backtracking signal before choosing a template.
- State the invariant for Generate Parentheses: uses counts to prune invalid prefix strings.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Generate Parentheses toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Constrained Backtracking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Letter Combinations of a Phone Number

LeetCode: [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

Difficulty: Medium

Pattern: Cartesian Product Backtracking

Why It Matters: Builds combinations across positions.

Skills Tested:
- Identify the Cartesian Product Backtracking signal before choosing a template.
- State the invariant for Letter Combinations of a Phone Number: builds combinations across positions.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Letter Combinations of a Phone Number toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Cartesian Product Backtracking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Palindrome Partitioning

LeetCode: [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

Difficulty: Medium

Pattern: Partition Backtracking

Why It Matters: Chooses valid cuts over a string.

Skills Tested:
- Identify the Partition Backtracking signal before choosing a template.
- State the invariant for Palindrome Partitioning: chooses valid cuts over a string.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Palindrome Partitioning toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Partition Backtracking invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Combination Sum II

LeetCode: [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Difficulty: Medium

Pattern: Duplicate-Safe Combinations

Why It Matters: Adds duplicate skipping to sorted candidates.

Skills Tested:
- Identify the Duplicate-Safe Combinations signal before choosing a template.
- State the invariant for Combination Sum II: adds duplicate skipping to sorted candidates.
- Handle duplicate choices, missing undo, invalid pruning, and output-size complexity.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Combination Sum II toward dynamic programming, greedy, BFS, trie pruning, or bitmask enumeration?
- Which duplicate choices case would break the first implementation?
- Can the Duplicate-Safe Combinations invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
