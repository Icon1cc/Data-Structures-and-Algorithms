# Graphs Hard Problems

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

## 1. Word Ladder

LeetCode: [Word Ladder](https://leetcode.com/problems/word-ladder/)

Difficulty: Hard

Pattern: BFS On Implicit Word Graph

Why It Matters: High-frequency shortest unweighted path problem.

Skills Tested:
- Recognize that one-letter transformations form an implicit graph where neighbors are words differing in exactly one position; BFS yields the shortest sequence length.
- State the invariant: distance is non-decreasing per BFS level, so the first time `endWord` is dequeued, its distance is optimal.
- Build neighbors lazily via wildcard patterns (`h*t` maps to all matching words) to avoid O(N^2) pairwise comparison.
- Time O(N * L^2) using wildcard maps, space O(N * L).

Common Follow-Ups:
- Word Ladder II (LC 126) returns all shortest sequences via BFS plus DFS reconstruction.
- Bidirectional BFS halves the explored layers.
- What if some transformations have weights.

## 2. Alien Dictionary

LeetCode: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

Difficulty: Hard

Pattern: Topological Sort From Adjacent-Word Comparisons

Why It Matters: Builds graph constraints from sorted words.

Skills Tested:
- Recognize that lexicographic order across adjacent word pairs implies a precedence edge from the first differing character of `a` to that of `b`.
- State the invariant: every directed edge represents a strict precedence; topo-sort yields a valid alphabet, while a cycle proves "no valid order".
- Detect the invalid case where `a` is longer than `b` and `b` is a prefix of `a` (return `""`).
- Time O(C) where C is the total characters across all words, space O(unique characters).

Common Follow-Ups:
- Course Schedule II (LC 210) is the underlying topo-sort primitive.
- What if multiple valid orders exist (return any).
- Generalize to a partial-order extension where the input is consistent.

## 3. Reconstruct Itinerary

LeetCode: [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

Difficulty: Hard

Pattern: Hierholzer Eulerian Path

Why It Matters: Uses lexical edge ordering and Eulerian path reasoning.

Skills Tested:
- Recognize that "use every ticket exactly once, starting at JFK, lexicographically smallest" is an Eulerian path on a multigraph with ties broken alphabetically.
- State the invariant (Hierholzer): always take the lexicographically smallest unused outgoing edge; postorder appending yields the reversed path which becomes the answer when reversed.
- Sort each adjacency list (or use a min-heap per node) to enforce lexicographic order.
- Time O(E log E), space O(V + E).

Common Follow-Ups:
- Eulerian Circuit on a directed graph (start and end at the same node).
- What if some edges may be skipped (no longer Eulerian).
- Stream edges and maintain the current itinerary online.

## 4. Making A Large Island

LeetCode: [Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

Difficulty: Hard

Pattern: Component Labeling Plus Best-Flip

Why It Matters: Combines component labeling with neighbor deduplication to evaluate a single flip.

Skills Tested:
- Recognize that the optimal flip joins up to 4 distinct neighboring components, so labeling components with unique IDs and storing their sizes lets you evaluate any flip in O(1).
- State the invariant: every land cell carries a component ID; for each water cell, the answer candidate is `1 + sum(size[id] for id in unique_neighbor_ids)`.
- Handle the all-land grid (no water cells; return `M * N`) and isolated water cells.
- Time O(M * N), space O(M * N).

Common Follow-Ups:
- Number of Islands (LC 200) is the component primitive.
- What if multiple flips are allowed (much harder, becomes connectivity-with-budget).
- Online union-find variant for incremental flips.

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
