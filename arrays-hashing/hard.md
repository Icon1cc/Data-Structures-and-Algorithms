# Arrays & Hashing Hard Problems

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

## 1. First Missing Positive

LeetCode: [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

Difficulty: Hard

Pattern: In-place Index Marking

Why It Matters: Classic constant-space array indexing problem with difficult boundary handling.

Skills Tested:
- Recognize that the answer must lie in `[1, n + 1]`, which means the array can serve as its own hash table by sending value `v` to index `v - 1`.
- State the invariant: after the placement pass, `nums[i] == i + 1` whenever `i + 1` is present, so the first index that fails this check is the answer.
- Handle non-positive values, values larger than `n`, and duplicates so the placement loop terminates without cycles.
- Achieve O(n) time, O(1) extra space, and explain why hash-set or sort approaches violate the constraint.

Common Follow-Ups:
- Find All Numbers Disappeared in an Array (LC 448) and Find All Duplicates in an Array (LC 442) reuse in-place index marking.
- What if the array is read-only - how does that force O(n) extra space.
- How does the technique extend when values can be very large but the range of valid answers is still small.

## 2. Longest Duplicate Substring

LeetCode: [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

Difficulty: Hard

Pattern: Rolling Hash With Binary Search

Why It Matters: Combines hashing, collision awareness, and answer search over substring length.

Skills Tested:
- Recognize that "longest substring that occurs at least twice" has a monotone predicate over length, so binary search the length and a rolling hash answers each predicate.
- State the invariant: for each candidate length `L`, the rolling hash over every length-`L` window collides if a duplicate of length `L` exists.
- Handle hash collisions by storing the actual substring at each hashed window or using double hashing to drive the false-positive rate down.
- Time O(n log n) average via binary search and rolling hash, with explicit reasoning on the chosen modulus and base.

Common Follow-Ups:
- Repeated DNA Sequences (LC 187) uses rolling hash without binary search.
- Replace the rolling hash with a suffix array or suffix automaton for guaranteed worst-case time.
- How would you find the longest substring repeated at least `k` times?

## 3. Count of Smaller Numbers After Self

LeetCode: [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

Difficulty: Hard

Pattern: Ordered Counting

Why It Matters: Forces prefix-style counting with an ordered structure rather than plain hashing.

Skills Tested:
- Recognize that "for each `i`, count `j > i` with `nums[j] < nums[i]`" is an inversion-count style query that needs an order-preserving counter.
- State the invariant: scanning right to left, a Fenwick tree indexed by rank stores how many already-seen elements are smaller than each new value.
- Handle large value ranges via coordinate compression and ties (count strictly smaller, not less-or-equal).
- Time O(n log n), space O(n), and compare Fenwick tree to merge-sort-with-count.

Common Follow-Ups:
- Reverse Pairs (LC 493) extends the predicate to `nums[i] > 2 * nums[j]`.
- Count of Range Sum (LC 327) replaces values with prefix sums.
- What if the input is streamed and queries arrive online (order-statistic tree).

## 4. Count of Range Sum

LeetCode: [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

Difficulty: Hard

Pattern: Prefix Sum With Ordered Counting

Why It Matters: Advanced prefix reasoning where counting prior prefixes requires ordered structure.

Skills Tested:
- Recognize that the count of subarrays with sum in `[lower, upper]` becomes "for each prefix `P[j]`, count earlier prefixes `P[i]` with `P[j] - upper <= P[i] <= P[j] - lower`".
- State the invariant: a balanced BST or merge-sort-with-count over the prefix array gives the running count of qualifying earlier prefixes.
- Handle 64-bit prefix overflow (use `long long`), negative values, and duplicate prefix sums (count each one).
- Time O(n log n), space O(n), and explain why a plain hash map fails because the predicate is range-based, not equality-based.

Common Follow-Ups:
- Reverse Pairs (LC 493) and Count of Smaller Numbers After Self (LC 315) share the same merge-sort scaffold.
- What if `lower` and `upper` change per query (offline sweep with Fenwick tree).
- How would you parallelize the merge-sort-with-count across cores.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
