"""
Disjoint Set Union (DSU) or Union-Find data structure implementation.
- Supports union by rank and path compression.
- Allows dynamic addition of elements.
- parent container based on a dictionary for flexibility with element types.
- parent as list also possible for integer elements in a known range.

- Why do I need union by rank?
"""

class DSU:
    def __init__(self, elements=None):
        """
        elements: optional iterable of initial elements
        """
        self.parent = {}
        self.rank = {}

        # Initially each element is its own parent (self root)
        if elements is not None:
            for x in elements:
                self.parent[x] = x
                self.rank[x] = 0

    def find(self, x):
        # lazy initialization for unseen elements
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x

        # GOTCHA: path compression -> flattening the tree
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        # Why do I need union by rank?
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:  # WHAT IS THIS CASE? -> equal rank
            self.parent[ry] = rx
            self.rank[rx] += 1 # GOTCHA: this is counter-intuitive because:
            # When merging two trees of equal height, the resulting tree becomes one level taller because 
            # the root of one tree becomes a child of the root of the other tree 
            # -> increase rank by 1 regardless of what both ranks were.

        return True


def main():
    dsu = DSU(list('ABCD'))
    print(dsu.parent)

    dsu.union('A', 'B')
    print(dsu.parent)


if __name__ == '__main__':
    main()