#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 탐색 알고리즘의 기초
int main(){
    int user, com, count = 0;
    printf("1부터 100까지 랜덤 숫자 맞추기\n");
    srand(time(NULL));
    com = rand()%100 + 1;
    while(1){
        printf("숫자 입력: ");
        scanf("%d", &user);
        count += 1;
        if(user == com){
            printf("\n목표 숫자: %d\n시도 횟수: %d\n정답입니다!\n", com, count);
            break;
        }
        else if(user > com){
            printf("목표 숫자는 더 작습니다.\n");
        }
        else if(user < com){
            printf("목표 숫자는 더 큽니다.\n");
        }
        else{
            printf("오류\n");
            break;
        }
    }
    
    return 0;
}