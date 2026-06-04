# Math & Geometry Hard Problems

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

## 1. Max Points on a Line

LeetCode: [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)

Difficulty: Hard

Pattern: Slope Hash With Reduced Fractions

Why It Matters: Uses normalized slopes and duplicate handling.

Skills Tested:
- Recognize that for each anchor point, every other point yields a slope; the largest co-linear group is `1 + max(slope_count)`.
- State the invariant: slopes are stored as reduced `(dy, dx)` pairs (with sign normalization) to avoid floating-point comparison errors.
- Handle vertical lines (`dx == 0`), duplicate points (count separately), and division by GCD.
- Time O(n^2), space O(n).

Common Follow-Ups:
- Closest Pair on a Line via sweep.
- What if the slope precision tolerance is configurable.
- Generalize to maximum co-planar points in 3-D.

## 2. Integer to English Words

LeetCode: [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

Difficulty: Hard

Pattern: Three-Digit Group Recursion

Why It Matters: Tests numeric decomposition, grouping, and careful handling of zero-valued segments.

Skills Tested:
- Recognize that English number words decompose into groups of three (thousands, millions, billions); each group's words are formed by hundreds plus tens plus ones.
- State the invariant: a helper converts `0..999` to words; the main function appends the right group label after each non-zero group.
- Handle zero (return `"Zero"`), single-word numbers like 11-19, and tens 20, 30, ..., 90 with hyphenation.
- Time O(log n base 1000), space O(log n base 1000).

Common Follow-Ups:
- English Words to Integer (parser).
- Generalize to other languages with different grouping rules.
- What if the input is a fraction or a decimal.

## 3. Erect the Fence

LeetCode: [Erect the Fence](https://leetcode.com/problems/erect-the-fence/)

Difficulty: Hard

Pattern: Andrew's Monotone Chain Convex Hull

Why It Matters: Classic orientation and hull problem.

Skills Tested:
- Recognize that the convex hull (including collinear boundary points) is computed by sorting points by `(x, y)` and walking the lower then upper hull, keeping a left-turn-or-collinear orientation.
- State the invariant: at every step, the partial hull stays convex (or collinear) by popping any point that makes a strict right turn.
- Handle duplicate points and fully collinear inputs.
- Time O(n log n), space O(n).

Common Follow-Ups:
- Smallest Enclosing Circle.
- What if points arrive online (dynamic convex hull).
- Compute hull diameter or perimeter from the hull output.

## 4. Rectangle Area II

LeetCode: [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

Difficulty: Hard

Pattern: Coordinate Compression Plus Sweep Line

Why It Matters: Combines coordinate compression with area accumulation.

Skills Tested:
- Recognize that the union of axis-aligned rectangles is computable via coordinate compression on x or y, then a sweep line that tracks active intervals.
- State the invariant: at each x boundary, sum the lengths of currently active y-intervals (by counts after coordinate compression) and multiply by `dx`.
- Reduce modulo `1e9 + 7` only at the end to preserve intermediate precision.
- Time O(n^2 log n) with sweep, space O(n^2).

Common Follow-Ups:
- The Skyline Problem (LC 218) is a sweep-line classic.
- Rectangle Area I (LC 223) is the two-rectangle special case.
- Generalize to rotated rectangles or polygons.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
