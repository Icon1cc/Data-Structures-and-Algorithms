# Tries Medium Problems

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

## 1. Implement Trie (Prefix Tree)

LeetCode: [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

Difficulty: Medium

Pattern: Prefix Insert And Search

Why It Matters: The required trie implementation baseline.

Skills Tested:
- Recognize that insert, search, and startsWith all share the same downward walk; only the termination condition differs.
- State the invariant: each trie node has up to 26 children plus an `isEnd` flag, and a path from the root represents the prefix accumulated so far.
- Choose between a fixed-size 26-array (fast, memory-heavy) and a dict (sparse, slower per step) and explain when each fits.
- Time O(len) per operation, space O(total characters across all words).

Common Follow-Ups:
- Implement Trie II - Prefix Tree (LC 1804) adds count and erase.
- Replace fixed-size children with a hash map for arbitrary alphabets.
- What if word frequencies must be stored alongside terminal markers.

## 2. Design Add and Search Words Data Structure

LeetCode: [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Difficulty: Medium

Pattern: Wildcard Trie DFS

Why It Matters: Adds branching search to trie basics.

Skills Tested:
- Recognize that a `.` wildcard means "try every child", which is depth-first search rather than a single descent.
- State the invariant: at each call, the matcher walks the trie from a node and a string index; on a literal, descend by character; on `.`, descend into every child.
- Prune as soon as no child path can match (returning false stops further branches).
- Time O(26 ^ wildcard_count * len) worst case, space O(len) recursion.

Common Follow-Ups:
- Word Search II (LC 212) layers trie DFS over a 2-D grid.
- What if the wildcard could match zero or more characters (regex-lite).
- How would you support deletion of a word.

## 3. Replace Words

LeetCode: [Replace Words](https://leetcode.com/problems/replace-words/)

Difficulty: Medium

Pattern: Shortest Root Prefix

Why It Matters: Uses trie prefixes to stop early.

Skills Tested:
- Recognize that "replace each word with its shortest root prefix in a dictionary" is a trie walk that stops at the first `isEnd` node.
- State the invariant: as you descend the trie following the input word, the first `isEnd` reached gives the shortest root.
- Handle the no-root case (the word stays unchanged) and root exactly equal to word.
- Time O(total characters), space O(trie nodes).

Common Follow-Ups:
- Longest Word With All Prefixes (LC 1858) is closely related but reverses the criterion.
- What if multiple roots match and you must pick the lexicographically smallest.
- Generalize to multiple dictionaries with priorities.

## 4. Map Sum Pairs

LeetCode: [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)

Difficulty: Medium

Pattern: Prefix Aggregated Trie

Why It Matters: Stores values under prefix paths.

Skills Tested:
- Recognize that `sum(prefix)` over inserted keys is a trie where each node stores the running sum of values whose key passes through it.
- State the invariant: insert updates `node.sum += delta` at every node on the path; sum is read at the prefix's terminal node.
- Handle key updates correctly: `delta = newValue - oldValue` so re-insertion does not double-count.
- Per-call time O(key length), space O(trie nodes).

Common Follow-Ups:
- Range Sum on Strings - aggregate over a substring range using a different structure.
- What if values are vectors of fixed dimension.
- How would you support deletion (subtract delta).

## 5. Search Suggestions System

LeetCode: [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

Difficulty: Medium

Pattern: Autocomplete Trie

Why It Matters: Combines prefix lookup with ranked output.

Skills Tested:
- Recognize that autocomplete requires sorting words at each trie node by lexicographic order, then capping the list at the requested limit (3 here).
- State the invariant: at each prefix length, the cached top-3 lexicographically smallest words sharing that prefix are immediately available.
- Build the trie from the sorted product list so the cached list is automatically in order.
- Time O(N log N) for sort plus O(M) per query of length `m`, space O(trie nodes).

Common Follow-Ups:
- Implement Magic Dictionary (LC 676) supports near-prefix matches with edits.
- What if the ranking is by query frequency rather than lexicographic.
- How would you support online insertion that keeps the top-3 cache valid.

## 6. Maximum XOR of Two Numbers in an Array

LeetCode: [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

Difficulty: Medium

Pattern: Bit Trie

Why It Matters: Shows tries over bits rather than characters.

Skills Tested:
- Recognize that XOR is maximized greedy bit-by-bit from the most significant bit, choosing the opposite-bit branch in the trie when possible.
- State the invariant: after inserting all numbers in the bit trie, querying with greedy opposite-bit descent yields the best partner for each input.
- Handle the case where no opposite-bit child exists (descend into the same-bit child instead).
- Time O(N * 31), space O(N * 31), and contrast with O(N^2) brute force.

Common Follow-Ups:
- Maximum XOR With an Element From Array (LC 1707) adds size constraints on partners.
- What if the bit width is much larger (256-bit IDs) or arbitrary big-integer.
- Online queries: maintain the trie as numbers stream in.

## 7. Implement Magic Dictionary

LeetCode: [Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

Difficulty: Medium

Pattern: One-Mismatch Trie Search

Why It Matters: Adds controlled branching to trie search while tracking exactly one changed character.

Skills Tested:
- Recognize that "exactly one character changed" is a trie DFS that allows one alternate-branch descent and otherwise must follow the literal path.
- State the invariant: a parameter `changed` is 0 initially and becomes 1 on the alternate descent; the search must end at an `isEnd` with `changed == 1`.
- Prune early when `changed` is already 1 and the literal child does not match.
- Time O(26 * len) per query in the worst case, space O(trie nodes).

Common Follow-Ups:
- Word Ladder (LC 127) extends to a sequence of one-edit transformations on a graph.
- What if up to `k` mismatches are allowed (parameterize `changed`).
- Generalize to insertions and deletions, not just substitutions.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
