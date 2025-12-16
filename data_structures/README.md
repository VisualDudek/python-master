## Disjoint Set Union (DSU) / Union-Find Data Structure
A Disjoint Set Union (DSU), also known as Union-Find, is a data structure that keeps track of a partition of a set into disjoint (non-overlapping) subsets. It supports two primary operations efficiently:
1. **Find**: Determine which subset a particular element is in. This can be used to check if two elements are in the same subset.
2. **Union**: Join two subsets into a single subset.

Next you have several choices to make:
- Implement path compression in the `find` method to flatten the structure of the tree whenever `find` is called, speeding up future operations.
- Implement union by rank/size in the `union` method to always attach the smaller tree under the root of the larger tree, keeping the overall tree flat.
- Does find on non-existing element raise an error or create a new set?
- Keep track of the size of roots to support size queries (add a `size` method). Here is tricky part to decide whether to keep size of only roots or of all elements. If only roots, then size method needs to find root first. If all elements, then union needs to update size of new root. When merging two sets, size of new root is sum of sizes of both roots and merged root size should be deleted to avoid confusion.
