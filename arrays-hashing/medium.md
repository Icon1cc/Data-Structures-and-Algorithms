# Arrays & Hashing Medium Problems

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

## 1. Group Anagrams

LeetCode: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Difficulty: Medium

Pattern: Grouping by Canonical Key

Why It Matters: Turns equivalence into a key and is a core hashmap grouping interview pattern.

Skills Tested:
- Recognize that grouping by anagram equivalence reduces to choosing a canonical key per string (sorted letters, or a 26-length count tuple).
- State the invariant: every string maps to one bucket, and every bucket holds exactly the strings sharing its canonical key.
- Handle empty strings (key is `""`), Unicode (the count-tuple key fails for arbitrary alphabets, switch to a sorted string), and tie-broken output order.
- Compare sorted-key (O(n * k log k)) with count-tuple (O(n * k)) when `k` is the average word length and the alphabet is fixed.

Common Follow-Ups:
- Group Shifted Strings (LC 249) uses a canonical key built from pairwise differences.
- Find All Anagrams in a String (LC 438) layers anagram bucketing on top of a sliding window.
- How would a streaming version that returns groups incrementally change the data structures?

## 2. Contiguous Array

LeetCode: [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

Difficulty: Medium

Pattern: Prefix Sum Balance

Why It Matters: Converts equal 0/1 counts into repeated prefix states and tests balance reasoning.

Skills Tested:
- Recognize that mapping 0 to -1 turns "equal zeros and ones in `[i, j]`" into "prefix sum at `j` equals prefix sum at `i - 1`".
- State the invariant: the first index where each prefix-sum value appeared yields the longest balanced subarray ending later.
- Handle the empty prefix (store `prefix = 0` at index `-1`), all zeros, and all ones (no balanced window).
- Time O(n), space O(n), and explain why a hash map of first-occurrence is necessary even though the answer is just a length.

Common Follow-Ups:
- Subarray Sum Equals K (LC 560) replaces the +1/-1 trick with general counts of prefix-sum frequencies.
- Find the Longest Substring Containing Vowels in Even Counts (LC 1371) extends the trick to a bitmask of parities.
- What if the problem asked for the count of all balanced subarrays rather than the longest one?

## 3. Product of Array Except Self

LeetCode: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Difficulty: Medium

Pattern: Prefix And Suffix Products

Why It Matters: Forces left/right accumulated state and careful zero handling.

Skills Tested:
- Recognize that the constraint "no division" rules out total-product divided by `nums[i]` and pushes you toward two passes that accumulate from each side.
- State the invariant: after the left pass, `out[i] = product of nums[0..i-1]`; after the right pass, `out[i] *= product of nums[i+1..n-1]`.
- Handle zero values (one zero makes only that index nonzero, two zeros make every index zero) without conditional branches.
- Achieve O(1) extra space (use the output array, then a running suffix scalar) versus the naive O(n) extra arrays.

Common Follow-Ups:
- Product of Array Except Self II variants restrict to ranges or windows.
- Maximum Product Subarray (LC 152) replaces the structural product with a contiguous-window product DP.
- What if a small number of single-index updates arrive online (segment tree or Fenwick-tree-with-product).

## 4. Encode and Decode Strings

LeetCode: [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

Difficulty: Medium

Pattern: Length Prefix Encoding

Why It Matters: Teaches delimiter-safe serialization and edge cases around empty strings.

Skills Tested:
- Recognize that any reserved delimiter can appear inside a string, so a length prefix (e.g., `"5#hello"`) avoids ambiguity by construction.
- State the invariant: at decode time, reading digits up to `#` gives the next chunk length, then the next `len` characters are the next string.
- Handle empty strings (encoded as `"0#"`), strings containing digits and `#`, and very long strings without integer overflow.
- Compare length-prefix with escape-character schemes and explain why escaping is harder to verify by inspection.

Common Follow-Ups:
- Serialize and Deserialize Binary Tree (LC 297) uses the same idea against a tree shape with null markers.
- Design a streaming decoder that emits each string as soon as its length prefix is satisfied.
- How would you make the encoding self-synchronizing if a chunk of bytes is dropped?

## 5. Longest Consecutive Sequence

LeetCode: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

Difficulty: Medium

Pattern: Hash Set Boundary Scan

Why It Matters: Shows how to start work only at sequence boundaries to stay linear.

Skills Tested:
- Recognize that the linear bound holds only when each value is the start of its run, which requires checking `value - 1` not in the set before extending.
- State the invariant: every value belongs to exactly one run, and only the smallest member of a run is allowed to grow it.
- Handle duplicates (drop into a set first), negative numbers (the set is value-keyed), and a single value (run length 1).
- Reach O(n) average time despite the inner while loop, and explain why naive sort solutions are O(n log n).

Common Follow-Ups:
- Binary Tree Longest Consecutive Sequence (LC 298) reuses the run idea on a tree structure.
- What if the array is streamed - how do you maintain the longest run online (union-find by value).
- How does the answer change when the values are bounded so a boolean array replaces the hash set?

## 6. Subarray Sum Equals K

LeetCode: [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Difficulty: Medium

Pattern: Prefix Sum With Counts

Why It Matters: A high-frequency prefix-sum problem, especially important with negative numbers.

Skills Tested:
- Recognize that "count subarrays summing to `k`" is exactly counting pairs of prefixes with difference `k`, so a hash map of prefix-sum counts solves it in one pass.
- State the invariant: at each `i`, `count += freq[prefix - k]`, then bump `freq[prefix]` for future indices.
- Handle negative values (sliding window fails here, that is why prefix-count is needed) and the empty prefix (seed `freq[0] = 1`).
- Time O(n), space O(n), and explain why the simpler two-pointer approach breaks once values can be negative.

Common Follow-Ups:
- Continuous Subarray Sum (LC 523) and Subarray Sums Divisible by K (LC 974) reuse prefix-sum-with-counts modulo `k`.
- Find longest subarray with sum exactly `k` (LC 325) replaces counts with first-occurrence indices.
- How would you support point updates and range-sum-equals-K queries (Fenwick tree of value frequencies).

## 7. Valid Sudoku

LeetCode: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

Difficulty: Medium

Pattern: Set Membership By Region

Why It Matters: Practices mapping rows, columns, and boxes to constraint sets.

Skills Tested:
- Recognize that a Sudoku validity check has nine row sets, nine column sets, and nine 3x3 box sets, all of which must remain disjoint of repeats.
- State the invariant: insertion of `board[r][c]` into row `r`, column `c`, and box `(r // 3, c // 3)` succeeds for every filled cell.
- Handle `.` entries (skip them), large alphabets (only digits 1-9 are valid), and partial boards (no need to fill, only validate).
- Time O(81), space O(81) - explain why constants are tiny and what changes for an N x N board.

Common Follow-Ups:
- Sudoku Solver (LC 37) layers backtracking on top of this validity check.
- Validate a partially filled Latin Square (rows and columns only).
- How would you parallelize the row, column, and box checks across nine threads?

## 8. Insert Delete GetRandom O(1)

LeetCode: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Difficulty: Medium

Pattern: Array Plus Hash Map

Why It Matters: Combines indexed storage with direct lookup and swap-delete mutation.

Skills Tested:
- Recognize that random access in O(1) requires a contiguous array, while O(1) delete requires swap-with-last and a hash map from value to its array index.
- State the invariant: after every operation, `arr[idx[v]] == v` for every present `v`, and `len(arr) == len(idx)`.
- Handle deleting the last element (no swap needed), inserting an existing value (return `false`), and getRandom on an empty container (problem assumption).
- Total memory O(n) plus understanding that random selection uses `random.choice(arr)` for O(1).

Common Follow-Ups:
- Insert Delete GetRandom O(1) - Duplicates allowed (LC 381) replaces `idx` with a set of indices per value.
- Design a structure with weighted random sampling (Fenwick tree of weights).
- What happens if delete must preserve insertion order (linked list with hash map of node references).

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
