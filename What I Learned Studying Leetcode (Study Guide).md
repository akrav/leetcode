
---

## What I Learned Studying Leetcode (Page 1)
#### By Adam Kravitz


### Recursion

- **Graph DFS**, **Dynamic Programming**, and **Backtracking** all have the same principles.

- All these problems are made easier by creating a “helper” recursive function to call, then returning the answer in the main function.

- All recursive functions start with an **if** condition for either a **base case** or a **success state**, and then return.

- All recursive functions can also have a second **if** condition to check whether the current state has already been calculated. You can do this by keeping a record/dictionary that represents visited/memo-ed paths. If the “key” is in the dictionary already, return the stored value.

- After that, consider the concept of **choices**. In other words, given where we are, what are the possible next moves?
    - Next moves can often be iterated with a loop (most commonly a **for** loop).
    - If the moves are a fixed set, you can just hard-code these paths (e.g., in a binary tree, `root.left` and `root.right`).

- Before calling the recursive function, "**prune**" impossible or invalid choices (or in other words do not call the recursive function on impossible or unhelpful choices):
    - For instance, skip duplicates or check whether the next choice even exists.
    - In a binary tree, for example, check if `root.right` exists before recursing.

- Once you have a valid set of choices (i.e., only choices that make sense), you then call the recursive function.

---

## Recursion (Page 2)

To call a recursive function, there are important principles to understand:

### Principle 1: All Recursive Functions Follow “Backtracking” Principles

- This means there are some variables we care about that we will pass into the recursive function.

- Before we call the function, we make some change to those variables, call the function, passing the changed variables as parameters, and then after the call, **undo** those variable changes.

These variable changes can appear in two ways:

1. **Explicit** backtracking variable changes.
2. **Implicit** backtracking variable changes.

### Principle 2: Implicit Backtracking

- When you call a recursive function, you can make changes to variables at the same time you are passing them in to a function as a parameter.

- The deeper (recursive) level “sees” the changed values, but the current recursive level the function is called on, does not see the changed values. 
	- When you can make changes to variables at the same time you are passing them in to a function, you are not explicitly showing the “undo” step in the code.

**Example**:

```python
def recursive(root, depth):
    # ...
    # Recursive call with an incremented depth
    recursive(root.left, depth + 1)
```

- **Pro**: Cleaner, simpler-looking code.
- **Con**: It does not explicitly show what’s happening to the variables, which can cause confusion.


---

## Recursion (Page 3)

### Principle 3: Explicit Backtracking

- Before you call a recursive function, you can make changes to the variables that will be passed as parameters.

- Then call the recursive function using those changed variables as the parameters.

- After the recursive function returns, you have to **revert** your variable changes to what they were before.

**Example**:

```python
def recursive(root, depth):
    # Explicit variable change
    curr_root = root  # Save current state
    root = root.left
    depth = depth + 1

    # Recursive call
    recursive(root, depth)

    # Explicitly undo changes
    root = curr_root
    depth = depth - 1
```

- **Pro**: Clear, explicit understanding of what the code is doing.
- **Con**: More code, can be harder to read and messier.

### Principle 4: Explicit Backtracking Is Functionally the Same as Implicit Backtracking

- After calling the recursive function based on all our choices, we can store the information we learned in a visited/memo-ed dictionary and then return to finish the function.

---

## Recursion Page 4

**Now we have a basic structure of a recursive function call, which looks like this:**

```python
def recursive(root, depth):
    # Base case or success case condition
    if root is None:
        # store some info here if applicable or do nothing
        # ...
        return ...
    
    # Check memo/visited to not recalculate
    if root in memo.keys():
        return memo[root]  # return the known value
    
    # Choices loop (can be a while loop, a for loop, or hard-coded choices)
    for child in root.children:
        # Condition to check if the choice makes sense to calculate; if not, skip
        if child.val < 0:
            continue  # Skipping negative nodes
        
        # Explicit (or implicit) variable changes; here, explicitly:
        curr_root = root
        root = child
        depth = depth + 1
        
        # Recursive call
        recursive(root, depth)
        
        # Undo explicit changes
        root = curr_root
        depth = depth - 1
    
    # Store result in memo
    memo[root] = ...
    
    # Can return memo[root] or nothing
    return ...
```

> **Above** is an example of a full recursive function format.

---

## Recursion Page 5

With a basic recursion function structure set, there are a few more principles to recursion we should understand:

### Principle 1

Some variables, if passed as a parameter in a recursive function, **retain “memory”** all across the recursion “stack” calls. Meaning, if you add a variable to a list, for example, that variable will remain in that list all the way to the last recursive call (as long as you don’t explicitly remove that variable).

- These variables are called **mutable variables**. These include **lists, sets, dictionaries, and most objects (classes)**.
    
- Let’s say you pass a list as a variable to a recursive function. In the recursive function, you add elements to that list. The list you passed in will retain that information.
    

**Example**:

```python
new_list = []
recursive(new_list)

return new_list  
# new_list will retain info even though it was initially set to []
# because the recursive function modified it.
```

- If you want to append a state of a **mutable** variable (list, set, object) to a **new** list, you need to **deep copy** it. Mutable variables are usually pointed to by reference, so you must store the data/state using a copy operation to avoid unintended modifications.

---

## Recursion Page 6

### Principle 2

Some variables, if passed as a parameter in a recursive function, **do not** retain “memory” across the recursive “stack” calls. Meaning, if you set a variable to some value at recursion “level A” (pass it as a parameter) and then change it at “level B,” the variable at the first recursion level will not be affected by the second recursion level’s change.

