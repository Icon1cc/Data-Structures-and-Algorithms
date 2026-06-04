# Advanced Graphs Easy Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.
- Genuine Easy problems exercising advanced graph algorithms (Dijkstra, MST, topological sort, low-link DFS) are rare on LeetCode, so this file is intentionally smaller; depth lives in `medium.md` and `hard.md`.

## Practice Order

- First pass: solve in the listed Easy order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Find the Town Judge

LeetCode: [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

Difficulty: Easy

Pattern: In-degree And Out-degree Balance

Why It Matters: Degree accounting before heavier graph algorithms.

Skills Tested:
- Recognize that "the judge trusts no one and is trusted by everyone else" is captured by `outDegree[judge] == 0` and `inDegree[judge] == n - 1`.
- State the invariant: a single pass over `trust` increments `outDegree[a]` and `inDegree[b]`; the judge is the unique node with `inDegree - outDegree == n - 1`.
- Handle `n == 1` (the only person is the judge) and a missing trust edge (no judge exists).
- Time O(N + E), space O(N), and contrast with full graph traversal which is unnecessary here.

Common Follow-Ups:
- Find Center of Star Graph (LC 1791) reuses the pure-degree idea on undirected graphs.
- What if multiple judges or no judge can exist (return all or `-1`).
- Generalize to weighted-trust networks where degree is a sum of weights.

## 2. Destination City

LeetCode: [Destination City](https://leetcode.com/problems/destination-city/)

Difficulty: Easy

Pattern: Directed Sink Detection

Why It Matters: Builds intuition for sink nodes and missing outgoing edges in a directed graph.

Skills Tested:
- Recognize that the destination city is the unique node that never appears as a source in any path edge.
- State the invariant: build a set of source cities; the answer is the unique destination not in that set.
- Handle the linear-path constraint: there is exactly one such node by problem guarantee.
- Time O(N), space O(N), and explain why a full DAG traversal is overkill.

Common Follow-Ups:
- Generalize to find all sinks in a DAG (out-degree zero).
- What if the path can branch (now the answer is not unique).
- How would you detect cycles before declaring a destination.

## 3. Find Champion I

LeetCode: [Find Champion I](https://leetcode.com/problems/find-champion-i/)

Difficulty: Easy

Pattern: Zero In-degree Champion

Why It Matters: Practices tournament-style graph reasoning with a unique candidate condition.

Skills Tested:
- Recognize that the champion is the unique team that loses to no one, which is the node with in-degree zero in the directed beats-graph.
- State the invariant: the answer exists iff exactly one node has in-degree zero; otherwise the result is `-1`.
- Compute in-degrees in a single pass over the adjacency matrix.
- Time O(N^2), space O(N), and contrast with traversal-based approaches.

Common Follow-Ups:
- Find Champion II (LC 2924) lifts the constraint to a general graph and forces a uniqueness check.
- What if cycles exist (no unique champion).
- Generalize to ranking the top-k under a tournament.

---

## Navigation

[Previous](PATTERNS.md) | [Home](../README.md) | [Next](medium.md)
