#include <stdio.h>

int factorial(int n){
    if (n>=1){
        return n*factorial(n-1);
    }
    else{
        return 1;
    }
}

int main(){
    int num = 0;
    scanf("%d", &num);
    printf("%d",factorial(num));
    return 0;
}