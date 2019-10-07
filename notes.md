;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

Search vs. Traversal: matter of goal
The traversal goes everywhere
Search stops when it finds a node you are lookoing for


```
BFT Pseudocode
Create a queue
Create list of visited nodes
Put starting node in the queue
While: queue not empty
Pop first node out of queue
If not visited
     Mark as visited
     Get adjacent edges and add to list
Goto top of loop
```

```
Make a stack
Make visited list
Add first node to stack
While stack not empty:
Pop top item
if not visited:
    Mark as visited
Get adjacent and add to stack
```
