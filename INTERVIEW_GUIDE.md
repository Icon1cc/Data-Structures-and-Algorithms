# Interview Guide

This guide focuses on execution during a live coding interview.

## Interview Process

Most technical interviews follow this shape:

1. Clarify the task and constraints.
2. Work through examples and edge cases.
3. State a brute force approach.
4. Identify wasted work.
5. Propose an optimized pattern.
6. Code with a stated invariant.
7. Test manually.
8. Analyze time and space.
9. Discuss follow-ups.

## Communication

Speak in short, concrete statements. Interviewers are listening for whether you can reason, not whether you can narrate every keystroke.

Useful phrases:

- "The brute force approach is..."
- "The repeated work is..."
- "The invariant I want to maintain is..."
- "This pattern works because..."
- "This edge case matters because..."
- "The auxiliary space is..."

## Brute Force To Optimized Thinking

Do not skip brute force. A clear brute force solution shows you understand the problem. Optimization usually comes from naming the wasted work:

| Wasted Work | Common Optimization |
|---|---|
| Repeated membership scan | Hash set or hash map |
| Recomputed range sum | Prefix sum |
| Rechecking every substring | Sliding window |
| Pair search in sorted data | Two pointers |
| Repeated min or max selection | Heap |
| Repeated recursive subproblem | Dynamic programming |
| Repeated reachability from scratch | Graph traversal or Union Find |

## Complexity Analysis

Always separate:

- Input size.
- Number of states or nodes visited.
- Work per state.
- Auxiliary space.
- Output size when output can be large.

Examples:

- Sliding window: each pointer moves at most n times, so O(n).
- Monotonic stack: each item is pushed once and popped once, so O(n) amortized.
- DP: states times transition cost.
- Graph traversal: O(V + E), not only O(V).
- Backtracking: exponential output is expected, but pruning still matters.

## Edge-Case Checklist

- Empty input.
- One item.
- Duplicates.
- Negative values.
- Sorted versus unsorted input.
- All equal values.
- Disconnected graph.
- Cycle.
- Deep recursion.
- Overflow in fixed-width languages.
- Mutating input when the caller may expect it preserved.

## Big-Tech Preparation Notes

- **Google**: emphasize invariants, proofs, and clean reasoning on unfamiliar variants.
- **Meta**: emphasize speed, pattern recognition, and bug-free implementation.
- **Amazon**: emphasize communication, edge cases, and practical tradeoffs.
- **OpenAI, Anthropic, Mistral**: emphasize fundamentals, clarity, correctness, and ability to adapt under changed constraints.

## Mock Interview Strategy

- Do one untimed explanation mock before timed mocks.
- In timed mocks, spend the first 5 minutes clarifying and planning.
- After each mock, write the exact moment where you lost time.
- Retry the same problem three days later without notes.
- Practice follow-ups: memory reduction, streaming input, duplicates, negative weights, very large input, and concurrency only when relevant.

## Final Interview Checklist

- [ ] I clarified inputs, outputs, and constraints.
- [ ] I stated brute force.
- [ ] I identified wasted work.
- [ ] I chose a pattern and named the invariant.
- [ ] I coded with edge cases visible.
- [ ] I tested manually.
- [ ] I gave precise time and auxiliary space.
- [ ] I handled at least one follow-up.

---

## Navigation

[Previous](STUDY_PLAN.md) | [Home](README.md) | [Next](REPO_INDEX.md)
