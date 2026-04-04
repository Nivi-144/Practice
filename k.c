#include <stdio.h>
#include <stdlib.h>
#define MAX 100
struct Edge {
    int u, v, weight;
};
struct Subset {
    int parent;
    int rank;
};
int find(struct Subset subsets[], int i) {
    if (subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);
    return subsets[i].parent;
}

// Union function by rank
void Union(struct Subset subsets[], int x, int y) {
    int rootX = find(subsets, x);
    int rootY = find(subsets, y);

    if (subsets[rootX].rank < subsets[rootY].rank)
        subsets[rootX].parent = rootY;
    else if (subsets[rootX].rank > subsets[rootY].rank)
        subsets[rootY].parent = rootX;
    else {
        subsets[rootY].parent = rootX;
        subsets[rootX].rank++;
    }
}

// Comparator for sorting edges
int compare(const void* a, const void* b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

void kruskal(struct Edge edges[], int V, int E) {
    struct Edge result[MAX];
    int e = 0; // result index
    int i = 0;

    // Sort edges by weight
    qsort(edges, E, sizeof(edges[0]), compare);

    struct Subset subsets[V];
    for (int v = 0; v < V; v++) {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    while (e < V - 1 && i < E) {
        struct Edge next = edges[i++];

        int x = find(subsets, next.u);
        int y = find(subsets, next.v);

        if (x != y) {
            result[e++] = next;
            Union(subsets, x, y);
        }
    }

    printf("Edges in Minimum Spanning Tree:\n");
    int totalCost = 0;
    for (i = 0; i < e; i++) {
        printf("%d -- %d == %d\n", result[i].u, result[i].v, result[i].weight);
        totalCost += result[i].weight;
    }
    printf("Total Cost = %d\n", totalCost);
}

int main() {
    int V = 4; // number of vertices
    int E = 5; // number of edges

    struct Edge edges[] = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    kruskal(edges, V, E);

    return 0;
}
