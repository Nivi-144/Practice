#include <stdio.h>

void quicksort(int a[], int low, int high) {
    int i = low, j = high, pivot = a[low], temp;

    while(i < j) {
        while(a[i] <= pivot && i < high)
            i++;
        while(a[j] > pivot)
            j--;

        if(i < j) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }

    temp = a[low];
    a[low] = a[j];
    a[j] = temp;

    if(low < j)
        quicksort(a, low, j-1);
    if(j < high)
        quicksort(a, j+1, high);
}

int main() {
    int a[100], n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    quicksort(a, 0, n-1);

    printf("Sorted array:\n");
    for(i = 0; i < n; i++)
        printf("%d ", a[i]);

    return 0;
}
