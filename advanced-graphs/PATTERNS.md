# Advanced Graphs Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Dijkstra | weighted shortest path | Do not use when any reachable edge can be negative |
| Bellman-Ford | negative edge | Do not choose it over Dijkstra when all weights are non-negative and constraints are large |
| Floyd-Warshall | all pairs | Do not use on large sparse graphs where n cubed is impossible |
| Minimum Spanning Tree | connect all | Do not use MST for shortest path between two nodes |
| Strongly Connected Components | mutual reachability | Do not use undirected component logic on directed graphs |
| Bridges And Articulation Points | critical edge | Do not apply bridge logic to directed SCC problems unchanged |
| DAG Shortest Or Longest Path | DAG | Do not use when cycles exist |

## Pattern: Dijkstra

### Beginner Intuition

Expand the cheapest known frontier node and relax non-negative edges.

### When To Use It

Use for shortest paths with non-negative weights.

### When Not To Use It

Do not use when any reachable edge can be negative.

### Recognition Signals

- weighted shortest path
- non-negative
- min heap

### Example Problems

- Network Delay Time
- Path With Minimum Effort

### Common Mistakes

- Treating a popped distance as final without checking `if d != dist[u]: continue`; stale heap entries inflate the running answer.
- Pushing on relaxation without updating `dist[v]`; the heap fills with redundant entries (correct but slow).
- Running Dijkstra on a graph with negative edges; once a node is settled with a too-large distance, no later relaxation revisits it.

### Pseudocode Or Template

```text
dist[source] = 0
heap = [(0, source)]
while heap:
    d, u = heappop(heap)
    if d != dist[u]: continue
    relax neighbors
```

### Complexity Notes

O((V + E) log V) with a heap.

### Interview Explanation

Non-negative weights make the popped shortest distance final.

## Pattern: Bellman-Ford

### Beginner Intuition

Relax every edge repeatedly so paths with more edges become known.

### When To Use It

Use for negative edges and negative-cycle detection.

### When Not To Use It

Do not choose it over Dijkstra when all weights are non-negative and constraints are large.

### Recognition Signals

- negative edge
- k stops
- cycle detection

### Example Problems

- Cheapest Flights Within K Stops
- Network Delay variants

### Common Mistakes

- For bounded-edge variants, updating `dist` in place; use a snapshot of the previous round so a value updated this round does not leak into another update.
- Running for fewer than `V - 1` rounds; the algorithm needs `V - 1` to settle the longest possible simple path.
- Detecting negative cycles by running exactly `V - 1` rounds; the negative-cycle test requires one more round and checks for any further relaxation.

### Pseudocode Or Template

```text
for _ in range(V - 1):
    for u, v, w in edges:
        dist[v] = min(dist[v], dist[u] + w)
```

### Complexity Notes

O(VE) time, O(V) space.

### Interview Explanation

After i rounds, shortest paths using at most i edges are known.

## Pattern: Floyd-Warshall

### Beginner Intuition

Allow each node as an intermediate and improve every pair distance.

### When To Use It

Use for dense graphs and all-pairs shortest paths with small n.

### When Not To Use It

Do not use on large sparse graphs where n cubed is impossible.

### Recognition Signals

- all pairs
- dense
- intermediate

### Example Problems

- Find the City With the Smallest Number of Neighbors at a Threshold Distance

### Common Mistakes

- Putting `k` as the inner loop; the intermediate index must be outermost so the recurrence sees only allowed intermediates.
- Initializing `dist[i][i]` to a non-zero value; the diagonal must be 0 for the relaxation to work.
- Using `int` infinity sentinels that overflow on addition; use a large but safely additive constant or guard the relaxation with `dist[i][k] + dist[k][j] < dist[i][j]`.

### Pseudocode Or Template

