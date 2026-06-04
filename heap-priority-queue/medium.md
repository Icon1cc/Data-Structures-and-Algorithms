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

Pattern: Top K Heap Or Quickselect

Why It Matters: Classic selection without full sort.

Skills Tested:
- Recognize that "kth largest" supports two solid approaches: a min-heap of size `k` (O(n log k)) and randomized quickselect (O(n) average).
- State the heap invariant: the heap always holds the k largest seen, so the top is the answer once the array is consumed.
- Implement Hoare or Lomuto partition correctly for the quickselect path; avoid the worst-case O(n^2) by random pivot selection.
- Compare time and space trade-offs: heap is deterministic but slower; quickselect is faster on average but in-place.

Common Follow-Ups:
- Kth Largest Element in a Stream (LC 703) is the streaming variant.
- Find K-th Smallest Pair Sum and other top-k variants.
- What if values are bounded (counting sort takes O(n + range)).

## 2. Top K Frequent Elements

LeetCode: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

Difficulty: Medium

Pattern: Frequency Plus Heap Or Bucket Sort

Why It Matters: Combines hashing with heap selection.

Skills Tested:
- Recognize that the answer is the k keys with the largest values in a frequency map, solvable by a min-heap of size k or by bucket sort indexed by frequency.
- State the heap invariant: keep at most k entries `(freq, key)` and pop the smallest when overflow occurs.
- Bucket sort: place each key into `bucket[freq]`, then walk buckets from highest to lowest until k keys are collected.
- Time O(n log k) for heap or O(n) for bucket sort, space O(n).

Common Follow-Ups:
- Sort Characters By Frequency (LC 451) is the same idea over characters.
- What if the input is streamed and `k` queries arrive online.
- Generalize to top-k by a multi-key priority.

## 3. Find K Pairs with Smallest Sums

LeetCode: [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

Difficulty: Medium

Pattern: K-Way Merge Frontier

Why It Matters: Uses sorted pair frontier expansion.

Skills Tested:
- Recognize that pairs `(nums1[i], nums2[j])` from sorted arrays form a sum that increases monotonically along each axis, so a heap of frontier pairs grows the smallest sums first.
- State the invariant: every pair popped is provably one of the smallest-sum unvisited pairs; pushing `(i, j+1)` (and `(i+1, j)` only when `j == 0`) keeps the frontier without duplicates.
- Use a `visited` set or the "push only along one axis when first popped" trick to avoid double-pushing.
- Time O(k log k), space O(k), and contrast with sorting all pairs which is O(N * M log(NM)).

Common Follow-Ups:
- Find K-th Smallest Element in a Sorted Matrix (LC 378) reuses the frontier idea.
- What if the operation is product instead of sum.
- Generalize to k-way frontier across more than two arrays.

## 4. K Closest Points to Origin

LeetCode: [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

Difficulty: Medium

Pattern: Top K Heap By Distance

Why It Matters: Tests custom priority by distance.

Skills Tested:
- Recognize that "k closest" by Euclidean distance is solved by a max-heap of size k that evicts farther points as new ones arrive.
- State the invariant: at any moment, the heap holds the k closest points seen so far; the top is the worst (farthest) of those.
- Compare squared distance to avoid `sqrt` cost; the order is preserved.
- Time O(n log k), space O(k), and compare with quickselect O(n) average.

Common Follow-Ups:
- Find Closest LCP - distance variants on strings.
- What if the distance metric is Manhattan or Chebyshev (still pairwise comparable).
- Generalize to top-k under multi-dimensional distances with KD-trees.

## 5. Task Scheduler

LeetCode: [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

Difficulty: Medium

Pattern: Greedy Scheduling With Heap And Cooldown Queue

Why It Matters: Uses counts and cooldown timing.

Skills Tested:
- Recognize that the optimal schedule fills each slot with the highest-count task whose cooldown has expired.
- State the invariant: a max-heap of remaining counts and a queue of `(taskCount, readyTime)` tuples track which tasks can run at the current time.
- Account for idle time when no task is ready by advancing time directly to the next ready time.
- Closed-form alternative: `max(len(tasks), (maxCount - 1) * (n + 1) + tieCount)` derives the answer from counts.

Common Follow-Ups:
- Reorganize String (LC 767) layouts characters to avoid adjacency.
- What if tasks have priorities or deadlines.
- How would you parallelize across multiple workers.

## 6. Design Twitter

LeetCode: [Design Twitter](https://leetcode.com/problems/design-twitter/)

Difficulty: Medium

Pattern: K-Way Merge Of Recent Streams

Why It Matters: Merges recent tweet streams by time.

Skills Tested:
- Recognize that `getNewsFeed` is a k-way merge over the user and each followee's tweet timeline, capped at 10 items.
- State the invariant: a heap of latest tweets across all relevant timelines yields the most recent at every pop.
- Maintain per-user followers and per-user tweets (linked list or list) for O(1) post.
- Per-feed time O(k log F) where F is the number of followees, space O(N tweets).

Common Follow-Ups:
- Add tweet edits and deletions while preserving the ordering invariant.
- What if "feed" uses ranked relevance instead of time.
- How would you shard the design across servers.

## 7. Sort Characters By Frequency

LeetCode: [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Difficulty: Medium

Pattern: Frequency Sort

Why It Matters: Orders values by counts.

Skills Tested:
- Recognize that the desired order is "characters by descending frequency, ties broken arbitrarily", which is a max-heap of `(freq, char)` or a sort by `-freq`.
- State the invariant: each character contributes a run of length `freq` in the output; concatenate runs in descending order.
- Compare bucket sort by frequency (O(n)) with sort-by-key (O(k log k) on unique chars).
- Time O(n + k log k), space O(n + k).

Common Follow-Ups:
- Top K Frequent Elements (LC 347) is the count-only variant.
- Reorganize String (LC 767) adds the no-adjacent constraint.
- What if frequencies are equal and a stable order must be enforced.

## 8. Single-Threaded CPU

LeetCode: [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

Difficulty: Medium

Pattern: Two-Phase Heap Scheduling

Why It Matters: Separates arrival ordering from processing priority.

Skills Tested:
- Recognize that tasks arrive in time order but are picked by `(processingTime, index)` priority among the ready set, which is two structures: a sorted arrival queue and a min-heap of ready tasks.
- State the invariant: at every moment, the ready heap contains all tasks with `enqueueTime <= currentTime` not yet executed.
- Advance `currentTime` to the next arrival when the ready heap is empty.
- Time O(n log n), space O(n), and explain how the secondary key (index) breaks ties on processing time.

Common Follow-Ups:
- Reorganize tasks under preemption.
- What if multiple CPUs run in parallel (heap of available CPUs).
- How would you support task cancellation.

---

## Navigation

[Previous](easy.md) | [Home](../README.md) | [Next](hard.md)
