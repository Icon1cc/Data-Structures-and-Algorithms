# Math & Geometry Medium Problems

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

## 1. Rotate Image

LeetCode: [Rotate Image](https://leetcode.com/problems/rotate-image/)

Difficulty: Medium

Pattern: Transpose Plus Reverse

Why It Matters: Core in-place matrix rotation.

Skills Tested:
- Recognize that a 90-degree clockwise rotation equals "transpose, then reverse each row" in place.
- State the invariant: after transpose, `matrix[i][j] = old[j][i]`; after row reverse, `matrix[i][j] = old[n - 1 - j][i]`, the rotation result.
- Avoid out-of-place buffers by performing both passes in place.
- Time O(n^2), space O(1) extra.

Common Follow-Ups:
- 90-degree counter-clockwise: transpose then reverse each column instead of each row.
- What if the matrix is non-square (no longer in place).
- Generalize to rotating a 3-D tensor.

## 2. Spiral Matrix

LeetCode: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

Difficulty: Medium

Pattern: Boundary Walk

Why It Matters: Boundary-driven traversal.

Skills Tested:
- Recognize that spiral order walks four boundaries (top, right, bottom, left) and shrinks inward.
- State the invariant: at every iteration, the current ring is bounded by `top, bottom, left, right`; after each ring, all four shrink.
- Handle the inner row-only or column-only cases that occur when `top == bottom` or `left == right`.
- Time O(M * N), space O(1) extra (output excluded).

Common Follow-Ups:
- Spiral Matrix II (LC 59) generates a spiral matrix.
- What if the matrix is sparse and only non-zero entries should be emitted.
- Generalize to spiral traversal on a hexagonal grid.

## 3. Pow(x, n)

LeetCode: [Pow(x, n)](https://leetcode.com/problems/powx-n/)

Difficulty: Medium

Pattern: Fast Exponentiation By Squaring

Why It Matters: Uses exponent halving and negative exponent handling.

Skills Tested:
- Recognize that `x^n` can be computed in `log n` multiplications by squaring `x` and halving `n`.
- State the invariant: at every step, the remaining `n >> 1` exponent applies to `x * x`; if the low bit is set, multiply the running result by the current `x`.
- Negate `n` and invert `x` for negative exponents (watch out for `n == INT_MIN` overflow).
- Time O(log n), space O(1) iterative or O(log n) recursive.

Common Follow-Ups:
- Modular Exponentiation `x^n mod p` reuses the same squaring with mod after each multiply.
- Matrix Exponentiation generalizes to integer matrices.
- What if `x` is a complex number (still works).

## 4. Set Matrix Zeroes

LeetCode: [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

Difficulty: Medium

Pattern: First Row And Column As Markers

Why It Matters: Uses first row and column as markers.

Skills Tested:
- Recognize that the first row and column can encode "this row should zero" and "this column should zero" without extra memory, but the original (0, 0) cell must be tracked separately.
- State the invariant: after the first scan, `matrix[i][0] == 0` means row `i` zeros, `matrix[0][j] == 0` means column `j` zeros.
- Process the body before zeroing the markers themselves to avoid clobbering.
- Time O(M * N), space O(1) extra.

Common Follow-Ups:
- Game of Life (LC 289) reuses in-place encoding via temporary states.
- What if mutation must be undone on demand.
- Generalize to k-zeroing rules.

## 5. Multiply Strings

LeetCode: [Multiply Strings](https://leetcode.com/problems/multiply-strings/)

Difficulty: Medium

Pattern: Grade-School Multiply With Carry

Why It Matters: Implements numeric multiplication over characters.

Skills Tested:
- Recognize that digit `i` of `num1` times digit `j` of `num2` lands in positions `i + j` and `i + j + 1` of the product.
- State the invariant: the result array (length `m + n`) accumulates partial products; carries propagate from low to high.
- Strip leading zeros at the end; handle the all-zero product as `"0"`.
- Time O(m * n), space O(m + n).

Common Follow-Ups:
- Add Strings (LC 415) is the simpler add-with-carry sibling.
- Big-integer multiplication via Karatsuba achieves O(n^log2 3).
- What if numbers are stored in scientific notation.

## 6. Integer to Roman

LeetCode: [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

Difficulty: Medium

Pattern: Greedy Symbol Subtraction

Why It Matters: Maps values to symbols in descending order.

Skills Tested:
- Recognize that pre-listing the 13 value-symbol pairs (including subtractive forms like 4=`IV`, 9=`IX`, 40=`XL`, 90=`XC`, 400=`CD`, 900=`CM`) reduces the problem to greedy subtraction.
- State the invariant: at every step, find the largest pair whose value `<= num`; append the symbol; subtract.
- Order the table from largest to smallest to make the loop simple.
- Time O(1) (bounded by 13 iterations), space O(1).

Common Follow-Ups:
- Roman to Integer (LC 13) is the inverse parser.
- Generalize to other numeral systems with subtractive forms.
- What if the value space exceeds 3999 (extension rules).

## 7. Factorial Trailing Zeroes

LeetCode: [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

Difficulty: Medium

Pattern: Legendre's Formula On Prime 5

Why It Matters: Counts factors of five across multiples.

Skills Tested:
- Recognize that trailing zeros come from factors of 10, which equal `min(count of 2s, count of 5s) = count of 5s` (5s are scarcer).
- State the invariant: the answer is `n // 5 + n // 25 + n // 125 + ...` until the divisor exceeds `n`.
- Handle very large `n` without overflow.
- Time O(log n base 5), space O(1).

Common Follow-Ups:
- Preimage Size of Factorial Zeros Function (LC 793) inverts the question.
- Generalize to any prime factor count in `n!`.
- What if the base is not 10 (count factors of `base`'s prime factors).

## 8. Random Pick with Weight

LeetCode: [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

Difficulty: Medium

Pattern: Prefix Sum Plus Binary Search

Why It Matters: Maps weighted random selection to prefix ranges.

Skills Tested:
- Recognize that a weighted pick is a uniform pick from `[1, total]` followed by a binary search to find the corresponding bucket via the prefix-sum array.
- State the invariant: `prefix[i]` is the cumulative weight up to index `i`; the answer is `bisect_left(prefix, randint(1, total))`.
- Build the prefix once in the constructor; per-call cost is O(log n).
- Per-call time O(log n), space O(n).

Common Follow-Ups:
- Random Pick from Distribution Online with updates (Fenwick tree).
- Reservoir sampling for streams.
- Generalize to weighted-without-replacement sampling.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