- These variables typically include **integers, floats, strings,** and **booleans** (i.e., immutable types).

---

With these added principles, we can now refine our basic recursive function structures.

- If a question asks for paths, lists, combinations, or permutations, you can create a **parent function** that creates a `result = []` variable. Within that parent function, you can then define a nested function to be **recursive function** (in other words a "helper" function).

- The recursive function’s **first condition** can check for the **success state** rather than a base case, since we need a condition to identify when to add **final results** are able to be added to the result variable.

- If you are finding the success state (e.g., building an answer), you typically don’t need a memo or path record. Instead, once you reach the success state, you can append a **copy** of the current state to `result`.

**Example**:

```python
def parent(...):
    result = []

    def recursive(...):
        # success state
        if success_state:
            result.append(state.copy())
            return
        
        # Otherwise, keep exploring/recursing
        # ...
        # ...
    
    recursive(...)  # Call the inner recursive function
    return result
```

Here, `result` accumulates all valid solutions or states discovered by the recursion.


---

## Recursion Page 7

1. **If a question asks for integer, floats, bool, string, max,  or min values**, then the first condition should be a **base case** identifier  instead of a **success state** identifier, and we should then **return** a value.

2. A variable should be set for all recursive calls; then, some variable manipulation should be done to return the final result.
    - These manipulations can be: `min`, `max`, addition, subtraction, multiplication, division, or conditional logic (`or`, `and`, `xor`, etc.).
    - Since we are focusing on a base case (making simpler problems), this is also a good place to use **memo/visited dictionaries** if states may repeat.

### Example

```python
def parent():
    def recursive(root):
        if root is None:
            return 0
        
        if root in memo.keys():
            return memo[root]
        
        left_depth = recursive(root.left) + 1
        right_depth = recursive(root.right) + 1
        
        memo[root] = max(left_depth, right_depth)
        return memo[root]
```

- Now, `memo` / `visited` is only needed if you might see the **exact same state/position** again. Otherwise, you can remove it.

#### Example Without Memo

```python
def recursive(root):
    if root is None:
        return 0
        
    left_depth = recursive(root.left) + 1
    right_depth = recursive(root.right) + 1
    
    return max(left_depth, right_depth)
```

---

## Page 8 — Pointers

In LeetCode, there are 3 major types of questions that use pointers:

1. The **2-pointer approach**
2. **Sliding window** questions
3. **LinkedList** (fast & slow pointers)

### General Overview

- Traditionally, in pointer questions, we deal with data that can be represented as 1D (an array) of data, or in other words: **strings**, **lists/arrays**, **linked lists**, etc.
    
- In 1D pointer questions, there are actually 8 variations of pointers we can use:
    
    1. **Left & Right Pointer**
        
        - Pointers set at the beginning and end of the 1D data.
        - Using logic, move `left` or `right` closer to the opposite side (until `left` and `right` overlap).
        - In a **sliding window**, both pointers might start at one end and move in the same direction—`right` moves first until a condition is met, then `left` adjusts, etc.
    2. **Min Left & Min Right**
        
        - These pointers follow the `left` and `right` pointers respectively.
        - When the `left` pointer moves and we find a new minimum value (or condition), we record that in `min_left`.
        - Similarly, for the `right` pointer, we store the new minimum in `min_right`.
    3. **Max Left & Max Right**
        
        - These follow the `left` and `right` pointers as well.
        - When `left` moves and we find a new maximum value for that position, we record it in `max_left`.
        - Similarly for the `right` pointer, we record the maximum in `max_right`.
    4. **Slow & Fast (almost always for linked lists/graphs)**
        
        - These pointers are used to travel a list where `slow` moves 1 unit at a time and `fast` moves 2 units at a time (e.g., `slow = slow.next`, `fast = fast.next.next`).
        - This is useful for several purposes, commonly:
            1. **Finding a linked list’s midpoint** (if the list has an odd number of nodes, `slow` lands exactly on the midpoint; if even, `slow` lands at the end of the first half).
            2. **Detecting loops** (when `slow` meets `fast`, you have a cycle).
            3. **Finding the start of a loop** (once a loop is detected, there’s a classic trick to locate the start node of that cycle).

#### Diagram for Odd Number of Nodes

```
o -> o -> o -> o -> o
          ^
       midpoint
```

#### Diagram for Even Number of Nodes

```
o -> o -> o -> o
     ^
"midpoint" (often the node right before the true center)
```

---

## Page 9 — Pointers (Continued)

### Slow & Fast (continued)

- **Find Loops**:  
    If a loop is in a linked list or graph, the `fast` pointer will eventually get stuck in the loop, and at some point the `slow` pointer will also end up in the loop. When `slow` intersects `fast`, we know we are in a loop.
    
    A simple arrow diagram could be:
    
    ```
    o -> o -> o -> o -> o -> o
                   ^         |
                   |_________|
    ```
    
    When `slow` and `fast` meet inside that cycle, we’ve detected the loop.
    
- **Trick** (Finding Graph Intersect or Cycle Beginning):
    
    1. Once `slow` and `fast` meet (detecting a cycle), move **one or both** pointers to a “head” position.
    2. Then, move **all pointers** 1 unit at a time.
    3. When `slow` meets `fast` again, that position is where the cycle starts (or where lists intersect).

#### Intersect 2 Linked Lists

