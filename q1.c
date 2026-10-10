#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int price[100], dp[101];
    int n, i, j;

    printf("Enter rod length: ");
    scanf("%d", &n);

    printf("Enter prices for lengths 1 to %d: ", n);
    for (i = 1; i <= n; i++)
        scanf("%d", &price[i]);

    dp[0] = 0;

    for (i = 1; i <= n; i++) {
        dp[i] = 0;
        for (j = 1; j <= i; j++)
            dp[i] = max(dp[i], price[j] + dp[i-j]);
    }

    printf("Maximum obtainable price = %d\n", dp[n]);

    return 0;
}
