# Arrays & Hashing Easy Problems

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

## 1. Two Sum

LeetCode: [Two Sum](https://leetcode.com/problems/two-sum/)

Difficulty: Easy

Pattern: Hash Lookup

Why It Matters: The canonical complement lookup problem and the first test of replacing a nested loop with memory.

Skills Tested:
- Recognize that needing two indices with `nums[i] + nums[j] == target` and one pass means storing the complement `target - nums[i]` in a hash map keyed by value.
- State the loop invariant: at index `i`, every value already in `seen` is a candidate complement for `nums[i]`, so a hit returns `[seen[target - nums[i]], i]`.
- Handle duplicate values that map to the same complement (use the first seen index), single-element arrays (no pair), and negative numbers.
- Compare the hash approach (O(n) time, O(n) space) with sort plus two pointers (O(n log n) time, O(1) extra space) and explain when index-preservation forbids sorting.

Common Follow-Ups:
- Two Sum II - Input Array Is Sorted (LC 167) and Two Sum III - Data Structure Design (LC 170) flip the trade-offs from indexed to sorted to streaming.
- 3Sum (LC 15) and 4Sum (LC 18) extend the same complement reasoning to triples and quadruples.
- Can you achieve O(1) extra space if the array can be modified or sorted in place?

## 2. Contains Duplicate

LeetCode: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Difficulty: Easy

Pattern: Hash Set Membership

Why It Matters: Builds the simplest seen-set invariant and forces a clean early exit.

Skills Tested:
- Recognize that "any value repeats" is a set membership question, not an ordering question, so the hash set holds every value scanned so far.
- State the invariant: at every index `i`, `seen` contains exactly the prior `i` values, and any hit before insert is a duplicate.
- Compare the hash approach (O(n) time, O(n) space) with sort and adjacent compare (O(n log n) time, O(1) extra space) and choose by input mutability.
- Decide whether early exit on the first duplicate is acceptable or the caller wants the duplicate value itself.

Common Follow-Ups:
- Contains Duplicate II (LC 219) bounds the duplicate to a sliding window of size `k`, which switches to a window-based hash set.
- Contains Duplicate III (LC 220) widens to value-bucket reasoning with bucket width `t`.
- What if values are very large but counts are bounded - would a Bloom filter or count-min sketch trade exact answers for memory?

## 3. Valid Anagram

LeetCode: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Difficulty: Easy

Pattern: Frequency Counting

Why It Matters: Tests whether counts, not sorting alone, can represent character multiplicity.

Skills Tested:
- Recognize that anagrams equal multisets of characters, so an array of length 26 (or a `Counter`) captures the invariant.
- State the invariant: after a single pass over `s` adding and `t` subtracting, every count is zero if and only if the strings are anagrams.
- Handle Unicode beyond ASCII (use a hash map, not a fixed array of size 26) and length mismatch as a fast reject.
- Compare counting (O(n) time, O(1) space for fixed alphabet) with sorting both strings (O(n log n) time) and explain when the alphabet bound matters.

Common Follow-Ups:
- Group Anagrams (LC 49) generalizes this canonical-key reasoning to bucketing many strings.
- Find All Anagrams in a String (LC 438) embeds anagram detection in a sliding window.
- Could you stream characters of `t` without ever materializing it?

## 4. Ransom Note

LeetCode: [Ransom Note](https://leetcode.com/problems/ransom-note/)

Difficulty: Easy

Pattern: Frequency Counting

Why It Matters: Practices decrementing inventory and detecting when a count is exhausted.

Skills Tested:
- Recognize that "letters from magazine cover ransom note" is a multiset containment check, not an order check.
- State the invariant: after counting `magazine`, every letter in `ransomNote` decrements its count, and going below zero proves insufficiency.
- Handle empty `ransomNote` (always true), case sensitivity (problem states lowercase), and very small magazines as fast rejects on length.
- Time O(n + m), space O(1) for fixed lowercase alphabet, and explain when the alphabet assumption fails.

Common Follow-Ups:
- Determine if a Ransom Note can be made from K magazines combined (sum the counts).
- What if some magazine letters are reusable (then the test reduces to a set of available letters).
- How does the answer change when letters carry weights or costs?

## 5. Majority Element

LeetCode: [Majority Element](https://leetcode.com/problems/majority-element/)

Difficulty: Easy

Pattern: Boyer-Moore Voting

Why It Matters: Introduces the idea that frequency structure can sometimes be compressed to constant space.

Skills Tested:
- Recognize that a strict majority (count > n/2) survives every cancellation by a different value, which is the Boyer-Moore key insight.
- State the invariant: after pairing one majority vote against one non-majority vote, the remaining unpaired suffix still contains the majority.
- Handle the guaranteed-majority assumption (the simple Boyer-Moore loop is enough) and the no-guarantee variant (a second pass to verify).
- Compare counting with a hash map (O(n) time, O(n) space) against Boyer-Moore (O(n) time, O(1) space).

Common Follow-Ups:
- Majority Element II (LC 229) finds all elements with count > n/3 using two candidate slots.
- What if the input is streamed and the majority might shift over time (Misra-Gries summary).
- How does randomized sampling estimate the majority with high probability?

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
