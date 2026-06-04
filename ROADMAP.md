# Roadmap

Use this roadmap to learn topics in an order that builds prerequisites before advanced pattern recognition.

## Learning Phases

| Phase | Topics | Expected Outcome |
|---|---|---|
| Foundation | arrays-hashing, two-pointers, stack, binary-search, sliding-window | Loop invariants, lookup, boundaries, nested structure, and contiguous ranges. |
| Pointer And Recursion Fluency | linked-list, trees, tries, heap-priority-queue | Reference mutation, traversal contracts, prefix storage, and priority retrieval. |
| Search And Connectivity | backtracking, graphs, advanced-graphs | Decision trees, reachability, shortest paths, dependencies, and weighted algorithms. |
| Optimization | 1d-dp, 2d-dp, greedy, intervals | State definition, transitions, proof of local choices, and ordered ranges. |
| Low-Level And Numeric | bit-manipulation, math-geometry | Binary representation, modular reasoning, matrix movement, and geometry invariants. |

## Topic Order

| Order | Topic | Prerequisite | Outcome |
|---:|---|---|---|
| 1 | [Arrays & Hashing](arrays-hashing/README.md) | None | Build direct lookup, counting, grouping, and prefix summaries over indexed data. |
| 2 | [Two Pointers](two-pointers/README.md) | Arrays & Hashing | Move one or two indices through linear data while preserving a clear relationship between them. |
| 3 | [Stack](stack/README.md) | Two Pointers | Use last-in-first-out state to model nested structure, undo decisions, and nearest greater or smaller elements. |
| 4 | [Binary Search](binary-search/README.md) | Stack | Halve a sorted or monotonic search space until the target or boundary is isolated. |
| 5 | [Sliding Window](sliding-window/README.md) | Binary Search | Maintain a contiguous range while expanding and shrinking it under an invariant. |
| 6 | [Linked List](linked-list/README.md) | Sliding Window | Manipulate node references safely when random access is unavailable. |
| 7 | [Trees](trees/README.md) | Linked List | Reason over hierarchical structures with recursion, traversal order, and subtree return values. |
| 8 | [Tries](tries/README.md) | Trees | Store strings by shared prefixes so prefix queries and dictionary pruning become efficient. |
| 9 | [Heap / Priority Queue](heap-priority-queue/README.md) | Tries | Repeatedly retrieve the smallest or largest active item without fully sorting every time. |
| 10 | [Backtracking](backtracking/README.md) | Heap / Priority Queue | Explore a decision tree by choosing, recursing, and undoing choices under constraints. |
| 11 | [Graphs](graphs/README.md) | Backtracking | Model relationships as nodes and edges, then traverse or group them safely. |
| 12 | [Advanced Graphs](advanced-graphs/README.md) | Graphs | Choose specialized graph algorithms for weighted paths, all-pairs paths, connectivity structure, and spanning trees. |
| 13 | [1-D Dynamic Programming](1d-dp/README.md) | Advanced Graphs | Define a one-dimensional state so overlapping subproblems are solved once. |
| 14 | [2-D Dynamic Programming](2d-dp/README.md) | 1-D Dynamic Programming | Use a table whose state depends on two indices, dimensions, strings, or interval boundaries. |
| 15 | [Greedy](greedy/README.md) | 2-D Dynamic Programming | Make locally optimal choices only when an exchange argument or invariant proves they remain globally safe. |
| 16 | [Intervals](intervals/README.md) | Greedy | Reason about ranges on a line by sorting endpoints, merging overlaps, or sweeping events. |
| 17 | [Bit Manipulation](bit-manipulation/README.md) | Intervals | Use binary representation directly for sets, parity, masks, and low-level arithmetic. |
| 18 | [Math & Geometry](math-geometry/README.md) | Bit Manipulation | Apply arithmetic, number theory, coordinate reasoning, and matrix movement cleanly. |

## Interview Relevance

- **Google-style problem solving**: emphasize invariants, proofs, and clean complexity analysis.
- **Meta-style speed**: emphasize Arrays & Hashing, Two Pointers, Sliding Window, Trees, Graphs, and fast pattern recall.
- **Amazon-style communication**: emphasize clarifying assumptions, edge cases, and tradeoffs before coding.
- **AI-lab fundamentals**: emphasize correctness under constraints, graph search, DP, and clean reasoning over unfamiliar variants.

## Prerequisite Rules

- Learn arrays and hashing before sliding window, DP, heaps, and graphs.
- Learn two pointers before linked lists and many in-place array problems.
- Learn recursion before trees, tries, backtracking, and DFS.
- Learn basic graphs before advanced graphs.
- Learn 1-D DP before 2-D DP and interval DP.

## Expected Outcomes

By the end of the roadmap, you should be able to:

- Choose a pattern from constraints rather than keywords alone.
- Explain a brute force baseline and the wasted work.
- State the optimized invariant.
- Code the solution with visible edge-case handling.
- Analyze time and auxiliary space precisely.
- Answer follow-ups about duplicates, sortedness, negative values, memory limits, and changed constraints.

---

## Navigation

[Previous](README.md) | [Home](README.md) | [Next](STUDY_PLAN.md)