- You have two heads: `head1` and `head2`.
- Move both pointers (`p1` starting at `head1`, `p2` starting at `head2`) one unit at a time.
- When one pointer reaches the end, set it to the other head.
- Eventually, the pointers will meet at the intersecting node (or both become `None` if no intersection exists).

A rough ASCII diagram:

```
round1: p1 (head1) -> 0 -> 0 -> 0 \
                                   0 -> 0 -> 0 -> 0
        p2 (head2) -----------> 0 /

After one pointer reaches the end, point it to the other head:

round2: p1 = head2
        p2 = head1

They continue until they meet at the intersection (Goal).
```

#### Find Where Cycle Starts

1. First, find the loop (where `slow == fast`).
2. Then move **one pointer** (either slow or fast but not both) back to the head of the linked list.
3. Move both pointers 1 unit at a time.
4. When they meet again, that node is the **start** of the cycle.

---

## Page 10 — Pointers Continued

### 1. 2-Pointer Approach

- The most generic form of 2 pointers: pointers generally start on opposite ends of a “list” of data and slowly move toward each other until a condition is met (or they cross).
- Alternatively, 2 pointers can start in the middle of a “list” and move **outward** slowly, depending on the problem.

### 2. Sliding Window

- A 2-pointer approach with `left` and `right` pointers, usually moving in the **same** direction.
- The `right` pointer advances until a certain condition is broken or satisfied, then the `left` pointer moves to restore or maintain the desired condition.
    - For example, in a size-based window:
        
        ```python
        for loop over fixed-size window
        ```
        
        ```python
        while right < len(data_list):
            # expand right, then move left if needed
        ```
        

> **Note**: With 2 pointers, be careful about starting and ending positions, since the data being traversed might have an odd or even number of elements.

---

## Linked Lists

### Removal: Remove a Node from a Linked List

```python
prev = head
current = head.next

# removal part
prev.next = current.next
current = current.next
```

(Above is a simplified snippet illustrating how you might skip/remove a node after `prev`, assuming `current` is the node to remove.)

---

## Page 11 — Linked Lists (Continued)

### Midpoint

To find the midpoint of a linked list:

- If the number of nodes is **odd**, you get the exact middle node.

- If the number of nodes is **even**, you end up on the node **just before** what would be the “non-existent” single midpoint.

#### Diagram for Odd Number of Nodes

```
o -> o -> o -> o -> o
          ^
       midpoint
```

#### Diagram for Even Number of Nodes

```
o -> o -> o -> o
          ^?
"midpoint" (often the node right before the true center)
```

#### Code Example

```python
slow = head
fast = head

# Find midpoint
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# When the number of nodes is odd: 
midpoint = slow
# When the number of nodes is even: 
midpoint = slow.next  (depending on how you define “midpoint”)
```

### Reversal: Reverse a Linked List

For example, `1 -> 2 -> 3` becomes `3 -> 2 -> 1`.

#### Code

```python
current = head
prev = None

# reversal
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
```

After this loop, `prev` is the new head of the reversed list.

---

## Page 12 — Linked List (Continued)

### Merge

**Given 2 lists, merge the two lists back and forth between them.**

#### Code (Pseudo Example)

```python
L1 = head_1
L2 = head_2
dummy = ListNode()  # a temporary dummy node
current = dummy

while L1 and L2:
    current.next = L1
    L1 = L1.next
    
    # "swap" step
    temp = L2
    L2 = L1
    L1 = temp
    
    current = current.next  # move to next
    


# If one list is not fully traversed, attach the remainder
if L1:
    current.next = L1
elif L2:
    current.next = L2

return dummy.next
```

Or

```python
dummy = ListNode()
dummy.next = head
curr = dummy

head1 = head
head2 = prev

is_odd = True
while head1 and head2:
	if is_odd:
		curr.next = head1
		head1 = head1.next
	else:
		curr.next = head2
		head2 = head2.next
	curr = curr.next
	is_odd = not is_odd
	

if head1:
	curr.next = head1

if head2:
	curr.next = head2

return dummy.next
```

Or

```python

dummy = ListNode()
tail = dummy

is_odd = True
while head1 and head2:
	if is_odd:
		tail.next = head1
		head1 = head1.next
	else:
		tail.next = head2
		head2 = head2.next
	tail = tail.next
	is_odd = not is_odd
	

if head1:
	tail.next = head1

if head2:
	tail.next = head2

return dummy.next
	

```

(This is a rough illustration of weaving the nodes from two lists. The exact logic can vary based on your merge strategy.)

---

## DFS & BFS — Iterative Approach

- **DFS (Depth-First Search)** uses a **stack** to explore the deepest path possible, then “recurses” back up to explore other paths to their deepest point.
    
    - DFS can be recursive, which internally uses the built in recursive call stack in the code
    - DFS can be iterative where you can explicitly use your own stack data structure (stack = []) to simulate recursion.
    

### Iterative Approach Notes

- **Pro**: The “recursive stack” has a smaller limit on stored data than a dedicated iterative stack. Creating your own stack for DFS allows you to handle much larger problems if recursion depth is a concern (stack overflow).
- **Con**: The iterative approach is more verbose, making it more complex to read and understand.


---

## Page 13 — DFS & BFS Iterative Approach (Continued)

### DFS (continued)

#### Code Example (Iterative DFS)

```python
visited = []
stack = [root]

while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        
        # For loop over neighbors is a generic form of adding nodes to a stack
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
```

**Note**:

