# Greedy Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Sort And Scan | sort | Do not sort by a key that does not match the proof |
| Greedy With Proof | exchange | Do not rely on intuition alone |
| Interval Greedy | earliest end | Do not pick longest interval unless that is specifically proven |
| Jump Greedy | farthest reach | Do not BFS all indices when range tracking is enough |
| Heap-Assisted Greedy | available choices | Do not sort once if availability and priority are separate dimensions |
| Monotonic Greedy | lexicographic | Do not pop a value if it cannot appear again and is required |

## Pattern: Sort And Scan

### Beginner Intuition

Sort to expose the safest next candidate, then make one pass.

### When To Use It

Use for intervals, cookies, arrows, and pairing.

### When Not To Use It

Do not sort by a key that does not match the proof.

### Recognition Signals

- sort
- earliest finish
- one pass

### Example Problems

- Assign Cookies
- Minimum Number of Arrows to Burst Balloons

### Common Mistakes

- Sorting by start when the proof needs end.
- Ignoring the exclusion case for Sort And Scan: Do not sort by a key that does not match the proof.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
items.sort(key=key)
for item in items:
    if safe(item): take item
```

### Complexity Notes

O(n log n) time.

### Interview Explanation

The sorted order makes the exchange argument simple.

## Pattern: Greedy With Proof

### Beginner Intuition

Choose locally only after proving the choice can appear in some optimal solution.

### When To Use It

Use for all greedy problems.

### When Not To Use It

Do not rely on intuition alone.

### Recognition Signals

- exchange
- proof
- locally optimal

### Example Problems

- Jump Game
- Non-overlapping Intervals

### Common Mistakes

- Skipping the correctness argument.
- Ignoring the exclusion case for Greedy With Proof: Do not rely on intuition alone.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
state greedy choice
show any optimal solution can swap to it
```

### Complexity Notes

Implementation varies; proof is required.

### Interview Explanation

I explain why taking this choice never blocks a better global answer.

## Pattern: Interval Greedy

### Beginner Intuition

Pick the interval that leaves the most room for future intervals.

### When To Use It

Use for erase overlap, meeting selection, and arrows.

### When Not To Use It

Do not pick longest interval unless that is specifically proven.

### Recognition Signals

- earliest end
- overlap
- scheduling

### Example Problems

- Non-overlapping Intervals
- Meeting Rooms II

### Common Mistakes

- Treating touching endpoints incorrectly.
- Ignoring the exclusion case for Interval Greedy: Do not pick longest interval unless that is specifically proven.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
sort by end
last_end = -inf
for interval in intervals:
    if interval.start >= last_end: take it
```

### Complexity Notes

O(n log n) time.

### Interview Explanation

Earliest finishing compatible interval is safest because it leaves maximum remaining space.

## Pattern: Jump Greedy

### Beginner Intuition

Track the farthest reachable index within the current jump range.

### When To Use It

Use for reachability and minimum jumps.

### When Not To Use It

Do not BFS all indices when range tracking is enough.

### Recognition Signals

- farthest reach
- jump
- range

### Example Problems

- Jump Game
- Jump Game II

### Common Mistakes

- Updating jump count before finishing the current range.
- Ignoring the exclusion case for Jump Greedy: Do not BFS all indices when range tracking is enough.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
end = farthest = jumps = 0
for i in range(n - 1):
    farthest = max(farthest, i + nums[i])
    if i == end: jumps += 1; end = farthest
```

### Complexity Notes

O(n) time, O(1) space.

### Interview Explanation

Each range represents all indices reachable with the current jump count.

## Pattern: Heap-Assisted Greedy

### Beginner Intuition

Use a heap when the greedy choice changes as candidates become available.

### When To Use It

Use for scheduling, refueling, and selecting best active resource.

### When Not To Use It

Do not sort once if availability and priority are separate dimensions.

### Recognition Signals

- available choices
- heap
- schedule

### Example Problems

- Task Scheduler
- Minimum Number of Refueling Stops

### Common Mistakes

- Pushing candidates too late after they become reachable.
- Ignoring the exclusion case for Heap-Assisted Greedy: Do not sort once if availability and priority are separate dimensions.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
sort by availability
while need progress:
    add newly available choices to heap
    take best choice
```

### Complexity Notes

O(n log n) time.

### Interview Explanation

Sorting handles availability and the heap handles best active choice.

## Pattern: Monotonic Greedy

### Beginner Intuition

Maintain a result stack and remove worse previous choices while it is safe.

### When To Use It

Use for lexicographically smallest subsequences and digit removal.

### When Not To Use It

Do not pop a value if it cannot appear again and is required.

### Recognition Signals

- lexicographic
- remove k
- stack greedy

### Example Problems

- Remove K Digits
- Remove Duplicate Letters

### Common Mistakes

- Popping required characters without checking future availability.
- Ignoring the exclusion case for Monotonic Greedy: Do not pop a value if it cannot appear again and is required.
- Failing to test counterexamples, tie-breaking, proof gaps, and sorted-order assumptions against the stated invariant.

### Pseudocode Or Template

```text
while stack and can_improve(stack[-1], x) and safe_to_pop:
    stack.pop()
stack.append(x)
```

### Complexity Notes

O(n) amortized time.

### Interview Explanation

I only remove a previous choice when a better current choice can replace it safely.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
