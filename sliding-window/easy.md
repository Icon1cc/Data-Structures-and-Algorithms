# Sliding Window Easy Problems

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

## 1. Best Time to Buy and Sell Stock

LeetCode: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Difficulty: Easy

Pattern: One-pass Window Minimum

Why It Matters: Builds the idea of retaining the best left boundary.

Skills Tested:
- Recognize that "max profit from one buy and one later sell" is the running difference between today's price and the minimum price seen so far.
- State the invariant: at index `i`, `minSoFar` is the smallest price in `prices[0..i]` and `best = max(best, prices[i] - minSoFar)`.
- Handle strictly decreasing prices (return 0), single-day arrays, and large numbers without overflow.
- Time O(n), space O(1), and contrast with O(n^2) brute force over every buy-sell pair.

Common Follow-Ups:
- Best Time to Buy and Sell Stock II (LC 122) allows multiple transactions and reduces to summing positive day differences.
- Best Time to Buy and Sell Stock with Cooldown (LC 309) and With Transaction Fee (LC 714) push the problem into DP.
- What changes if you must report the buy day and sell day, not just the profit.

## 2. Contains Duplicate II

LeetCode: [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

Difficulty: Easy

Pattern: Fixed Distance Window

Why It Matters: Tests membership within a moving index range.

Skills Tested:
- Recognize that "duplicate within distance `k`" is a sliding window of size `k + 1` over a hash set.
- State the invariant: `seen` always equals `set(nums[max(0, i - k) .. i])`, so a hit on `nums[i]` proves a near-duplicate.
- Evict `nums[i - k - 1]` from the set when the window grows past `k`.
- Time O(n), space O(min(n, k)), and explain why pure Contains Duplicate (no `k`) is a degenerate case.

Common Follow-Ups:
- Contains Duplicate III (LC 220) replaces equality with a value-bucket of width `t`.
- Continuous Subarray Sum (LC 523) layers prefix-sum-mod logic on top of the same window idea.
- What if values are very large but counts are bounded - bloom filter trade-off.

## 3. Maximum Average Subarray I

LeetCode: [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

Difficulty: Easy

Pattern: Fixed Window Sum

Why It Matters: The baseline fixed-size window problem.

Skills Tested:
- Recognize that a fixed window of length `k` keeps a rolling sum updated by `+ nums[right] - nums[right - k]`.
- State the invariant: `windowSum` always equals `sum(nums[right - k + 1 .. right])` once `right >= k - 1`.
- Skip the divide-by-`k` until the very end and compare sums (or compare averages directly with floating point care).
- Time O(n), space O(1), and contrast with the prefix-sum variant which costs O(n) extra memory.

Common Follow-Ups:
- Maximum Sum of Distinct Subarrays With Length K (LC 2461) adds a uniqueness constraint inside the window.
- Maximum Average Subarray II (LC 644) generalizes to variable length with binary search on average.
- How does the answer change when `k > len(nums)` (problem boundary).

## 4. Longest Harmonious Subsequence

LeetCode: [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/)

Difficulty: Easy

Pattern: Frequency Range Window

Why It Matters: Uses counts over adjacent values after grouping.

Skills Tested:
- Recognize that a harmonious subsequence has `max - min == 1`, so for every value `v` in the count map the candidate length is `count[v] + count[v + 1]`.
- State the invariant: the answer is the maximum of `count[v] + count[v + 1]` across all `v` where both keys exist.
- Handle isolated values (no neighbor by 1, contribute zero), repeated values, and very large negative values via dict not array.
- Time O(n), space O(n), and explain why subsequence (not subarray) lets us ignore order.

Common Follow-Ups:
- Subarray with `max - min == k` extends to a sliding window with min-deque and max-deque.
- What if order matters and only contiguous subsequences count.
- How to support online updates of the multiset.

## 5. Minimum Recolors to Get K Consecutive Black Blocks

LeetCode: [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)

Difficulty: Easy

Pattern: Fixed Window Count

Why It Matters: Small fixed-window problem with direct state update.

Skills Tested:
- Recognize that recolors needed for a window of length `k` is `k - (number of B in the window)`, so minimize `whiteCount` over fixed-size windows.
- State the invariant: rolling `whiteCount` always equals the count of `W` in the current `k`-length window.
- Update by `+ (blocks[right] == 'W')` and `- (blocks[right - k] == 'W')` once the window is full.
- Time O(n), space O(1), and explain why a brute pass over every window costs O(n * k).

Common Follow-Ups:
- Maximum Number of Vowels in a Substring of Given Length (LC 1456) is the same skeleton over vowel counts.
- What if `k` itself is a query parameter that changes online (segment tree or sparse table).
- How does the answer change if you can also delete blocks.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
