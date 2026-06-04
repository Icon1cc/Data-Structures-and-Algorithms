# Sliding Window Hard Problems

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

## 1. Minimum Window Substring

LeetCode: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

Difficulty: Hard

Pattern: Frequency Window With Match Counter

Why It Matters: The most important hard sliding-window problem.

Skills Tested:
- Recognize that "smallest window of `s` covering all characters of `t`" is a shrink-while-valid window with a need-counter `have == required`.
- State the invariant: `have` equals the number of distinct characters whose count meets `t`'s requirement, and the window is valid only when `have == required`.
- Update `have` by exactly one increment or decrement per slide step (when `count[c]` crosses the target threshold).
- Time O(n + m), space O(alphabet), and explain why naive substring enumeration is O(n^3).

Common Follow-Ups:
- Smallest Window Containing All Characters of Another String II returns the substring rather than just length.
- What if `t` allows repeated characters with different multiplicities (already handled by counters, walk through it).
- How would you support online queries where `t` arrives one character at a time.

## 2. Sliding Window Maximum

LeetCode: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

Difficulty: Hard

Pattern: Monotonic Deque

Why It Matters: Uses a deque to keep maximum candidates.

Skills Tested:
- Recognize that the maximum of every length-`k` window is maintained by a deque of indices whose values are strictly decreasing.
- State the invariant: the front of the deque is the index of the maximum in the current window, and any element that becomes obsolete (out of the window or smaller than a new entry) is popped.
- Pop from the back while `nums[back] <= nums[i]` and from the front while `front <= i - k`.
- Time O(n), space O(k), and contrast with a heap which is O(n log k) and harder to evict expired entries.

Common Follow-Ups:
- Constrained Subsequence Sum (LC 1425) layers DP on top of a monotonic-deque maximum.
- What if you also need the minimum at the same time (two deques).
- How does the answer change when `k` itself slides.

## 3. Substring with Concatenation of All Words

LeetCode: [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

Difficulty: Hard

Pattern: Aligned Block Window

Why It Matters: Maintains word counts over aligned chunks.

Skills Tested:
- Recognize that words have equal length `L`, so the search space splits into `L` independent block-aligned windows starting at offsets `0..L-1`.
- State the invariant: at each offset, a count map tracks the word frequency in the current `len(words) * L` block, and the block is valid when the map equals `Counter(words)`.
- Slide block-by-block within an offset, evicting the leftmost word and admitting the rightmost word.
- Time O(n * L), space O(unique words), and contrast with the brute O(n * len(words) * L) check.

Common Follow-Ups:
- Find All Anagrams in a String (LC 438) is the single-character version.
- What if word lengths are not all equal (much harder, falls back to suffix automaton style).
- How would you precompute hashes per block to compare in O(1) per slide.

## 4. Subarrays with K Different Integers

LeetCode: [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

Difficulty: Hard

Pattern: Exactly K Via At Most K Minus At Most K Minus One

Why It Matters: Turns an exactly-k requirement into two monotonic sliding-window counts.

Skills Tested:
- Recognize that `exactly K = atMostK - atMostKMinusOne` because exactly-K is not directly monotone but at-most-K is.
- State the invariant: `atMost(K)` counts subarrays with at most K distinct using a window plus distinct counter; the difference yields the exact answer.
- Implement `atMost(K)` cleanly so calling it twice with different K values stays O(n) each.
- Time O(n), space O(K), and explain why a single-pass exactly-K is harder to maintain.

Common Follow-Ups:
- Count Number of Nice Subarrays (LC 1248) reuses the at-most-K trick on binary parity.
- Replace the count of subarrays with the count of distinct subarrays.
- What if the constraint is "exactly K" but order matters as a sequence rather than a contiguous subarray.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