- `visited` is only needed if there’s a chance to see the same node twice (e.g., in graphs or trees that could contain cycles or repeated nodes). For strictly acyclic trees with all unique nodes, a visited list might not be necessary.
- In the generic “for neighbor in node.neighbors” approach, you can explicitly check:
    1. Whether `neighbor` exists.
    2. Whether `neighbor` is not visited.

Or, in a simple binary tree, you might just do:

```python
if node.left:
    stack.append(node.left)
if node.right:
    stack.append(node.right)
```

(without the need for a `visited` set/list, assuming no duplicates).

---

## Page 14 — DFS & BFS Iterative Approach (Continued)

### BFS

- **BFS** uses a **queue** to explore the graph or tree level by level. In other words, BFS checks all the neighbors before going deeper.

- Because BFS checks level by level first, it **cannot** be done recursively in the same straightforward manner as DFS (which uses the call stack). Instead, BFS in code typically involves a queue.

#### Code 1 (Implicit “level” BFS)

```python
visited = []
queue = [root]

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
```

#### Code 2 (Explicit “level” BFS)

```python
visited = []
queue = [root]

while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
```

In this second version, we explicitly handle each “level” of the graph/tree, which can be useful for problems that require processing data level by level (e.g., a typical “level order traversal” of a binary tree).

---

## Page 15 — Permutations

A **permutation** is a list of all possible arrangements of a collection where **order matters**. For example, `[1,2]` is different from `[2,1]`. Permutations are often generated using **backtracking**.

There are two types of permutation backtracking approaches to consider:

1. When the permutation length is the **same** as the input length. (This is the common “all permutations” scenario.)
2. When you want a permutation of a **certain length** from a larger input dataset (partial permutations). This can be coded in a way similar to combination problems, but with order taken into account.

Below is an example for the **first** approach (permutation length == input length).

### Code 1 (Permutation length == input length)

```python
def perm(self, nums):
    # Optionally sort nums if you need to handle duplicates
    nums.sort()

    result = []

    def backtracking(start):
        # If 'start' has reached the end, we've formed a complete permutation
        if start == len(nums):
            result.append(nums[:])  # nums[:] is a copy of nums
            return
        
        # Explore all possible swaps at the current 'start' position
        for i in range(start, len(nums)):
            # (Optional) If you want to skip duplicates:
            if i > start and nums[i] == nums[start]:
                continue

            # Swap nums[start] with nums[i]
            temp = nums[start]
            nums[start] = nums[i]
            nums[i] = temp

            # Recurse on the next position
            backtracking(start + 1)

            # Undo the swap after backtracking
            temp = nums[start]
            nums[start] = nums[i]
            nums[i] = temp

    backtracking(0)
    return result
```

- **Key Points**:
    - Instead of swapping shown above in python you can swapping in-place (`nums[start], nums[i] = nums[i], nums[start]`) saves space compared to creating a new list every time.
    - Always **undo** the swap after the recursive call, so the list state is restored for the next iteration.


---

## Page 16 — Permutations (Continued)

### Code 2: All Permutations (where `len(path) < len(input_data)` until we reach the desired length)

> **Note**: This approach is similar to the combinations code, but we allow **reordering** (since order matters). We can also handle **duplicate** numbers by sorting and skipping duplicates.

```python
def perm(self, nums):
    result = []
    path = []
    used = [False] * len(nums)

    # Sort if you want to handle duplicates (not needed if no duplicates)
    nums.sort()

    def backtracking():
        # If we want a full permutation of the entire list:
        if path: # or if looking for a specific permutation size len(path) == len(nums)
        
            result.append(path[:])
            
            # can "return" here if, if statement is looking for a specific permutation size
            #return

        for i in range(len(nums)):
            # Skip already-used elements
            if used[i]:
                continue
            
            # Skip duplicates if the current num is the same as the previous,
            # and the previous was NOT used
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # Choose
            used[i] = True
            path.append(nums[i])

            # Explore
            backtracking()

            # Undo
            used[i] = False
            path.pop()

    backtracking()
    return result
```

- **Key Points**:
    - `used[i]` tracks whether we’ve included `nums[i]` in the current permutation path.
    - Sorting + checking `nums[i] == nums[i-1]` (and `not used[i-1]`) is a common technique to skip duplicate permutations.

---

## Page 17 — Combinations

A **combination** is a list of all possible selections where **order does not matter**.  
For example, `[1,2]` is the same as `[2,1]`. You can generate combinations using **backtracking**.

### Example Code

```python
def combine(self, candidates, k):
    result = []
    combination_arr = []

    # Sort if you need to skip duplicates
    candidates.sort()

    def backtracking(start, combination_arr):
        # If we've chosen 'k' elements, add a copy to the result
        if len(combination_arr) == k:
            result.append(combination_arr[:])
            return

        for i in range(start, len(candidates)):
            # Skip duplicates if the current candidate == previous candidate,
            # and we haven't used the previous candidate in this loop
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # Choose
            combination_arr.append(candidates[i])
            i += 1
            # Explore with i+1 to avoid reusing the same element index
            backtracking(i, combination_arr)

            # Undo
            combination_arr.pop()
            i -= 1

    backtracking(0, combination_arr)
    return result
```

- **Key Points**:
    - We pass `i + 1` to `backtracking` so each element can only be used once.
    - Sorting + the duplicate check (`if i > start and candidates[i] == candidates[i - 1]`) skips identical candidates at the same decision level.

---

## Page 18 — Topological Sort

