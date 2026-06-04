# Stack Medium Problems

Curated LeetCode practice for this topic. Solutions are intentionally not included. Solve for pattern recognition, invariant clarity, and interview communication.

## Curation Rules

- Problems are selected for pattern coverage before volume.
- Priority goes to NeetCode 150, Blind 75, Grind 75, and classic high-frequency interview variants.
- Each problem appears once in this repository; related topics should transfer the pattern instead of duplicating the entry.
- Difficulty placement follows the listed LeetCode difficulty and the expected interview reasoning load.

## Practice Order

- First pass: solve in the listed Medium order and write the invariant before coding.
- Second pass: shuffle this file with adjacent topic files to avoid memorizing folder context.
- Retry pass: redo misses after 2 days, 7 days, and 21 days.

## 1. Min Stack

LeetCode: [Min Stack](https://leetcode.com/problems/min-stack/)

Difficulty: Medium

Pattern: Auxiliary Stack

Why It Matters: Combines stack operations with constant-time minimum queries.

Skills Tested:
- Recognize that O(1) min query under push/pop requires an auxiliary stack of running minima parallel to the main stack.
- State the invariant: the top of the min stack always equals the minimum of the values currently in the main stack.
- Decide between pushing on every push (simple) or pushing only on a new minimum (memory-efficient with a count) and explain the trade-off.
- Time O(1) per operation, space O(n), and contrast with scanning the stack on every getMin which is O(n) per query.

Common Follow-Ups:
- Max Stack (LC 716) supports both min and max with a doubly linked list and balanced BST.
- What if removeMin is required (Max Stack again).
- How would you serialize and restore the structure.

## 2. Evaluate Reverse Polish Notation

LeetCode: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Difficulty: Medium

Pattern: Operand Stack

Why It Matters: Exercises operand ordering and operator evaluation.

Skills Tested:
- Recognize that postfix evaluation pushes operands and pops two whenever an operator arrives.
- State the invariant: the stack always holds operands ready to be combined when the next operator appears.
- Handle integer-truncation toward zero in division (Python's `//` rounds toward negative infinity, watch out) and operand order (`a` was pushed before `b`, so `a OP b`).
- Time O(n), space O(n), and explain how this is an iterative form of expression-tree evaluation.

Common Follow-Ups:
- Basic Calculator (LC 224) evaluates an infix expression using an operand and an operator stack.
- What if the operator set includes unary minus or function calls.
- How would you compile this to bytecode for repeated evaluation.

## 3. Daily Temperatures

LeetCode: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Difficulty: Medium

Pattern: Monotonic Decreasing Stack

Why It Matters: Core next-greater-distance problem.

Skills Tested:
- Recognize that "days until a warmer temperature" is "next greater value distance", a monotonic-decreasing stack of indices.
- State the invariant: the stack holds indices whose answer has not yet been found, in strictly decreasing temperature order.
- Pop while `temps[stack.top] < temps[i]` and write `answer[stack.top] = i - stack.top`.
- Time O(n), space O(n), and contrast with O(n^2) brute force.

Common Follow-Ups:
- Next Greater Element II (LC 503) circularizes the array.
- 132 Pattern (LC 456) uses a stack with a side-pointer for the middle value.
- What if you also need the previous warmer day (mirror pass).

## 4. Car Fleet

LeetCode: [Car Fleet](https://leetcode.com/problems/car-fleet/)

Difficulty: Medium

Pattern: Monotonic Stack On Sorted Times

Why It Matters: Uses stack-like grouping after sorting by position.

Skills Tested:
- Recognize that after sorting cars by start position descending, a car merges into the fleet ahead if its time-to-target is less than the fleet's time, else it forms a new fleet.
- State the invariant: the stack of fleet times is strictly increasing and represents the surviving fleets ahead of the current car.
- Use floating-point time carefully (avoid divide-by-zero, but `position < target` and `speed > 0` rule it out by problem statement).
- Time O(n log n) for sort and O(n) for the scan, space O(n).

Common Follow-Ups:
- Car Fleet II (LC 1776) computes per-car collision times with a monotonic stack of collision events.
- What if speeds can change at intermediate checkpoints.
- How does the answer change when cars can pass each other (no longer a fleet model).

## 5. Decode String

LeetCode: [Decode String](https://leetcode.com/problems/decode-string/)

Difficulty: Medium

Pattern: Nested Counter Stack

Why It Matters: Tests nested counters and partial string state.

Skills Tested:
- Recognize that nested `k[...]` patterns require pushing both the multiplier and the partial outer string when entering a bracket.
- State the invariant: the stack of `(prevString, multiplier)` pairs always describes how to combine the current building string with everything outside.
- Parse multi-digit `k` correctly by accumulating digits before pushing.
- Time O(output length), space O(stack depth), and explain why naive recursion blows the call stack on deep inputs.

Common Follow-Ups:
- Number of Atoms (LC 726) extends to chemistry-style nested groups with multipliers.
- Tag Validator (LC 591) uses a similar nested-tag stack.
- What if the encoding allows back-references like `k[group_index]`.

## 6. Asteroid Collision

LeetCode: [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

Difficulty: Medium

Pattern: LIFO Resolution

Why It Matters: Forces repeated resolution against the most recent survivor.

Skills Tested:
- Recognize that only the most recent right-moving asteroid can collide with an incoming left-moving asteroid, which is exactly a stack.
- State the invariant: the stack holds the surviving asteroids in left-to-right order; right-moving entries are at the top until a left-mover resolves them.
- Resolve by comparing absolute values: equal magnitudes annihilate both, otherwise the larger survives.
- Time O(n), space O(n), and explain why a brute simulation is O(n^2) in the worst case.

Common Follow-Ups:
- Robot Bounded In Circle (LC 1041) reuses LIFO resolution thinking on direction state.
- What if asteroids carry a probability of survival.
- How would you support online insertion of new asteroids (maintain the same stack online).

## 7. Online Stock Span

LeetCode: [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

Difficulty: Medium

Pattern: Monotonic Stack With Counts

Why It Matters: Compresses previous prices into spans.

Skills Tested:
- Recognize that "consecutive days with price <= today" is the count of popped entries from a monotonic-decreasing-by-price stack.
- State the invariant: each stack entry stores `(price, span)` and the stack is strictly decreasing in price; on a new day, pop all entries with price <= today and add their spans.
- Use amortized O(1) per call: each day is pushed once and popped at most once across the lifetime.
- Total time O(n) for n calls, space O(n) worst case (strictly decreasing prices).

Common Follow-Ups:
- Sum of Subarray Minimums (LC 907) uses the same pop-and-accumulate accounting.
- Design a streaming maximum-of-window-K with a monotonic deque.
- What changes when prices can be revised retroactively.

## 8. Simplify Path

LeetCode: [Simplify Path](https://leetcode.com/problems/simplify-path/)

Difficulty: Medium

Pattern: Path Stack

Why It Matters: Maps filesystem rules to stack operations.

Skills Tested:
- Recognize that `..` is a pop, `.` is a no-op, and any other token is a push, which is a stack of canonical path components.
- State the invariant: the stack always holds the resolved canonical components corresponding to the prefix processed so far.
- Handle leading slashes, repeated slashes (`//`), and pops on empty stack (treat as no-op or root).
- Time O(n), space O(n), and explain why splitting on `/` first and then walking is cleaner than character-by-character parsing.

Common Follow-Ups:
- Implement `cd` and `pwd` with the same stack model.
- What if symbolic links can introduce cycles (cycle detection on the resolved stack).
- How would you precompute many path simplifications under shared prefixes (trie of components).

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
