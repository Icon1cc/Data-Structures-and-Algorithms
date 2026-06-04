# Tries Easy Problems

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

## 1. Longest Common Prefix

LeetCode: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Difficulty: Easy

Pattern: Prefix Scan Or Trie

Why It Matters: Introduces shared-prefix reasoning before full trie design.

Skills Tested:
- Recognize that a vertical scan over the strings or a trie with a single child path both compute the longest common prefix.
- State the invariant: at column `c`, every input string has the same character; the answer extends through the rightmost such `c`.
- Handle empty input list (return ""), an empty string in the list (return ""), and a single-string list (return the string).
- Time O(N * len), space O(1) for the vertical scan, and contrast with the trie approach which is O(N * len) build but supports prefix queries afterward.

Common Follow-Ups:
- Add Strings (LC 415) shares the column-scan style on numeric strings.
- What if the input is streamed and you must answer prefix length online (a trie shines here).
- How does the answer change for "longest common suffix".

## 2. Unique Morse Code Words

LeetCode: [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)

Difficulty: Easy

Pattern: Canonical Encoding Set

Why It Matters: Practices string-to-key mapping used by trie-like grouping.

Skills Tested:
- Recognize that mapping each word to its concatenated Morse string and counting distinct results is the same canonical-key idea trie nodes encode at terminal.
- State the invariant: every word maps to one Morse encoding, and equality is decided on the encoding.
- Handle the alphabet table indexing (`ord(ch) - ord('a')`), uppercase input rejection, and empty words.
- Time O(total characters), space O(unique encodings), and explain why a trie would store the same encodings.

Common Follow-Ups:
- Group Anagrams (LC 49) extends canonical-key grouping to anagram equivalence.
- What if the alphabet uses prefix-free codes versus fixed-length codes (decoding ambiguity).
- How does the answer change if Morse codes are user-supplied per dictionary.

## 3. Verifying an Alien Dictionary

LeetCode: [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)

Difficulty: Easy

Pattern: Custom Order Prefix Compare

Why It Matters: Tests prefix rules and lexicographic constraints.

Skills Tested:
- Recognize that lexicographic ordering with a custom alphabet reduces to comparing each adjacent pair under a `rank[ch]` map.
- State the invariant: a word `a` precedes `b` only if at the first differing position `rank[a[i]] < rank[b[i]]`, or `a` is a prefix of `b`.
- Handle the prefix special case (`abc` before `abcd` is valid, `abcd` before `abc` is not).
- Time O(total characters), space O(26), and contrast with sorting (overkill for a yes/no validation).

Common Follow-Ups:
- Alien Dictionary (LC 269) reverses the question and infers the order via topological sort.
- What if the alphabet has more than 26 characters or repeated rank ties.
- How would you support online insertion of a new word.

## 4. Longest Word in Dictionary

LeetCode: [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

Difficulty: Easy

Pattern: Trie Traversal With Prefix Existence

Why It Matters: Reinforces the trie's prefix-existence query as a tool for incremental word building.

Skills Tested:
- Recognize that a word is "buildable" only if every one of its prefixes is also a dictionary entry, which is exactly a trie path with end-of-word markers along the way.
- State the invariant: a DFS over the trie only descends into children whose `isEnd` is true; the deepest such path yields the longest buildable word.
- Break ties by lexicographic order (visit children in alphabetical order, keep the deepest first answer).
- Time O(total characters), space O(trie nodes), and contrast with sort-by-length-then-set which is O(N log N).

Common Follow-Ups:
- Longest Word With All Prefixes (LC 1858) is the same problem with a different framing.
- What if some intermediate prefixes can be inferred (autocomplete dictionaries).
- How does the answer change with a max-length cap.

## 5. Find Words That Can Be Formed by Characters

LeetCode: [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)

Difficulty: Easy

Pattern: Frequency Subset Match

Why It Matters: Pairs trie-style alphabet tables with multiset containment, the same accounting tries use at terminal nodes.

Skills Tested:
- Recognize that "can `word` be built from `chars`" is multiset containment over the alphabet, the same comparison a trie uses when storing per-node counts.
- State the invariant: for every letter `c`, `count_word[c] <= count_chars[c]`; one violation rejects the word.
- Handle the empty word (always buildable, length 0) and characters outside `a-z` (state the assumption).
- Time O(total characters), space O(26), and explain how a trie with per-node counts would answer the same question via path traversal.

Common Follow-Ups:
- Ransom Note (LC 383) is the same multiset containment on a single pair.
- Group Anagrams (LC 49) reuses count-tuple keys.
- What if some letters can be substituted by jokers (wildcards in the trie).

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
