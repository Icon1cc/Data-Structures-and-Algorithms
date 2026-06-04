# Heap / Priority Queue Medium Problems

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

## 1. Kth Largest Element in an Array

LeetCode: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Difficulty: Medium

Pattern: Top K Heap

Why It Matters: Classic selection without full sort.

Skills Tested:
- Identify the Top K Heap signal before choosing a template.
- State the invariant for Kth Largest Element in an Array: classic selection without full sort.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Kth Largest Element in an Array toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Top K Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

## 2. Top K Frequent Elements

LeetCode: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

Difficulty: Medium

Pattern: Frequency Plus Heap

Why It Matters: Combines hashing with heap selection.

Skills Tested:
- Identify the Frequency Plus Heap signal before choosing a template.
- State the invariant for Top K Frequent Elements: combines hashing with heap selection.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Top K Frequent Elements toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Frequency Plus Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

## 3. Find K Pairs with Smallest Sums

LeetCode: [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

Difficulty: Medium

Pattern: K-way Heap Frontier

Why It Matters: Uses sorted pair frontier expansion.

Skills Tested:
- Identify the K-way Heap Frontier signal before choosing a template.
- State the invariant for Find K Pairs with Smallest Sums: uses sorted pair frontier expansion.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Find K Pairs with Smallest Sums toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the K-way Heap Frontier invariant survive streaming input, in-place restrictions, or lower memory limits?

## 4. K Closest Points to Origin

LeetCode: [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

Difficulty: Medium

Pattern: Top K Heap

Why It Matters: Tests custom priority by distance.

Skills Tested:
- Identify the Top K Heap signal before choosing a template.
- State the invariant for K Closest Points to Origin: tests custom priority by distance.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push K Closest Points to Origin toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Top K Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

## 5. Task Scheduler

LeetCode: [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

Difficulty: Medium

Pattern: Heap-Assisted Scheduling

Why It Matters: Uses counts and cooldown timing.

Skills Tested:
- Identify the Heap-Assisted Scheduling signal before choosing a template.
- State the invariant for Task Scheduler: uses counts and cooldown timing.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Task Scheduler toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Heap-Assisted Scheduling invariant survive streaming input, in-place restrictions, or lower memory limits?

## 6. Design Twitter

LeetCode: [Design Twitter](https://leetcode.com/problems/design-twitter/)

Difficulty: Medium

Pattern: K-way Merge

Why It Matters: Merges recent tweet streams by time.

Skills Tested:
- Identify the K-way Merge signal before choosing a template.
- State the invariant for Design Twitter: merges recent tweet streams by time.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Design Twitter toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the K-way Merge invariant survive streaming input, in-place restrictions, or lower memory limits?

## 7. Sort Characters By Frequency

LeetCode: [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Difficulty: Medium

Pattern: Frequency Heap

Why It Matters: Orders values by counts.

Skills Tested:
- Identify the Frequency Heap signal before choosing a template.
- State the invariant for Sort Characters By Frequency: orders values by counts.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Sort Characters By Frequency toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Frequency Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

## 8. Single-Threaded CPU

LeetCode: [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

Difficulty: Medium

Pattern: Available Task Heap

Why It Matters: Separates arrival ordering from processing priority.

Skills Tested:
- Identify the Available Task Heap signal before choosing a template.
- State the invariant for Single-Threaded CPU: separates arrival ordering from processing priority.
- Handle tie-breakers, stale entries, empty heaps, and heap size invariants.
- Explain time, auxiliary space, and any output-size cost separately.

Common Follow-Ups:
- What changes if the constraints push Single-Threaded CPU toward sorting, quickselect, deque, balanced tree, or bucket counting?
- Which tie-breakers case would break the first implementation?
- Can the Available Task Heap invariant survive streaming input, in-place restrictions, or lower memory limits?

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