**Topological sort**:  
A graph traversal algorithm (often using **DFS** or **BFS**) that finds an ordering of the nodes such that if there is an edge `u -> v`, then `u` appears before `v` in the ordering.

- The goal is also to detect a cycle in a directed graph. If a cycle exists, no valid topological ordering is possible.
- If no cycle exists, we return a list of nodes in an order that respects all directed edges (“dependencies”).

### DFS Approach

Since DFS can be done **iteratively** or **recursively**, both methods can work for topological sort. However, the recursive DFS is often more intuitive to write, and if an iterative approach is desired, many people prefer BFS (a.k.a. **Kahn’s Algorithm** for topological sorting).

#### Example: Building an Adjacency List

```python
from collections import defaultdict

def build_adjacency_list(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph


def topological_sort(self, n, edges):
    # Build adjacency list from edges
    graph = self.build_adjacency_list(n, edges)

    visited = [False] * n                 # Tracks whether a node is fully processed (no loop found)
    recursive_stack_visited = [False] * n # Tracks nodes currently in the recursion stack
    result = []                           # Will hold nodes in post-order

    def dfs(node):
        # If this node is already in the recursion stack, we have a loop
        if recursive_stack_visited[node]:
            return False
        
        # If fully visited, no loop here; return True
        if visited[node]:
            return True
        
        # Mark node as in the recursion stack
        recursive_stack_visited[node] = True

        # Recurse on all neighbors
        for neighbor in graph[node]:
            if not dfs(neighbor):  # If any neighbor leads to a loop
                return False

        # Undo the recursion stack marking
        recursive_stack_visited[node] = False
        
        # Mark fully visited and append to result (post-order)
        visited[node] = True
        result.append(node)
        return True

    # Run DFS from every unvisited node
    for v in range(n):
        if not visited[v]:
            if not dfs(v):
                # Loop found; no valid topological ordering
                return []

    # If no loop, 'result' is in reverse topological order (due to post-order appending)
    return result[::-1]  # Reverse it to get the correct topological order
```

- **Key Steps**:
    1. `recursive_stack_visited[node] = True` before exploring neighbors.
    2. If we ever see a node that’s already in the recursion stack, we have a cycle, so return `False`.
    3. Once done exploring neighbors, set `recursive_stack_visited[node] = False` and `visited[node] = True`, then append `node` to `result`.
    4. After all nodes are checked, if no loop was found, reverse `result` because it’s built in **post-order**.

---

## Page 20 — DFS Recursive Code Explained & BFS Approach

### DFS Recursive Code (Recap)

- **DFS** uses a **recursive stack** to check for loops. If DFS for a node finds no loops, we mark it visited and add it to our post-order result list. Repeat for all nodes.

### BFS Approach (Kahn’s Algorithm)

An **iterative** approach that also produces a topological order if no cycle exists:

1. **Build** an adjacency list for the graph.
```
u -> v
```

| key | value |
| --- | ----- |
| u   | v     |


2. **Compute** the **indegree** of each node (the number of incoming edges).
```
u -> v
```

| key | value |
| --- | ----- |
| u   | 0     |
| v   | 1     |

3. Initialize a queue with all nodes whose indegree is `0` (An indegree of 0 means there are no dependencies on that node).
4. We can then explore 0 indegree nodes neighbors and remove 1 from those neighbors indegree values
5. If those neighbors indegree is now 0 after the adjustment we can then add that node to the queue to be visited

#### Example Helpers

```python
from collections import defaultdict

def build_adjacency_list(self, num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph

def compute_indegrees(self, num_nodes, edges):
    indegree = defaultdict(int)
    # Make sure every node is in indegree, even if it stays 0
    for i in range(num_nodes):
        indegree[i] = 0

    for u, v in edges:
        indegree[v] += 1

    return indegree
```

---

## Page 21 — Topological Sort (Continued)

### Code: BFS (Kahn’s Algorithm) Approach

```python
def topological_sort(self, num_nodes, edges):
    graph = self.build_adjacency_list(num_nodes, edges)
    indegree = self.compute_indegrees(num_nodes, edges)

    # Initialize queue with all nodes of indegree 0
    queue = []
    for node in range(num_nodes):
        if indegree[node] == 0:
            queue.append(node)

    result = []

    # Process the queue
    while queue:
        current_node = queue.pop(0)
        result.append(current_node)

        # For each neighbor, reduce its indegree by 1
        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1
            # If indegree is now 0, add to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If we didn't include all nodes, there's a cycle
    if len(result) < num_nodes:
        return []

    return result
```

- **Key Points**:
    - If a cycle exists, some nodes will never reach indegree `0`, so they won’t appear in `result`.
    - We detect a cycle by comparing `len(result)` to `num_nodes`. If it’s smaller, return `[]`.

### Undirected Graph BFS (Kahn's Algorithm)
- Notice that the indegree leaf nodes now have values of 1 due to the nature of how undirected graph nodes are connected
- Also notice the line in the while loop
	- indegree[curr] -= 1 
- The above line is needed only for undirected Kahn's Algorithm. This line is needed since undirected graphs inherently have cycles because of the nature of undirected graph edges. The indegree[curr] -= 1  is needed to remove those cycles. 
- In other words, since undirected edges are cycles, we need to remove the current node and its neighbor

