#include<stdio.h>

int x[10], a[10][10], n;
void nextValue(int k)
{
    while(1)
    {
        x[k] = (x[k] + 1) % (n + 1);

        if(x[k] == 0)
            return;

        if(a[x[k-1]][x[k]] != 0)
        {
            int j;

            for(j=1; j<k; j++)
            {
                if(x[j] == x[k])
                    break;
            }

            if(j == k)
            {
                if((k < n) || (k == n && a[x[n]][x[1]] != 0))
                    return;
            }
        }
    }
}

/* Hamiltonian function */
void hamiltonian(int k)
{
    while(1)
    {
        nextValue(k);

        if(x[k] == 0)
            return;

        if(k == n)
        {
            printf("\nHamiltonian Cycle: ");

            for(int i=1; i<=n; i++)
                printf("%d ", x[i]);

            printf("%d", x[1]);
        }
        else
        {
            hamiltonian(k+1);
        }
    }
}

int main()
{
    printf("Enter number of vertices: ");
    scanf("%d",&n);

    printf("Enter adjacency matrix:\n");

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }

    x[1]=1;     // Start from vertex 1

    hamiltonian(2);

    return 0;
}