```text
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### Complexity Notes

O(V^3) time, O(V^2) space.

### Interview Explanation

When k is outermost, dist only uses allowed intermediate nodes up to k.

## Pattern: Minimum Spanning Tree

### Beginner Intuition

Connect all nodes with minimum total edge cost without cycles.

### When To Use It

Use for cheapest network connection in undirected weighted graphs.

### When Not To Use It

Do not use MST for shortest path between two nodes.

### Recognition Signals

- connect all
- minimum cost
- undirected

### Example Problems

- Min Cost to Connect All Points
- Find Critical and Pseudo-Critical Edges in MST

### Common Mistakes

- Confusing MST with shortest path; an MST minimizes total edge weight, not pairwise distance.
- For Kruskal, forgetting union-find path compression on dense inputs; the algorithm degrades to near-quadratic without it.
- For Prim with a complete graph (e.g., point-to-point Manhattan distances), building an explicit edge list is wasteful; iterate over neighbors implicitly.

### Pseudocode Or Template

```text
sort edges by weight
for edge in edges:
    if union(u, v): take edge
```

### Complexity Notes

Kruskal is O(E log E); Prim is O(E log V).

### Interview Explanation

A cheapest safe edge crossing a cut can be added without hurting optimality.

## Pattern: Strongly Connected Components

### Beginner Intuition

Group directed nodes that can all reach each other.

### When To Use It

Use for condensation graphs, dependency cycles, and mutual reachability.

### When Not To Use It

Do not use undirected component logic on directed graphs.

### Recognition Signals

- mutual reachability
- SCC
- directed

### Example Problems

- Critical Connections in a Network related
- strongly connected designs

### Common Mistakes

- Computing connected components on the underlying undirected graph; the result is not SCC.
- For Tarjan's algorithm, confusing `disc[u]` (DFS discovery time) with `low[u]` (smallest reachable discovery); they update on different events.
- Forgetting the SCC stack; nodes leave the stack only when their subtree's `low == disc`.

### Pseudocode Or Template

```text
Tarjan: assign index and lowlink during DFS
when lowlink == index, pop one SCC
```

### Complexity Notes

O(V + E) time.

### Interview Explanation

An SCC is a maximal region where every node can reach every other node.

## Pattern: Bridges And Articulation Points

### Beginner Intuition

Use DFS low-link values to find edges or nodes whose removal disconnects the graph.

### When To Use It

Use for network reliability and critical connections.

### When Not To Use It

Do not apply bridge logic to directed SCC problems unchanged.

### Recognition Signals

- critical edge
- bridge
- lowlink

### Example Problems

- Critical Connections in a Network

### Common Mistakes

- Treating the parent edge as a back edge; the algorithm must skip the immediate parent during low-update.
- Forgetting that for the root, articulation requires two or more independent subtrees, while non-root nodes use the `low[v] >= disc[u]` rule.
- Running on a directed graph using the same low-link rule; SCC needs Tarjan's separate algorithm.

### Pseudocode Or Template

```text
dfs(u, parent):
    disc[u] = low[u] = time
    for v in graph[u]: update low
    if low[v] > disc[u]: edge is bridge
```

### Complexity Notes

O(V + E) time, O(V) space.

### Interview Explanation

If a child cannot reach an ancestor of u, the edge to that child is critical.

## Pattern: DAG Shortest Or Longest Path

### Beginner Intuition

Topologically order a DAG, then relax edges once in order.

### When To Use It

Use for weighted DAGs and dependency optimization.

### When Not To Use It

Do not use when cycles exist.

### Recognition Signals

- DAG
- topological order
- relax once

### Example Problems

- Course Schedule style weighted variants

### Common Mistakes

- Running Dijkstra on a DAG instead of single-pass topological relaxation; the latter is O(V + E) without a heap.
- Computing the topological order separately and then forgetting to use it; relax in topological order, not arbitrary order.
- Treating "longest path on a DAG" as NP-hard (it is on a general graph); on a DAG you simply negate weights or maximize during relaxation.

### Pseudocode Or Template

```text
order = topo_sort(graph)
for u in order:
    for v, w in graph[u]: relax
```

### Complexity Notes

O(V + E) time after topological sort.

### Interview Explanation

Topological order guarantees every predecessor is finalized before a node is processed.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
