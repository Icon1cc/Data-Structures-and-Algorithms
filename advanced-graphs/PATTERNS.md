# Advanced Graphs Patterns

This file is the main pattern-recognition reference for advanced graphs. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Dijkstra Shortest Path

### Intuition

Expand the unsettled node with the smallest known distance and relax its outgoing edges.

### When To Use It

Use for non-negative weighted shortest paths.

### When Not To Use It

Do not use it with negative edge weights.

### Recognition Signals

- dijkstra shortest path
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Network Delay Time
- Min Cost to Connect All Points

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dist[src] = 0
heap = [(0, src)]
while heap:
    d, u = pop min
    relax edges from u
```

## Pattern: Bellman-Ford

### Intuition

Relax every edge repeatedly so paths with more edges can improve distances.

### When To Use It

Use when negative edges or limited stops matter.

### When Not To Use It

Do not use when all weights are non-negative and Dijkstra is simpler.

### Recognition Signals

- bellman-ford
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Min Cost to Connect All Points
- Critical Connections in a Network

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for round in range(limit):
    next_dist = dist.copy()
    for u, v, w in edges: relax
```

## Pattern: Floyd-Warshall

### Intuition

Allow each node as an intermediate and improve all-pairs distances.

### When To Use It

Use for small dense graphs and all-pairs reachability.

### When Not To Use It

Do not use on large sparse graphs.

### Recognition Signals

- floyd-warshall
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Critical Connections in a Network
- Network Delay Time

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for k in nodes:
    for i in nodes:
        for j in nodes: relax dist[i][j]
```

## Pattern: Minimum Spanning Tree

### Intuition

Choose edges that connect components with minimum total cost and no cycles.

### When To Use It

Use for connecting all points or cities at minimum cost.

### When Not To Use It

Do not confuse MST with shortest path from one source.

### Recognition Signals

- minimum spanning tree
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Network Delay Time
- Min Cost to Connect All Points

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sort edges by weight
for edge in edges:
    if union(u, v): take edge
```

## Pattern: Tarjan Bridges

### Intuition

Use discovery time and low-link values to find edges whose removal disconnects the graph.

### When To Use It

Use for critical connections and bridge detection.

### When Not To Use It

Do not apply bridge logic to directed SCC problems without changing the algorithm.

### Recognition Signals

- tarjan bridges
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Min Cost to Connect All Points
- Critical Connections in a Network

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
dfs(u, parent):
    disc[u] = low[u] = time
    for v in graph[u]: update low values
```

## Pattern: Topological DP

### Intuition

Process DAG nodes in prerequisite order and push best values to outgoing edges.

### When To Use It

Use for longest path, prerequisite accumulation, and DAG optimization.

### When Not To Use It

Do not use before proving the graph is acyclic.

### Recognition Signals

- topological dp
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Critical Connections in a Network
- Network Delay Time

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for node in topo_order:
    for nei in graph[node]:
        dp[nei] = best(dp[nei], transition(dp[node]))
```
---

## Navigation

[Previous](../advanced-graphs/CHEATSHEET.md) | [Home](../README.md) | [Next](../advanced-graphs/easy.md)
