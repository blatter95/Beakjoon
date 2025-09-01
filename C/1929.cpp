#include<stdio.h>

int PrimeNum(int num1, int num2) {
    int cnt = 0;
    for (int i = num1; i<=num2; i++){
        if(i == 1) continue;
        cnt = (i % 2 != 0) ? PrimeNum(i, num2) : i;
        printf("%d\n", cnt);
    }
    return 0;
}

int main() {
    int n1, n2 = 0;
    scanf("%d %d", &n1, &n2);
    PrimeNum(n1, n2);
}