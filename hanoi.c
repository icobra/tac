#include<stdio.h>

// Ханойская башня
// n дисков с колышка i  на колышек j

int towers(int n, int i, int j){
    int k;
    if (n == 1)
        printf("Переместить диск с %d на %d\n", i, j);
    else {
        k = 6 - i - j;
        towers(n-1, i, k);
        towers (1, i, j);
        towers (n - 1, k, j);
    }
}

int main(){
    towers(3,1,3);
}