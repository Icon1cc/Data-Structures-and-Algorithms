# Greedy Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Assign Cookies

LeetCode: [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

Difficulty: Easy

Pattern: Sort Both And Two Pointers

Why It Matters: Baseline matching with smallest sufficient resource.

Skills Tested:
- Recognize that the maximum content children is achieved by giving each child the smallest cookie that satisfies them, which is two sorted arrays advanced together.
- State the invariant: pointer `i` over children and `j` over cookies; advance `j` until `cookie[j] >= child[i]`, satisfy that child, advance both.
- Handle empty children (return 0) and empty cookies (return 0).
- Time O(n log n), space O(1) extra, and explain why the matching is provably optimal (exchange argument).

Common Follow-Ups:
- Boats to Save People (LC 881) extends two-pointer matching with weight constraints.
- What if children have priorities (weighted matching).
- Generalize to bipartite matching.

## 2. Lemonade Change

LeetCode: [Lemonade Change](https://leetcode.com/problems/lemonade-change/)

Difficulty: Easy

Pattern: Greedy Cash Handling

Why It Matters: Tests local bill choices with limited denominations.

Skills Tested:
- Recognize that to give change for a $20, you should hand back a $10 + $5 if available, else three $5s; for a $10, hand back a $5.
- State the invariant: prefer larger bills first when giving change so smaller bills remain for future $10 customers.
- Maintain only `fives` and `tens` counters; track $20s implicitly (they cannot be returned anyway).
- Time O(n), space O(1), and explain why the greedy is optimal via an exchange argument.

Common Follow-Ups:
- Coin Change (LC 322) is the general DP version; greedy fails on non-canonical coin sets.
- What if customers can give multiple bills.
- Generalize to currencies where greedy is not optimal.

## 3. Best Time to Buy and Sell Stock II

LeetCode: [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Difficulty: Easy

Pattern: Sum Of Positive Differences

Why It Matters: Adds every positive price difference.

Skills Tested:
- Recognize that with unlimited transactions, the maximum profit is the sum of every positive day-over-day price difference.
- State the invariant: each ascending segment contributes `prices[end] - prices[start]`, which equals the sum of positive deltas inside.
- Avoid the trap of trying to find local minima and maxima; the sum-of-deltas form is equivalent and simpler.
- Time O(n), space O(1).

Common Follow-Ups:
- Best Time to Buy and Sell Stock (LC 121) restricts to one transaction.
- Best Time to Buy and Sell Stock with Cooldown (LC 309) and With Fee (LC 714) require DP.
- What if you must keep the trade count under K (LC 188).

## 4. Can Place Flowers

LeetCode: [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

Difficulty: Easy

Pattern: Local Feasibility Greedy

Why It Matters: Checks safe placements without backtracking.

Skills Tested:
- Recognize that planting at position `i` is safe iff `flowerbed[i] == 0`, `flowerbed[i - 1] == 0` (or `i == 0`), and `flowerbed[i + 1] == 0` (or `i == n - 1`).
- State the invariant: greedily plant whenever safe; this never blocks a future safe planting.
- Pad the array conceptually with zeros at both ends to simplify boundary checks.
- Time O(n), space O(1), and explain why local greedy is provably optimal.

Common Follow-Ups:
- Generalize to "no two flowers within distance `k`".
- What if some cells must remain empty.
- Streaming variant where positions arrive online.

## 5. Maximum Odd Binary Number

LeetCode: [Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number/)

Difficulty: Easy

Pattern: Bit Placement Greedy

Why It Matters: Places bits to maximize value under parity constraint.

Skills Tested:
- Recognize that an odd binary number has its last bit `1`, and the value is maximized by placing all other `1`s at the leftmost positions.
- State the invariant: count `1`s as `k`; place `k - 1` ones at the front, then `n - k` zeros, then the final `1`.
- Handle the edge case where `s` has only one `1` (the answer is `0...01`).
- Time O(n), space O(n) for the output string.

Common Follow-Ups:
- Largest Number (LC 179) generalizes to a custom comparator over digits.
- What if you may also flip bits within budget.
- Maximize the value under a "no two 1s adjacent" constraint.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