```python
class Solution:

	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

		n = len(edges) + 1 # a tree stucture has n nodes and n-1 edges
		graph = defaultdict(list)
		indegree = defaultdict(int)

  

		for a, b in edges:
			graph[a].append(b)
			graph[b].append(a)
			indegree[a] += 1
			indegree[b] += 1

		q = []
		for i in range(n):
			if indegree[i] == 1:
				q.append(i)

  

		while q:
			curr = q.pop()
			indegree[curr] -= 1 
			
			for neighbor in graph[curr]:
				indegree[neighbor] -= 1
				
				if indegree[neighbor] == 1:
					q.append(neighbor)

  

		for a, b in reversed(edges):
			if indegree[a] == 2 and indegree[b] != 0:
				return [a, b]

		return []
```


Below are four new sections—**Binary Search**, **Tabulation**, **Basic Sorting & Searching Patterns**, and **Complexity Analysis**—written in a style similar to your existing study guide. Feel free to adjust page numbering and formatting as needed.

---
## Dijkstra’s Algorithm

**Dijkstra’s Algorithm** finds the shortest path from a single source to all nodes in a graph with **non-negative** edge weights. It’s typically implemented with a **priority queue** (heap) to always expand the node with the **smallest** known distance/time so far.

### Key Points

- **Graph Representation**: Usually an **adjacency list**. For each node `u`, we store pairs `(neighbor, weight)`.
- **Distance/Time**: We keep a **distance array** (or dictionary) that stores the best known distance from the source to each node.
- **Priority Queue**: A min-heap, always pops the node with the smallest distance so far.
- If a popped node is already visited, skip it. Otherwise, update neighbors’ distances if we find a better path.

### Code Example (Iterative with Priority Queue)
```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        visited = {}
        
        q = [(0, k)]

        result = 0 
        while q:
            time, curr = heapq.heappop(q)
            if curr in visited:
                continue
            result = time
            visited[curr] = True

            for neighbor, neighbor_time in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(q, (neighbor_time + time, neighbor))

        print(visited)
        return result if len(visited) == n else -1

```

**Note**:

1. We do `(distance, node)` in the heap so it sorts by the **smallest distance** first.
2. If we pop a node that’s already `visited`, we skip it (that means we already found a better route).
3. Each time we find a better path to `neighbor`, we push `(new_dist, neighbor)` into the heap.

---

## Prim’s Algorithm

**Prim’s Algorithm** finds a **Minimum Spanning Tree (MST)** in a weighted **undirected** graph. It’s somewhat similar to Dijkstra’s approach with a priority queue, except we track the **cost** to connect each unvisited node to the MST, rather than shortest paths.

### Key Points

- **Starting Node**: We pick any node as a start (Prim’s doesn’t require a “source,” just a place to begin the MST).
- **Priority Queue**: We push `(cost, node)`. The “cost” is how cheaply we can connect this node to the growing MST.
- **Visited**: Once we pop `(cost, curr)`, if it’s unvisited, we add `cost` to our MST total cost, mark it visited, and push its edges to the queue with the new potential costs.
- We continue until we’ve visited all nodes (or can’t proceed if the graph is disconnected).

### Code Example (Iterative with Priority Queue)
```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                man_dist = abs(x2-x1) + abs(y2-y1)
                graph[i].append([man_dist, j])
                graph[j].append([man_dist, i])
                

        q = [[0,0]] #cost point
        result = 0
        visited = {}

        while q:
            cost, curr = heapq.heappop(q)
            if curr in visited:
                continue
            
            result += cost

            visited[curr] = True

            for n_cost, neighbor in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(q, [n_cost, neighbor])
        
        return result
```

**Note**:

1. For MST, the cost we push is just the **edge weight** to connect `neighbor`.
2. We pop the smallest `(cost, node)` from the queue. If unvisited, that cost is the cheapest edge connecting `node` to the MST, so we add `cost` to `mst_cost`.
3. We only set the node as visited **once** and add its neighbors with `(weight, neighbor)` to the heap.
4. If we end with `visited_count < n`, the graph wasn’t connected.

---

**Comparing Dijkstra vs. Prim**:

- **Dijkstra**: The “priority queue cost” is the **distance from the source**. We keep a `dist[]` array updated as we find shorter paths.
- **Prim**: The “priority queue cost” is the **weight** to connect a new node to the existing MST. We keep a **visited** set to track which nodes are in the MST.
- Implementation details look quite similar: `(cost, node)` in a min-heap, a visited set, repeated extraction of the smallest cost.
- ###### ==Note: The difference in how cost is added and pushed to the priority queue between **Dijkstra** and  **Prim** algorithm is because Dijkstra is getting a full path from a source node, while Prim does not care about a path it just wants the cheapest connection==

---
# Chatgpt Additional Section Notes
## Page XX — Binary Search

Binary Search is used to **find a target** (or boundary condition) in a **sorted** array or range in **O(log n)** time.

1. **Core Idea**
    
    - Start with two pointers: `left` at the beginning, `right` at the end.
    - Find the `mid` index: `mid = left + (right - left) // 2.
	    - **Important Note**:  
			When using `mid = left + (right - left) // 2`, we get the floor of the midpoint. This means if we set `left = mid` in a scenario where `mid == left`, we make **no progress**, potentially causing an infinite loop. Instead always use **`left = mid + 1`** (to exclude `mid`) when we know `mid` is not the solution—otherwise.
```python
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		
		while left < right:
			mid = left + (right - left)//2 #flooring mid, meaning left = mid + 1 (thus left cannot have a <= or >= if condition)
			
			if target <= nums[mid]:
				right = mid
			else:
				left = mid + 1
		
		return left if nums[left] == target else -1
```
     - However, if we were using a ceiling-based midpoint, we would adjust the updates accordingly.
