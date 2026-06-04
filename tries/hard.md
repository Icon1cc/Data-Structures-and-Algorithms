# Tries Hard Problems

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

## 1. Word Search II

LeetCode: [Word Search II](https://leetcode.com/problems/word-search-ii/)

Difficulty: Hard

Pattern: Grid DFS With Trie Pruning

Why It Matters: The classic trie plus backtracking problem.

Skills Tested:
- Recognize that running a separate DFS per word is wasteful; insert all words into a trie once and DFS the grid while descending the trie in lockstep.
- State the invariant: at each grid cell, the active trie node mirrors the path of letters chosen so far; the search prunes when no child matches.
- Mark and unmark grid cells (with a sentinel like `#`) to enforce the no-revisit constraint of the original problem.
- Time O(M * N * 4 ^ maxLen), space O(total trie nodes), and pop dead trie subtrees to keep the search tight.

Common Follow-Ups:
- Word Search (LC 79) is the single-word version.
- What if words can revisit cells but not adjacent cells.
- Generalize to a sparse graph instead of a grid.

## 2. Concatenated Words

LeetCode: [Concatenated Words](https://leetcode.com/problems/concatenated-words/)

Difficulty: Hard

Pattern: Trie Plus DP On Splits

Why It Matters: Tests reusable dictionary decomposition.

Skills Tested:
- Recognize that a word is concatenated if it can be split into two or more shorter dictionary words; this is a DP over split points using either a hash set or a trie for membership.
- State the invariant: `canForm[i]` is true if the prefix of length `i` decomposes into two or more dictionary words; transitions consider every shorter dictionary word ending at `i`.
- Sort by length to ensure each word's components were inserted before it is tested.
- Time O(N * L^2), space O(dictionary size), and contrast with brute enumeration of splits which is exponential.

Common Follow-Ups:
- Word Break II (LC 140) returns all decompositions of a single word.
- What if the dictionary is streamed and queries arrive online.
- Generalize to weighted decompositions where each word has a cost.

## 3. Palindrome Pairs

LeetCode: [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

Difficulty: Hard

Pattern: Reversed-Word Trie With Palindrome Tail

Why It Matters: Advanced string-pair matching.

Skills Tested:
- Recognize that pairs `(i, j)` form a palindrome when one word's suffix matches the other's reversed prefix and the leftover side is itself a palindrome.
- State the invariant: insert each word reversed into the trie, recording word indices and the indices of palindromic suffixes at intermediate nodes; query each word against the trie.
- Handle the empty string carefully (every palindrome can pair with it on either side).
- Time O(N * L^2), space O(N * L), and contrast with brute O(N^2 * L) pairwise checks.

Common Follow-Ups:
- Shortest Palindrome (LC 214) uses the same prefix/suffix palindrome reasoning.
- What if words can be reused.
- Online: support insertions while maintaining the pair set.

## 4. Stream of Characters

LeetCode: [Stream of Characters](https://leetcode.com/problems/stream-of-characters/)

Difficulty: Hard

Pattern: Reversed Trie Streaming Query

Why It Matters: Maintains suffix queries over a stream.

Skills Tested:
- Recognize that "does the recent suffix match any dictionary word" is naturally a reversed-word trie indexed by trailing characters.
- State the invariant: insert each word reversed into the trie; the stream buffer is walked from the most recent character backward through the trie until a dead end or a terminal.
- Cap the trie depth (and the buffer) at the longest dictionary word to stay bounded.
- Per-query time O(maxWordLen), space O(total characters across words).

Common Follow-Ups:
- Aho-Corasick automaton answers all-suffix matches in O(1) amortized per character.
- What if the stream is bidirectional or segmented.
- Generalize to wildcard matches on the suffix.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
