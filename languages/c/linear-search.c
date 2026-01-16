#include <stdio.h>
#define SIZE 6

int main(){
    int arr[SIZE] = {3, 8, 12, 15, 29, 43};
    int key;
    scanf("%d", &key);
    for(int i = 0; i<SIZE; i++){
        if(arr[i]==key){
            printf("인덱스: %d", i);
            break;
        }
    }
    return 0;
}