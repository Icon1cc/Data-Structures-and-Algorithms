# Greedy Patterns

This file is the main pattern-recognition reference for greedy. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Sort and Scan

### Intuition

Sort candidates so a single pass can make locally safe choices.

### When To Use It

Use for many interval, assignment, and minimization problems.

### When Not To Use It

Do not sort by a convenient key without a proof.

### Recognition Signals

- sort and scan
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Jump Game
- Gas Station

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
items.sort(key=chosen_key)
for item in items: decide take or skip
```

## Pattern: Interval Greedy

### Intuition

Choose by earliest finishing boundary or merge by start depending on the objective.

### When To Use It

Use for non-overlap, arrows, and interval selection.

### When Not To Use It

Do not use unweighted interval greedy for weighted interval scheduling.

### Recognition Signals

- interval greedy
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Gas Station
- Candy

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sort intervals by end
if start >= current_end: take
```

## Pattern: Jump Greedy

### Intuition

Track the farthest reachable position within the current jump boundary.

### When To Use It

Use for jump reachability and minimum jumps.

### When Not To Use It

Do not use when every move has different weighted cost.

### Recognition Signals

- jump greedy
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Candy
- Jump Game

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for i in range(n):
    farthest = max(farthest, i + nums[i])
    if i == current_end: jumps += 1
```

## Pattern: Heap Greedy

### Intuition

Use a heap to choose the best available candidate while constraints change over time.

### When To Use It

Use for refueling, hiring, IPO, and scheduling.

### When Not To Use It

Do not use if no dynamic candidate set exists.

### Recognition Signals

- heap greedy
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Jump Game
- Gas Station

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
add candidates that are now available
choose best candidate from heap
```

## Pattern: Exchange Argument

### Intuition

Show any optimal solution can swap in the greedy choice without becoming worse.

### When To Use It

Use to justify greedy correctness in interviews.

### When Not To Use It

Do not present greedy as correct without a proof or counterexample check.

### Recognition Signals

- exchange argument
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Gas Station
- Candy

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
Assume optimal solution differs
replace its first differing choice with greedy choice
show value stays optimal
```

## Pattern: Greedy with Counts

### Intuition

Use frequencies to place, remove, or schedule the most constrained items first.

### When To Use It

Use for character rearrangement, task scheduler, and deletion minimization.

### When Not To Use It

Do not ignore impossible max-frequency conditions.

### Recognition Signals

- greedy with counts
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Candy
- Jump Game

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
count items
while counts remain:
    choose highest valid count
    update counts
```
---

## Navigation

[Previous](../greedy/CHEATSHEET.md) | [Home](../README.md) | [Next](../greedy/easy.md)
