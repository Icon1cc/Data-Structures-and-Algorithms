# 2-D Dynamic Programming Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Grid DP | grid | Do not use if movement has cycles without a topological order |
| Two String DP | two strings | Do not use substring logic when order can skip characters |
| Knapsack Table | items | Do not reuse the same item unless the problem is unbounded |
| Interval DP | interval | Do not fill by start index alone if inner intervals are not ready |
| Path Counting With Obstacles | obstacle | Do not add paths through invalid cells |
| State Compression | rolling row | Do not compress if reconstruction of the answer path is required |
| Game DP | two players | Do not greedily take the larger end without proof |

## Pattern: Grid DP

### Beginner Intuition

Each cell combines answers from cells that can move into it.

### When To Use It

Use for unique paths, minimum path sum, and obstacle grids.

### When Not To Use It

Do not use if movement has cycles without a topological order.

### Recognition Signals

- grid
- paths
- top left
- obstacles

### Example Problems

- Unique Paths
- Minimum Path Sum

### Common Mistakes

- Initializing the first row and first column to 1 unconditionally; an obstacle blocks every cell beyond it in that row/column.
- Reading `dp[r - 1][c]` at `r == 0` without bounds checking; either pad with a sentinel row or special-case the boundary.
- Mixing row-then-column with column-then-row iteration when the recurrence depends on both `top` and `left`; pick row-major and stick with it.

### Pseudocode Or Template

```text
for r in range(rows):
    for c in range(cols):
        dp[r][c] = combine(dp[r-1][c], dp[r][c-1])
```

### Complexity Notes

O(rows * cols) time.

### Interview Explanation

The state dp[r][c] answers the subproblem ending at that cell.

## Pattern: Two String DP

### Beginner Intuition

Use prefixes of two strings as the state axes.

### When To Use It

Use for LCS, edit distance, interleaving, and distinct subsequences.

### When Not To Use It

Do not use substring logic when order can skip characters.

### Recognition Signals

- two strings
- prefixes
- edit
- subsequence

### Example Problems

- Longest Common Subsequence
- Edit Distance

### Common Mistakes

- Confusing 1-indexed `dp[i][j]` with 0-indexed `text[i - 1]`; the off-by-one is the source of most bugs in these recurrences.
- Forgetting to seed `dp[0][j] = j` and `dp[i][0] = i` for Edit Distance; without those, deleting or inserting prefixes is impossible.
- Treating "longest common substring" like "longest common subsequence"; the former resets to 0 on mismatch, the latter takes the max of the two prefixes.

### Pseudocode Or Template

```text
for i in range(1, m + 1):
    for j in range(1, n + 1):
        compare text1[i-1], text2[j-1]
```

### Complexity Notes

O(mn) time and space, often compressible to O(n).

### Interview Explanation

Rows and columns represent prefix lengths, not raw indices.

## Pattern: Knapsack Table

### Beginner Intuition

Use item index and capacity or target as the two dimensions.

### When To Use It

Use when item choices interact with a numeric limit.

### When Not To Use It

Do not reuse the same item unless the problem is unbounded.

### Recognition Signals

- items
- capacity
- target

### Example Problems

- Target Sum
- Coin Change II

### Common Mistakes

- For 0/1 knapsack on a 1-D array, iterating capacity ascending; that lets the same item appear multiple times.
- For unbounded knapsack on a 1-D array, iterating capacity descending; that misses reusing items in the same row.
- Forgetting that `dp[i][cap]` always inherits `dp[i - 1][cap]` when the item does not fit; the no-take branch is mandatory.

### Pseudocode Or Template

```text
dp[i][cap] = dp[i-1][cap]
if cap >= weight: dp[i][cap] = best(dp[i][cap], dp[i-1][cap-weight])
```

### Complexity Notes

O(n * capacity) time.

### Interview Explanation

The row means how many items have been considered.

## Pattern: Interval DP

### Beginner Intuition

Solve smaller intervals before larger intervals and try split points.

### When To Use It

Use for burst balloons, matrix-chain style costs, and palindrome intervals.

### When Not To Use It

Do not fill by start index alone if inner intervals are not ready.

### Recognition Signals

- interval
- split
- length order

### Example Problems

- Burst Balloons
- Longest Palindromic Subsequence

### Common Mistakes

- Iterating by `left` and then `right` instead of by length first; without length-first iteration, inner subproblems are not yet computed.
- For Burst Balloons, picking which balloon to burst *first* in the interval; the correct framing is to pick which balloon bursts *last* so its neighbors are the interval boundaries.
- Forgetting to pad the array with virtual `1`s on both sides for Burst Balloons; the boundary multipliers are essential.

### Pseudocode Or Template

```text
for length in range(1, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        try split points
```

### Complexity Notes

Often O(n^3) time and O(n^2) space.

### Interview Explanation

Increasing length order guarantees subinterval answers are ready.

## Pattern: Path Counting With Obstacles

### Beginner Intuition

Treat blocked states as zero ways and propagate only through valid cells.

### When To Use It

Use for grids with barriers or forbidden transitions.

### When Not To Use It

Do not add paths through invalid cells.

### Recognition Signals

- obstacle
- blocked
- count paths

### Example Problems

- Unique Paths II

### Common Mistakes

- Initializing the first row or column with `1` unconditionally; once an obstacle appears, every cell beyond it must be 0.
- Continuing to fill `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]` even when `obstacle[r][c] == 1`; gate the assignment.
- Treating the start or end cell being blocked as a valid input; both should return 0 paths.

### Pseudocode Or Template

```text
if blocked[r][c]: dp[r][c] = 0
else: dp[r][c] = top + left
```

### Complexity Notes

O(rows * cols) time.

### Interview Explanation

A blocked cell contributes zero ways to every later path.

## Pattern: State Compression

### Beginner Intuition

Keep one row or two rows when a cell only needs nearby previous-row data.

### When To Use It

Use for grid and string DP after full table is understood.

### When Not To Use It

Do not compress if reconstruction of the answer path is required.

### Recognition Signals

- rolling row
- previous row
- space

### Example Problems

- Longest Common Subsequence
- Unique Paths

### Common Mistakes

- For LCS-style recurrences, overwriting `dp[j - 1]` before reading the diagonal `dp[i - 1][j - 1]`; save it in a temporary first.
- Compressing too aggressively to a single row when the recurrence reads two rows back; some problems need a two-row alternation.
- Compressing first and validating later; always confirm correctness on the full 2-D table before reducing memory.

### Pseudocode Or Template

```text
prev_diag = 0
for j in range(1, n + 1):
    saved = dp[j]
    update dp[j]
    prev_diag = saved
```

### Complexity Notes

Same time, O(n) space.

### Interview Explanation

Compression is an optimization after the recurrence is correct.

## Pattern: Game DP

### Beginner Intuition

Store best score difference or win state for a subarray game.

### When To Use It

Use for take-from-ends games and optimal play.

### When Not To Use It

Do not greedily take the larger end without proof.

### Recognition Signals

- two players
- optimal play
- ends

### Example Problems

- Stone Game
- Predict the Winner

### Common Mistakes

- Tracking only the current player's score; the recurrence must capture the opponent's optimal counter-move via score difference.
- Iterating `[left, right]` arbitrarily; this is a length-first interval DP.
- Greedy "take the larger end" without proof; the recurrence shows greedy is wrong on adversarial inputs.

### Pseudocode Or Template

```text
dp[l][r] = max(nums[l] - dp[l+1][r], nums[r] - dp[l][r-1])
```

### Complexity Notes

O(n^2) time and space.

### Interview Explanation

Score difference naturally captures both players under optimal play.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
