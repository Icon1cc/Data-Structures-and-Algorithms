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

Pattern: Choose-Or-Skip Backtracking

Why It Matters: The baseline choose-or-skip decision tree.

Skills Tested:
- Recognize that the power set has two branches per index (include or exclude), so backtracking from `i = 0` to `n` enumerates every subset.
- State the invariant: at index `i`, the path holds the chosen prefix; appending a copy to the result on every call captures all `2^n` subsets.
- Compare backtracking with the iterative cascade (each new element doubles the result) and bitmask enumeration.
- Time O(n * 2^n), space O(n) recursion plus output.

Common Follow-Ups:
- Subsets II (LC 90) handles duplicates by sorting and skipping equal siblings.
- Generate all subsets of size exactly `k` (Combinations LC 77).
- Stream subsets lazily without buffering.

## 2. Combination Sum

LeetCode: [Combination Sum](https://leetcode.com/problems/combination-sum/)

Difficulty: Medium

Pattern: Combinations With Reuse

Why It Matters: Tests reusable choices and target pruning.

Skills Tested:
- Recognize that an element can be chosen unlimited times, which means the recursion may stay at the same index after a pick.
- State the invariant: the running `remaining` is non-negative; the recursion ends with success when `remaining == 0` and failure when `remaining < 0` or no candidates remain.
- Sort candidates and break early when a candidate exceeds `remaining` to prune the search.
- Time O(N^(target / min)), space O(target / min) for recursion, and contrast with DP O(N * target).

Common Follow-Ups:
- Combination Sum II (LC 40) forbids reuse and requires duplicate skipping at the same level.
- Combination Sum IV (LC 377) counts ordered combinations and is a 1-D DP.
- What if candidates can be negative.

## 3. Permutations

LeetCode: [Permutations](https://leetcode.com/problems/permutations/)

Difficulty: Medium

Pattern: Used-Set Backtracking

Why It Matters: Builds used-set recursion where order matters.

Skills Tested:
- Recognize that order-sensitive enumeration requires a `used` mask or a swap-based partition to avoid revisiting the same element.
- State the invariant: at each call, `path` holds a prefix of the permutation; choices come from the unused elements.
- Implement either the `used[]` boolean array variant or the in-place swap variant; explain memory differences.
- Time O(n * n!), space O(n) for the path and used set.

Common Follow-Ups:
- Permutations II (LC 47) handles duplicates with sort-then-skip.
- Next Permutation (LC 31) jumps to the next ordering directly.
- Generate the k-th permutation without enumerating all (LC 60).

## 4. Word Search

LeetCode: [Word Search](https://leetcode.com/problems/word-search/)

Difficulty: Medium

Pattern: Grid DFS With Visit Mark

Why It Matters: Core board DFS with visited state.

Skills Tested:
- Recognize that scanning every starting cell and recursing into 4-directional neighbors with a visit mark covers all paths.
- State the invariant: the path so far matches `word[0..k]`; success at `k == len(word) - 1`, failure on bounds, mismatch, or revisit.
- Use a sentinel (`#`) on the cell during recursion and restore it on backtrack to avoid an explicit visited set.
- Time O(M * N * 4 ^ L), space O(L) recursion.

Common Follow-Ups:
- Word Search II (LC 212) batches many words via a trie.
- What if diagonal movement is also allowed.
- Generalize to weighted grids where each step has a cost.

## 5. Generate Parentheses

LeetCode: [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

Difficulty: Medium

Pattern: Counted Backtracking

Why It Matters: Uses counts to prune invalid prefix strings.

Skills Tested:
- Recognize that a valid prefix obeys `open <= n` and `close <= open`, so two counters drive the recursion.
- State the invariant: at every recursion, `open >= close`; appending `(` is allowed when `open < n`, appending `)` when `close < open`.
- Stop when `len(path) == 2 * n` and append a copy.
- Time O(Catalan(n)) which is roughly O(4^n / sqrt(n)), space O(n).

Common Follow-Ups:
- Remove Invalid Parentheses (LC 301) uses BFS for minimum-removal generation.
- Different Ways to Add Parentheses (LC 241) enumerates expression-tree shapes.
- Catalan number combinatorics in detail.

## 6. Letter Combinations of a Phone Number

LeetCode: [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

Difficulty: Medium

Pattern: Cartesian Product Backtracking

Why It Matters: Builds combinations across positions.

Skills Tested:
- Recognize that each digit maps to 3 or 4 letters, so the answer is the Cartesian product of those sets.
- State the invariant: at index `i`, the path holds one letter chosen for each prior digit; recurse over all letters of `digits[i]`.
- Handle the empty input (return empty list, not `[""]` unless that is the spec).
- Time O(3^N * 4^M) where N and M count digits with 3 and 4 letters, space O(N + M).

Common Follow-Ups:
- Word Break II (LC 140) is a Cartesian product over dictionary segments.
- What if the mapping changes online.
- Generalize to keypad with weighted letter probabilities.

## 7. Palindrome Partitioning

LeetCode: [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

Difficulty: Medium

Pattern: Cut Backtracking With Predicate

Why It Matters: Chooses valid cuts over a string.

Skills Tested:
- Recognize that "all decompositions where each piece is a palindrome" is a recursion over cut positions, with a palindrome check on each piece.
- State the invariant: the path holds the chosen palindrome pieces; at index `n`, append the path copy.
- Memoize palindrome checks (or precompute a 2-D `isPal` table) to avoid O(L^2) checks per cut.
- Time O(2^n * n) worst case, space O(n) recursion.

Common Follow-Ups:
- Palindrome Partitioning II (LC 132) minimizes cuts, which becomes a 1-D DP.
- What if pieces must also be of bounded length.
- Stream the generation of partitions.

## 8. Combination Sum II

LeetCode: [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Difficulty: Medium

Pattern: Sort Plus Skip-Equal-Sibling Combinations

Why It Matters: Adds duplicate skipping to sorted candidates.

Skills Tested:
- Recognize that each element is used at most once and duplicates must produce only unique combinations, which is sorted-input plus the skip-equal-sibling-at-the-same-recursion-level rule.
- State the invariant: at level `i`, skip values equal to `candidates[i - 1]` only if `i > start` (the first occurrence at each level must be tried).
- Sort the candidates first; break when the smallest remaining exceeds the remaining target.
- Time O(2^n * n), space O(n).

Common Follow-Ups:
- Subsets II (LC 90) reuses the same skip-equal-sibling rule for power set with duplicates.
- Permutations II (LC 47) reuses the rule for ordered enumeration.
- Generalize to "each element with bounded multiplicity".

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
