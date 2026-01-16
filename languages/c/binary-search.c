#include <stdio.h>
#define SIZE 6

int main(){
    int key;
    int high = SIZE-1, low = 0, mid;
    int arr[SIZE] = {2,6,11,13,18,20};

    scanf("%d", &key);
    while(high>=low){
        mid = (high+low) / 2;
        if(key == arr[mid]){
            printf("%d", mid);
            break;
        }
        else if(key > arr[mid]){
            low = mid+1;
        }
        else if(key < arr[mid]){
            high = mid-1;
        }
    }
    return 0;
}