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

Pattern: BFS Shortest Transformation

Why It Matters: High-frequency shortest unweighted path problem.

Skills Tested:
- Identify the BFS Shortest Transformation signal before choosing a template.
- State the invariant for Word Ladder: high-frequency shortest unweighted path problem.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Word Ladder toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the BFS Shortest Transformation invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Alien Dictionary

LeetCode: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

Difficulty: Hard

Pattern: Topological Sort

Why It Matters: Builds graph constraints from sorted words.

Skills Tested:
- Identify the Topological Sort signal before choosing a template.
- State the invariant for Alien Dictionary: builds graph constraints from sorted words.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Alien Dictionary toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Topological Sort invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Reconstruct Itinerary

LeetCode: [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

Difficulty: Hard

Pattern: Hierholzer DFS

Why It Matters: Uses lexical edge ordering and Eulerian path reasoning.

Skills Tested:
- Identify the Hierholzer DFS signal before choosing a template.
- State the invariant for Reconstruct Itinerary: uses lexical edge ordering and Eulerian path reasoning.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Reconstruct Itinerary toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Hierholzer DFS invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. Making A Large Island

LeetCode: [Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

Difficulty: Hard

Pattern: Grid Components With Relabeling

Why It Matters: Combines component labeling with neighbor deduplication to evaluate a single flip.

Skills Tested:
- Identify the Grid Components With Relabeling signal before choosing a template.
- State the invariant for Making A Large Island: combines component labeling with neighbor deduplication to evaluate a single flip.
- Handle disconnected components, cycles, duplicate enqueues, and directed versus undirected edges.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Making A Large Island toward Union Find, topological sort, Dijkstra, dynamic programming, or backtracking?
- Which disconnected components case would break the first implementation?
- Can the Grid Components With Relabeling invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](medium.md) | [Home](../README.md) | [Next](../REPO_INDEX.md)