```python
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		
		while left < right:
			mid = left + math.ceil((right - left)/2) #ceiling mid, meaning right = mid - 1 (thus right cannot have a <= or >= if condition)
			
			if target < nums[mid]:
				right = mid - 1
			else:
				left = mid
		
		return left if nums[left] == target else -1
```
- Compare the value at `mid` with the target.
        - If `mid_value` == `target`, return `mid`.
        - If `mid_value` < `target`, move `left` to `mid + 1`.
        - Otherwise, move `right` to `mid - 1`.
    - Continue until `left > right` (meaning the target is not found).
2. **Off-by-One Errors**
    
    - Be careful with how you update `left` and `right` in each iteration.
    - Common mistakes involve infinite loops when `mid` calculation or pointer updates are off by 1.
3. **Variations**
    
    - **Leftmost/Rightmost Occurrence**: Keep searching even after finding a match, adjusting `right` or `left` to find the earliest/latest position of the target.
    - **Binary Search on Answer**: When the search space is not an array but a **range** of possible answers (like searching for a minimum capacity or maximum feasible distance).

**Example Code**:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found
```


Below are **two** versions of your same code that only **change** how the **lower_bound** and **upper_bound** row searches are done. One uses a **convergence-style** binary search (`while left < right`), the other uses the **classic-style** (`while left <= right`). **All other code**, including the final per-row search for the target, is unchanged.

---

# 1. Convergence-Style Version (`while left < right`)

In this version, both the lower-bound and upper-bound searches use the “peak element” style (or “boundary convergence” style) approach with `while left < right`. After the loop, `left == right`, and we interpret `left` or `left-1` as needed.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # ------------- LOWER BOUND -------------
        # We want to find the last row <some_condition>.
        # Original code logic:
        #   if target <= matrix[mid][num_cols - 1]:
        #       up = mid - 1
        #   else:
        #       down = mid + 1
        # We'll do a 'convergence' version:
        
        # Meaning: We skip rows where matrix[mid][last_col] >= target -> go left.
        # If matrix[mid][last_col] < target, we go right.
        
        down, up = 0, num_rows - 1
        while down < up:
            mid = (down + up) // 2
            # If target <= matrix[mid][num_cols - 1], then row mid is not strictly < target.
            # So we move up to mid (include mid in next range).
            if target <= matrix[mid][num_cols - 1]:
                up = mid
            else:
                down = mid + 1
        
        # After the loop, down == up.
        # We want the "largest row index r" s.t. matrix[r][last_col] < target.
        # If we ended up on a row whose last_col is >= target, 
        # that means the row is not strictly < target, so the 'largest row' is down-1.
        if matrix[down][num_cols - 1] < target:
            lower_bound = down
        else:
            lower_bound = down - 1
        
        # ------------- UPPER BOUND -------------
        # Original logic:
        #   if target >= matrix[mid][0]:
        #       down = mid + 1
        #   else:
        #       up = mid - 1
        # We'll do the convergence style:
        
        down, up = 0, num_rows - 1
        while down < up:
            mid = (down + up) // 2
            # If target >= matrix[mid][0], then row mid might hold the target or we go even lower
            # (meaning we want to push the boundary downward).
            if target >= matrix[mid][0]:
                down = mid + 1
            else:
                up = mid
        
        # After loop, down == up.
        # If that row's first element is <= target, it's a candidate row, so 'up' is down.
        # Otherwise we should shift one up:
        if matrix[down][0] <= target:
            upper_bound = down
        else:
            upper_bound = down - 1
        
        # ------------- Now do the same final search as your code -------------
        # We look from row = (lower_bound+1) to row = upper_bound inclusive.
        
        for row in range(lower_bound + 1, upper_bound + 1):
            left = 0
            right = num_cols - 1
            # find target in row with classic binary search
            while left <= right:
                mid = (left + right) // 2
                if target == matrix[row][mid]:
                    return True
                elif target < matrix[row][mid]:
                    right = mid - 1
                else:  # target > matrix[row][mid]
                    left = mid + 1
        
        return False
```

**Key Points** (convergence style):

1. We do `while down < up`.
2. We do `mid = (down + up)//2`.
3. We set `up = mid` or `down = mid + 1`.
4. At the end, `down == up`. We interpret that final index carefully (sometimes “take `down - 1`” if we needed a strictly smaller condition).

---

# 2. Classic-Style Version (`while left <= right`)

