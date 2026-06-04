# Greedy

## What You Will Learn

You will learn the core model behind greedy, the operations it supports, the patterns that interviewers commonly test, and the recognition signals that tell you this topic is being tested.

## Why This Topic Matters

Greedy problems test whether you can turn a prompt into a precise state model. The best solutions are usually short once the invariant is clear.

## Real World Usage

Used in scheduling, caching, compression, resource allocation, interval selection, load assignment, and networking decisions.

## Intuition

Ask what information must be remembered after each step. If you can name that state and explain why it is enough, the implementation becomes much safer.

## Formal Definition

A greedy algorithm builds a solution by committing to locally optimal choices that can be proven globally safe.

## Core Data Structure Or Algorithm

Sort or prioritize candidates so the safe choice is visible, then maintain a proof-friendly invariant.

## Time Complexity

| Operation or Pattern | Complexity |
|---|---:|
| Sort plus scan | O(n log n) |
| Heap greedy | O(n log n) |
| Linear greedy | O(n) |
| Proof | Required even though it is not runtime |

## Space Complexity

| Case | Complexity |
|---|---:|
| Constant counters | O(1) |
| Heap | O(n) |
| Frequency map | O(k) |

## Common Operations

| Operation | What It Means |
|---|---|
| Sort by key | Expose the choice order. |
| Commit | Take a safe candidate. |
| Exchange | Prove another optimal solution can adopt the choice. |
| Repair | Use a heap or replacement when better candidates appear. |

## Visual Explanation

```mermaid
flowchart LR
    A[candidates] --> B[sort or prioritize]
    B --> C[pick safe choice]
    C --> D[update invariant]
```

## Mathematical Foundations

Greedy algorithms need proof through exchange arguments, cut properties, or stays-ahead reasoning.

## Common Interview Patterns

- **Sort and Scan**: Sort candidates so a single pass can make locally safe choices.
- **Interval Greedy**: Choose by earliest finishing boundary or merge by start depending on the objective.
- **Jump Greedy**: Track the farthest reachable position within the current jump boundary.
- **Heap Greedy**: Use a heap to choose the best available candidate while constraints change over time.
- **Exchange Argument**: Show any optimal solution can swap in the greedy choice without becoming worse.
- **Greedy with Counts**: Use frequencies to place, remove, or schedule the most constrained items first.

## Pattern Recognition

Look for the operation the prompt asks you to optimize. If brute force repeats the same lookup, traversal, choice, or state calculation, one of the patterns in this folder is probably intended.

## Common Mistakes

- Coding before defining what the state means.
- Forgetting edge cases such as empty input, one item, duplicates, and boundary endpoints.
- Choosing a familiar pattern even when the constraints do not support its invariant.
- Reporting time complexity without auxiliary memory.

## Interview Tips

- Start with brute force and name the repeated work.
- State the invariant before coding.
- Keep the implementation small and testable.
- Explain why the pattern is correct, not only why it is fast.
- Test one normal case, one edge case, and one adversarial case.

## Mini Exercises

- Write the template for each pattern from memory.
- Solve two Easy problems and explain the invariant aloud.
- Solve one Medium problem with pseudocode before coding.
- Re-solve one missed problem after 24 hours.

## Recommended Learning Order

1. Study Sort and Scan in [PATTERNS.md](PATTERNS.md).
2. Study Interval Greedy in [PATTERNS.md](PATTERNS.md).
3. Study Jump Greedy in [PATTERNS.md](PATTERNS.md).
4. Study Heap Greedy in [PATTERNS.md](PATTERNS.md).
5. Study Exchange Argument in [PATTERNS.md](PATTERNS.md).
6. Study Greedy with Counts in [PATTERNS.md](PATTERNS.md).
7. Review [CHEATSHEET.md](CHEATSHEET.md).
8. Solve [easy.md](easy.md), then [medium.md](medium.md), then selected [hard.md](hard.md).

## Practice Sets

[Cheatsheet](CHEATSHEET.md) | [Patterns](PATTERNS.md) | [Easy](easy.md) | [Medium](medium.md) | [Hard](hard.md)

---

## Navigation

[Previous](../2d-dp/README.md) | [Home](../README.md) | [Next](../greedy/CHEATSHEET.md)
