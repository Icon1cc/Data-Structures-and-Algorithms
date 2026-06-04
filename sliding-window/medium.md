# Sliding Window Medium Problems

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

## 1. Longest Substring Without Repeating Characters

LeetCode: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Difficulty: Medium

Pattern: Variable Frequency Window

Why It Matters: The core longest-valid-substring pattern.

Skills Tested:
- Recognize that the validity predicate ("no repeats") is monotone under shrinking, so a window grows and shrinks via a count map.
- State the invariant: `count[c] <= 1` for every character in `s[left..right]`, and `right - left + 1` is the candidate length.
- Decide between counter-shrinking (decrement until the duplicate leaves) and last-index jumping (move `left` past `lastSeen[c] + 1`).
- Time O(n), space O(min(n, alphabet)), and contrast with O(n^2) brute force over every substring.

Common Follow-Ups:
- Longest Substring with At Most K Distinct Characters (LC 340) generalizes to k-distinct.
- Longest Substring with At Most Two Distinct Characters (LC 159) is the k = 2 special case.
- What changes when "no repeats" is replaced with "at most one repeat" - track second-most-recent position.

## 2. Longest Repeating Character Replacement

LeetCode: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Difficulty: Medium

Pattern: Window With Max Frequency

Why It Matters: Tests maintaining a max frequency while shrinking.

Skills Tested:
- Recognize that the validity predicate is `windowLen - maxFreq <= k`, so the window only needs to track `maxFreq` rather than recompute it.
- State the invariant: `maxFreq` is non-decreasing across the lifetime of the window because shrinking does not need to refresh it (the answer monotonically grows).
- Handle the optimization that you never shrink the window below its previous best length, only slide it forward.
- Time O(n), space O(alphabet), and contrast with the explicit-recompute variant which is O(n * alphabet).

Common Follow-Ups:
- Max Consecutive Ones III (LC 1004) is the same skeleton on a binary alphabet.
- What if `k` were also a function of the window (e.g., `k = floor(len / 2)`).
- Show how the answer length is provably the right answer even though the window state may not represent any specific valid substring at every step.

## 3. Permutation in String

LeetCode: [Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Difficulty: Medium

Pattern: Frequency Match Window

Why It Matters: Fixed-length anagram matching with counts.

Skills Tested:
- Recognize that a permutation match is exactly a frequency match over a window of length `len(s1)` in `s2`.
- State the invariant: a counter `diff` tracks how many of the 26 letters differ from the target; when `diff == 0`, a permutation occurs.
- Update `diff` by adjusting only two letters per slide step (the entering and leaving character).
- Time O(n), space O(26), and contrast with re-comparing entire counters at every shift (O(n * 26)).

Common Follow-Ups:
- Find All Anagrams in a String (LC 438) returns every match instead of just a boolean.
- What if `s1` is allowed to be missing one character and the match is approximate.
- How does the answer change for Unicode where the alphabet is unbounded.

## 4. Find All Anagrams in a String

LeetCode: [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Difficulty: Medium

Pattern: Frequency Match Window

Why It Matters: Collects every matching fixed-length window.

Skills Tested:
- Recognize that this is the all-positions variant of Permutation in String, so the same window-and-diff machinery applies.
- State the invariant: append `right` when `diff == 0`, then keep sliding to find the next match.
- Handle empty `p`, `len(p) > len(s)` (return empty), and `s` containing characters outside `a-z`.
- Time O(n + m), space O(26), and explain why prefix-sort comparison is much slower.

Common Follow-Ups:
- Substring with Concatenation of All Words (LC 30) extends to multi-word matches.
- What if `p` is a multiset of multi-character tokens, not single characters.
- How would you parallelize across many query patterns simultaneously.

## 5. Minimum Size Subarray Sum

LeetCode: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

Difficulty: Medium

Pattern: Variable Sum Window

Why It Matters: Classic shortest valid positive-sum window.

Skills Tested:
- Recognize that all values are positive, which makes the window sum monotone in length and enables a shrink-when-valid loop.
- State the invariant: while `windowSum >= target`, the current window is valid; record its length and shrink from the left.
- Handle no valid window (return 0), the entire array as a window, and very large sums without overflow.
- Time O(n), space O(1), and contrast with prefix-sum + binary search (O(n log n)) which works even with negative values.

Common Follow-Ups:
- Shortest Subarray with Sum at Least K (LC 862) breaks the monotone-sum assumption with negatives and forces a deque.
- Maximum Size Subarray Sum Equals K (LC 325) flips the predicate to equality with a hash map.
- What if the values are floats with rounding error.

## 6. Max Consecutive Ones III

LeetCode: [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

Difficulty: Medium

Pattern: At Most K Window

Why It Matters: Transforms flips into a count of invalid values.

Skills Tested:
- Recognize that "at most `k` flips" is the same as "at most `k` zeros in the window".
- State the invariant: `zeros` counts zeros in `nums[left..right]` and is kept `<= k` by advancing `left`.
- Apply the no-shrink-below-best-length trick to keep the answer length monotonically non-decreasing.
- Time O(n), space O(1), and explain how this is the same skeleton as Longest Repeating Character Replacement.

Common Follow-Ups:
- Longest Subarray of 1's After Deleting One Element (LC 1493) is the `k = 1` case with deletion.
- Maximum Consecutive Floors Without Special Floors (LC 2274) is a different framing of the same window idea.
- How does the answer change when zeros and ones cost different flip prices.

## 7. Fruit Into Baskets

LeetCode: [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

Difficulty: Medium

Pattern: At Most Two Distinct

Why It Matters: The standard at-most-k distinct window.

Skills Tested:
- Recognize that two baskets means "at most two distinct values in the window", so a count map of size at most 2 is the invariant.
- State the invariant: while the count map has more than two keys, advance `left` and decrement `count[fruits[left]]`, removing the key when it reaches zero.
- Handle uniform arrays (single distinct fruit), strictly alternating arrays, and very long runs.
- Time O(n), space O(2), and explain why this generalizes cleanly to "at most k distinct".

Common Follow-Ups:
- Longest Substring with At Most K Distinct Characters (LC 340) replaces 2 with `k`.
- Subarrays with K Different Integers (LC 992) flips at-most-k into exactly-k via two windows.
- What if baskets can hold a budget rather than a value (no longer a simple distinct-count problem).

## 8. Frequency of the Most Frequent Element

LeetCode: [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

Difficulty: Medium

Pattern: Sorted Window Cost

Why It Matters: Combines sorting with a window cost invariant.

Skills Tested:
- Recognize that after sorting, the cheapest plan is to raise every value in `[left, right]` up to `nums[right]`, costing `nums[right] * (right - left + 1) - windowSum`.
- State the invariant: `windowSum` is the sum of `nums[left..right]`, and the cost predicate `nums[right] * len - windowSum <= k` decides whether to shrink.
- Handle very large products (use 64-bit arithmetic) and the edge case where one element already satisfies the budget.
- Time O(n log n) for sort plus O(n) for the window, space O(1) extra.

Common Follow-Ups:
- Maximum Number of Visible People in a Queue (LC 1944) shares the sorted-prefix idea.
- What if you can both raise and lower values within budget (two-sided cost).
- How would you support online updates of `k`.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