Here’s the **same** approach but with the **traditional** `while left <= right` pattern and final `left`/`right` interpretation. We do it separately for `lower_bound` and `upper_bound`. This more closely matches your original code, but we re-wrote it for consistency.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # ------------- LOWER BOUND -------------
        # We want to find the "largest row r" s.t. matrix[r][last_col] < target.
        # We'll do a classic while <= approach, then interpret up or down at the end:
        
        down, up = 0, num_rows - 1
        while down <= up:
            mid = (down + up) // 2
            if target <= matrix[mid][num_cols - 1]:
                # This row is NOT strictly less than target
                # So we move 'up' to mid-1
                up = mid - 1
            else:
                # this row's last_col < target, so row mid is valid, we might find a bigger row
                down = mid + 1
        
        # When the loop exits, 'up' is the last row index we found that satisfies 
        # matrix[row][last_col] < target, or -1 if none. 
        lower_bound = up

        # ------------- UPPER BOUND -------------
        # We want to find the "smallest row r" s.t. matrix[r][first_col] > target,
        # or equivalently the last row that might still contain target's range.
        # from your code:
        # if target >= matrix[mid][0]: down=mid+1
        # else up=mid-1
        # So let's do that:

        down, up = 0, num_rows - 1
        while down <= up:
            mid = (down + up) // 2
            if target >= matrix[mid][0]:
                # row mid might be valid for target or we can go further
                down = mid + 1
            else:
                up = mid - 1
        
        upper_bound = up

        # ------------- Final row search -------------
        for row in range(lower_bound + 1, upper_bound + 1):
            left, right = 0, num_cols - 1
            while left <= right:
                mid = (left + right) // 2
                if target == matrix[row][mid]:
                    return True
                elif target < matrix[row][mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False
```

**Key Points** (classic style):

1. We do `while down <= up`.
2. If `condition`, we do `up = mid - 1`, else `down = mid + 1`.
3. After the loop, typically:
    - **Either** `up` (or right) is the “last index satisfying condition,”
	    -  mid value > target (right - 1)
		    - Right in this case will be <= to the target at the end of the search 
		    - last index satisfying condition
    - **Or** `down` (or left) is the “first index not satisfying condition.”
	    - mid value <= target (left + 1)
		    - left in this case will be > the target at the end of the search 
		    - first index not satisfying condition
    - You pick which variable to interpret (`up` or `down`) depending on the logic.

You can see this matches your original approach, just cleaned up and commented.

---

## Final Thoughts

1. **Both** “convergence style” (`while left < right`) **and** “classic style” (`while left <= right`) can do the same job.
2. You just have to carefully decide **which** variable you update (`up = mid` vs. `up = mid - 1`) and how you interpret the final `left` or `up`.
3. In “convergence style,” we typically end with `left == right`. In “classic style,” we often end with `left == up + 1`.
4. Either pattern is fine, as long as the code is consistent. Good luck!

---

## Page XX — Tabulation (Dynamic Programming)

**Tabulation** is a **bottom-up** dynamic programming approach. Unlike memoization (top-down + caching), tabulation **fills out a table/array iteratively**, building from base cases up to the final answer.

### General Steps

1. **Identify States**
    
    - Determine which parameters define the subproblems (e.g., array indices, capacity in knapsack, length of substring).
2. **Initialize a Table**
    
    - Create a table (often a list or 2D array) that will store subproblem results.
    - Base cases are filled in first (e.g., `dp[0] = 0`).
3. **Iterate in Order**
    
    - Fill the table starting from the smallest subproblems up to the final one.
    - Each entry `dp[i]` (or `dp[i][j]`) is computed from previously solved states.
4. **Return Final Answer**
    
    - The last filled entry in the table (`dp[n]`, `dp[m][n]`, etc.) is typically the final solution.

### Example (Fibonacci)

```python
def fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

- **Base Cases**: `dp[0] = 0`, `dp[1] = 1`.
- **Transition**: `dp[i] = dp[i-1] + dp[i-2]`.

---

## Page XX — Basic Sorting & Searching Patterns

Sometimes, interviewers expect you to know (or at least reason about) basic sorting and searching in addition to binary search.

1. **Sorting Algorithms**
    
    - **Merge Sort**: Divide and conquer, O(n log n) time, stable.
    - **Quick Sort**: Average O(n log n), worst O(n²), not always stable.
    - **Heap Sort**: O(n log n), uses a heap data structure.
    - **Built-in Sort**: In many languages, this is often a hybrid of mergesort/insertionsort (Python’s Timsort, for instance).
2. **Linear Search**
    
    - Check each element in O(n). Usually overshadowed by binary search if the data is sorted.
3. **Searching in 2D Matrices**
    
    - Some problems allow “staircase search” from top-right or bottom-left if the rows/columns are sorted.
4. **Important**:
    
    - Know the **complexities** and general behavior of each sort (like stability).
    - In interviews, you rarely code a full mergesort/quick sort from scratch (unless specifically asked), but you might need to explain how it works.

---

## Page XX — Complexity Analysis

Understanding and quickly explaining **Time Complexity** and **Space Complexity** is crucial during interviews. Here are the core ideas:

1. **Time Complexity**
    
    - **O(1)**: Constant time, does not depend on input size.
    - **O(log n)**: Often from dividing the problem space in half each step (binary search).
    - **O(n)**: Linear time, e.g., a simple pass over an array.
    - **O(n log n)**: Commonly found in efficient sorting algorithms.
    - **O(n²)**: Often from nested loops (e.g., checking all pairs).
    - **O(2^n)**, **O(n!)**: Common in backtracking/DFS for subsets, permutations, or generating all combinations.
2. **Space Complexity**
    
    - **Stack space** in recursion problems (e.g., max depth of the recursion tree).
    - Additional data structures such as arrays, hash maps, or priority queues.
    - For example, DFS on a tree might be O(h) space (height h), BFS might be O(w) space (width w).
    - DP arrays or tables can use O(n) or O(n×m) space, etc.
3. **Typical Patterns**
    
    - **DFS/BFS** on a graph: O(V + E) time, O(V) or O(V + E) space.
    - **Backtracking** (e.g., permutations): O(n!) in the worst case.
    - **Dynamic Programming**: Usually O(n) or O(n×m) time/space, depending on the dimension of the DP table.

> Always keep in mind what data structures you’re using and how they grow with input size.

---

**That’s it!** Adjust these sections to fit your desired level of detail and style, but the above provides a concise overview in line with the rest of your study guide.