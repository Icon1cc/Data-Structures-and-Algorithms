# Linked List

## What You Will Learn

You will learn the core model behind linked list, the operations it supports, the patterns that interviewers commonly test, and the recognition signals that tell you this topic is being tested.

## Why This Topic Matters

Linked List problems test whether you can turn a prompt into a precise state model. The best solutions are usually short once the invariant is clear.

## Real World Usage

Used in LRU caches, memory allocators, undo stacks, schedulers, adjacency lists, and systems where O(1) splicing after a known node matters.

## Intuition

Ask what information must be remembered after each step. If you can name that state and explain why it is enough, the implementation becomes much safer.

## Formal Definition

A linked list is a sequence of nodes where each node stores a value and one or more references to neighboring nodes. Unlike arrays, linked lists do not provide constant-time index access.

## Core Data Structure Or Algorithm

Use dummy nodes for head changes, fast and slow pointers for structural questions, and careful rewiring for reversal or splicing.

## Time Complexity

| Operation or Pattern | Complexity |
|---|---:|
| Search or access by position | O(n) |
| Insert after known node | O(1) |
| Delete after known node | O(1) |
| Reverse list | O(n) |

## Space Complexity

| Case | Complexity |
|---|---:|
| Iterative rewiring | O(1) |
| Recursive traversal | O(n) stack |
| Copy with map | O(n) |

## Common Operations

| Operation | What It Means |
|---|---|
| Traverse | Move node by node because there is no random access. |
| Rewire | Change next pointers in an order that never loses the remaining list. |
| Splice | Insert or remove a segment by adjusting neighboring links. |
| Detect cycle | Use two pointers moving at different speeds. |

## Visual Explanation

```mermaid
flowchart LR
    A[prev] --> B[curr]
    B --> C[next]
    C --> D[rest]
```

## Mathematical Foundations

Pointer algorithms are proved by preserving reachability. After each rewire, every node must still be reachable from either the reversed prefix or the unreversed suffix.

## Common Interview Patterns

- **Dummy Head**: Add a sentinel node before the real head so deleting or inserting near the head has the same logic as every other position.
- **Fast and Slow Pointers**: Move two references at different speeds or with a fixed gap to reveal cycles, middles, and nth-from-end positions.
- **In-place Reversal**: Reverse links one node at a time while preserving the next node before rewiring.
- **Merge Lists**: Always attach the smaller available head from sorted lists and advance that source.
- **Cycle Detection**: A faster pointer eventually catches a slower pointer if a cycle exists.
- **Copy with Random Pointer**: Create a mapping from original node identity to cloned node, then wire next and random references.

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

1. Study Dummy Head in [PATTERNS.md](PATTERNS.md).
2. Study Fast and Slow Pointers in [PATTERNS.md](PATTERNS.md).
3. Study In-place Reversal in [PATTERNS.md](PATTERNS.md).
4. Study Merge Lists in [PATTERNS.md](PATTERNS.md).
5. Study Cycle Detection in [PATTERNS.md](PATTERNS.md).
6. Study Copy with Random Pointer in [PATTERNS.md](PATTERNS.md).
7. Review [CHEATSHEET.md](CHEATSHEET.md).
8. Solve [easy.md](easy.md), then [medium.md](medium.md), then selected [hard.md](hard.md).

## Practice Sets

[Cheatsheet](CHEATSHEET.md) | [Patterns](PATTERNS.md) | [Easy](easy.md) | [Medium](medium.md) | [Hard](hard.md)

---

## Navigation

[Previous](../sliding-window/README.md) | [Home](../README.md) | [Next](../linked-list/CHEATSHEET.md)
