# Advanced Graphs Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

Weighted graph algorithms optimize path or connection cost under assumptions about weights, cycles, and directedness. Violating assumptions changes correctness.

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Dijkstra with heap | O((V + E) log V) |
| Bellman-Ford | O(VE) |
| Floyd-Warshall | O(V^3) |
| Kruskal MST | O(E log E) |
| Tarjan SCC | O(V + E) |

## Space Table

| Case | Complexity |
|---|---:|
| Distances | O(V) or O(V^2) |
| Heap frontier | O(E) worst case |
| DSU | O(V) |
| DFS stacks | O(V) |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Dijkstra | Use for shortest paths with non-negative weights. |
| Bellman-Ford | Use for negative edges and negative-cycle detection. |
| Floyd-Warshall | Use for dense graphs and all-pairs shortest paths with small n. |
| Minimum Spanning Tree | Use for cheapest network connection in undirected weighted graphs. |
| Strongly Connected Components | Use for condensation graphs, dependency cycles, and mutual reachability. |
| Bridges And Articulation Points | Use for network reliability and critical connections. |
| DAG Shortest Or Longest Path | Use for weighted DAGs and dependency optimization. |

## Recognition Hints

Look for weighted shortest path, negative edge, all-pairs distance, connect all points with minimum cost, critical edge, strongly connected, or network delay.

## Pattern Choice Checklist

- Dijkstra: non-negative weights, one source, sparse graph friendly.
- Bellman-Ford: negative edges allowed, detects negative cycles.
- Floyd-Warshall: all pairs, dense or small V.
- Kruskal: sort edges and Union Find for MST.

## Interview Calibration

- Say the brute force baseline and the exact wasted work.
- State the invariant before code, not after the solution works.
- Dry run negative weights, disconnected graphs, stale heap entries, and dense-graph constraints before submitting.

## Templates

### Dijkstra

```text
dist[source] = 0
heap = [(0, source)]
while heap:
    d, u = heappop(heap)
    if d != dist[u]: continue
    relax neighbors
```

### Bellman-Ford

```text
for _ in range(V - 1):
    for u, v, w in edges:
        dist[v] = min(dist[v], dist[u] + w)
```

### Floyd-Warshall

```text
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### Minimum Spanning Tree

```text
sort edges by weight
for edge in edges:
    if union(u, v): take edge
```

## Common Traps

- Using Dijkstra with negative weights.
- Confusing MST with shortest path.
- Forgetting stale heap entries.
- Ignoring disconnected graphs or unreachable nodes.

## Interview Reminders

- Say the brute force approach first in one or two sentences.
- State the invariant before coding.
- Test one normal case, one smallest case, and one adversarial case.
- Include auxiliary space, not only input and output size.
- Mention when the pattern assumptions would fail.

## Final Checklist

- [ ] I can define the topic in plain language.
- [ ] I can identify at least three recognition signals.
- [ ] I can write the main template from memory.
- [ ] I can explain time and space complexity.
- [ ] I can name two common mistakes and how to avoid them.

---

## Navigation

[Previous](README.md) | [Home](../README.md) | [Next](PATTERNS.md)
