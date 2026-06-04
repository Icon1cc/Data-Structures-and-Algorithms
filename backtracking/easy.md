# Backtracking Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.
- Genuine Easy backtracking problems are rare on LeetCode (most subset and permutation problems are Medium); this file stays focused, with depth in `medium.md` and `hard.md`.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Binary Tree Paths

LeetCode: [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

Difficulty: Easy

Pattern: Path Backtracking

Why It Matters: Introduces path push/pop and copying at leaves.

Skills Tested:
- Recognize that all root-to-leaf paths require a DFS that pushes the node value before recursing and pops it after, with a copy of the path saved at every leaf.
- State the invariant: the path list always equals the current root-to-node sequence; modifying after appending a leaf-copy never corrupts the saved result.
- Handle null roots, single-node trees, and trees with only left or only right subtrees.
- Time O(n * h), space O(h) for the path stack, and contrast with concatenating strings which is O(n * h^2).

Common Follow-Ups:
- Path Sum II (LC 113) layers a target-sum predicate on the same scaffold.
- Sum Root to Leaf Numbers (LC 129) reduces each path to a base-10 integer.
- What if you must yield paths lazily without buffering all of them.

## 2. Path Sum

LeetCode: [Path Sum](https://leetcode.com/problems/path-sum/)

Difficulty: Easy

Pattern: Recursive Path State

Why It Matters: Practices carrying remaining target down a tree.

Skills Tested:
- Recognize that root-to-leaf path-sum equality is naturally a recursion that subtracts the current node's value from the remaining target.
- State the invariant: at a leaf, return `remaining == 0`; at an inner node, OR the result over the children's recursions.
- Handle null roots (return false), trees where the only path matches at a non-leaf (must reach a leaf), and negative values.
- Time O(n), space O(h), and contrast with collecting all paths and then checking, which uses extra memory.

Common Follow-Ups:
- Path Sum II (LC 113) returns every matching path.
- Path Sum III (LC 437) counts paths starting at any node using prefix sums.
- What if the sum target is approximate (within tolerance) on real-valued trees.

## 3. Sum of All Subset XOR Totals

LeetCode: [Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)

Difficulty: Easy

Pattern: Subset Enumeration

Why It Matters: Small enumeration problem with subset choices.

Skills Tested:
- Recognize that summing XOR over every subset is a 2^n enumeration; backtracking with include/exclude is the simplest baseline before the bit-trick optimization.
- State the invariant: the recursion tracks the running XOR; at a leaf (index `n`), add the running XOR to the answer.
- Discover the closed-form: each bit set in any element contributes `2^(n-1)` to the sum, so the answer is `OR(nums) * 2^(n-1)`.
- Time O(2^n) backtracking or O(n) with the bit observation, and use the small `n` constraint to justify the simpler approach.

Common Follow-Ups:
- Subsets (LC 78) enumerates the subsets directly.
- What if the operation is sum (not XOR) over all subsets.
- Generalize to all subsets of size exactly `k`.

## 4. Letter Case Permutation

LeetCode: [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

Difficulty: Easy

Pattern: Branch-On-Character Backtracking

Why It Matters: Shows backtracking when each position has a binary choice (case toggle) without permuting positions.

Skills Tested:
- Recognize that letters offer two branches (lower and upper) while digits offer one, which is a per-position binary or unary choice.
- State the invariant: at index `i`, the current path holds the chosen prefix; recursing to `i + 1` covers the remaining decisions.
- Handle digits (single branch), single-character strings, and empty strings.
- Time O(n * 2^n), space O(n) for recursion plus output, and contrast with bitmask iteration over `2^k` (where `k` is the count of letters).

Common Follow-Ups:
- Generate Parentheses (LC 22) uses a similar prefix-with-constraints recursion.
- What if some characters are emojis with multiple case variants.
- Generalize to "for each position, choose from a per-position set".

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
