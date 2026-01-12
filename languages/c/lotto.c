#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int temp = 0;
    int lotto[6] = {0};
    srand(time(NULL));
    for(int i = 0; i<6; i++){
        lotto[i] = rand() % 45 + 1;
        // 중복 검사
        for(int j = 0; j<i; j++){
            if(lotto[i]==lotto[j]){ 
                i--;
                break;
            }
        }
    }
    // 버블정렬 알고리즘
    for(int i = 0; i<5; i++){
        for(int j = 0; j<5-i; j++){
            if(lotto[j]>lotto[j+1]){
                temp = lotto[j];
                lotto[j] = lotto[j+1];
                lotto[j+1] = temp;
            }   
        }
    }
    // 배열 출력
    for(int i = 0; i<6; i++){
        printf("%d ", lotto[i]);
    }
    printf("\nFinish\n");

    return 0;
}