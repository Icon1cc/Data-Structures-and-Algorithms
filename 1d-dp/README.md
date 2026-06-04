# 1-D Dynamic Programming

## What This Topic Is

Define a one-dimensional state so overlapping subproblems are solved once.

This topic is a reusable mental model, not a bag of isolated tricks. You should finish it able to identify the problem shape, state the invariant, choose the right pattern, and explain the complexity without guessing.

## Why It Matters

1-D dynamic programming teaches the central DP skill: naming what a state means before trying to code transitions.

In interviews, the story usually hides the structure. Translate the story into operations: lookup, move a boundary, traverse, choose, relax, split, merge, or remember a state.

## Real-World Use

Used in pricing, sequence scoring, scheduling, inventory planning, retries, resource allocation, and optimization over linear histories.

The same ideas show up in production systems when constraints demand predictable lookup, bounded memory, fast traversal, or correct ordering.

## Beginner Intuition

DP is remembering answers to smaller versions of the same question. The hard part is choosing a state that contains enough history but not unnecessary detail.

Beginner rule: before coding, write one sentence that says what information your algorithm keeps and why that information is enough for the next decision.

## Formal Explanation

Dynamic programming applies when optimal substructure and overlapping subproblems exist. A 1-D DP state usually depends on earlier indices or capacities.

The formal model matters because it tells you which operations are cheap, which are expensive, and which assumptions are required for correctness.

## Core Operations

| Operation | Meaning |
|---|---|
| Define state | Write what dp[i] means in plain language. |
| Choose transition | List previous states that can lead to current. |
| Initialize base cases | Make the first states true by definition. |
| Fill order | Compute dependencies before dependents. |
| Compress | Keep only needed previous states when safe. |

## Time Complexity

| Operation or Pattern | Complexity |
|---|---:|
| Linear recurrence | O(n) |
| Capacity DP | O(n * capacity) |
| LIS quadratic | O(n^2) |
| LIS with binary search | O(n log n) |

## Space Complexity

| Case | Complexity |
|---|---:|
| Full table | O(n) or O(n * capacity) |
| Rolling variables | O(1) |
| Memo recursion | O(states) plus call stack |

## Visual Explanation

```mermaid
flowchart LR
    A[dp[i-2]] --> C[dp[i]]
    B[dp[i-1]] --> C
    C --> D[dp[i+1]]
    C --> E[dp[i+2]]
    F[State meaning] --> C
    G[Transition choice] --> C
```

## Foundations And Invariants

State meaning drives everything. If dp[i] means best answer ending at i, the transition is different from best answer using first i items.

When explaining a solution, name the invariant before writing code. A good invariant is short enough to repeat while coding and precise enough to catch edge cases.

## Pattern Recognition

Look for count ways, min cost, max profit, can reach, choose or skip, subsequence, partition, coin change, or repeated recursion over indices.

Ask these questions:

- What is the smallest state that makes the next decision easy?
- Does the problem require order, membership, connectivity, optimal choice, or all possibilities?
- Does any boundary move monotonically?
- Are constraints small enough for exponential search or DP state?

## Common Interview Patterns

- **State Definition**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Memoization**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Tabulation**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Transition Choice**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Knapsack**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Subsequence DP**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **State Compression**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).
- **Kadane**: recognition signals, mistakes, and templates in [PATTERNS.md](PATTERNS.md).

## Common Mistakes

- Coding before defining the state.
- Mixing ending-at with up-to-index states.
- Using wrong fill direction for 0/1 knapsack.
- Forgetting impossible-state sentinels.

## Interview Tips

- Start with brute force and name the repeated work or missing invariant.
- State why the chosen pattern removes that waste.
- Keep edge cases visible while coding.
- Give both time and auxiliary space complexity.
- If the interviewer changes constraints, re-check the pattern assumptions before modifying code.

## Mini Exercises

- Explain `State Definition` aloud, then write its invariant and template from memory.
- Explain `Memoization` aloud, then write its invariant and template from memory.
- Explain `Tabulation` aloud, then write its invariant and template from memory.
- Explain `Transition Choice` aloud, then write its invariant and template from memory.
- Pick two Easy problems from [easy.md](easy.md) and identify the pattern before coding.
- Pick one Medium problem from [medium.md](medium.md) and write pseudocode before implementation.
- For one missed problem, write the failed invariant and the corrected invariant.

## Recommended Learning Order

1. Read `State Definition` in [PATTERNS.md](PATTERNS.md).
2. Read `Memoization` in [PATTERNS.md](PATTERNS.md).
3. Read `Tabulation` in [PATTERNS.md](PATTERNS.md).
4. Read `Transition Choice` in [PATTERNS.md](PATTERNS.md).
5. Read `Knapsack` in [PATTERNS.md](PATTERNS.md).
6. Read `Subsequence DP` in [PATTERNS.md](PATTERNS.md).
7. Read `State Compression` in [PATTERNS.md](PATTERNS.md).
8. Read `Kadane` in [PATTERNS.md](PATTERNS.md).
9. Review [CHEATSHEET.md](CHEATSHEET.md) before timed practice.
10. Solve [easy.md](easy.md), then [medium.md](medium.md), then selected [hard.md](hard.md).

## Practice Navigation

- [Easy problems](easy.md): build fundamentals.
- [Medium problems](medium.md): build interview fluency.
- [Hard problems](hard.md): build advanced pattern recognition.

---

## Navigation

[Previous](../advanced-graphs/README.md) | [Home](../README.md) | [Next](CHEATSHEET.md)
