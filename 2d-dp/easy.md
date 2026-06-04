# 2-D Dynamic Programming Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.
- Genuine Easy 2-D DP problems on LeetCode are rare; this file stays small intentionally. Depth lives in `medium.md` and `hard.md`.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Pascal's Triangle II

LeetCode: [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

Difficulty: Easy

Pattern: Single-Row DP From Previous Row

Why It Matters: Small row-based table construction.

Skills Tested:
- Recognize that the k-th row is `C(k, 0), C(k, 1), ..., C(k, k)`, computable by repeatedly applying `row[j] = row[j] + row[j - 1]` from right to left.
- State the invariant: at the start of iteration `i`, `row` holds row `i - 1` of Pascal's triangle.
- Iterate from right to left so each `row[j]` reads its own old value plus the unmodified `row[j - 1]`.
- Time O(k^2), space O(k), and contrast with the closed form `C(k, j)` which requires factorials and risks overflow.

Common Follow-Ups:
- Pascal's Triangle (LC 118) returns every row.
- Compute `C(n, k) mod p` via Lucas's theorem when `n` is huge.
- Generate the row online if `k` grows over time.

## 2. Range Sum Query 2D - Immutable

LeetCode: [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

Difficulty: Easy

Pattern: 2-D Prefix Sum

Why It Matters: Introduces two-dimensional cumulative sums.

Skills Tested:
- Recognize that a 2-D prefix-sum table answers any rectangle query in O(1) via the inclusion-exclusion formula `total = P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]`.
- State the invariant: `P[r][c]` is the sum of the submatrix `(0, 0)` to `(r - 1, c - 1)`.
- Build the table with a single double-loop pass using `P[r][c] = matrix[r - 1][c - 1] + P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1]`.
- Build O(M * N), per-query O(1), space O(M * N), and contrast with naive per-query O(M * N) summation.

Common Follow-Ups:
- Range Sum Query 2D - Mutable (LC 308) needs a 2-D Fenwick tree (BIT).
- Maximum Submatrix Sum (LC 363) reuses prefix sums plus a 1-D max-subarray scan.
- Generalize to k-dimensional prefix sums.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
