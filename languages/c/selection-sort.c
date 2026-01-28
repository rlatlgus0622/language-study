#include <stdio.h>

void swap(int players[], int i, int j){
    int temp = players[i];
    players[i] = players[j];
    players[j] = temp;
}

int main(){
    int players[100];
    int n, k = 0, count = 0;
    scanf("%d %d", &n, &k);
    //players 배열값들 입력
    for(int i = 0; i<n; i++){
        scanf("%d", &players[i]);
    }
    
    for(int i = 0; i<n; i++){
        int least = i; //최솟값 인덱스 i로 설정
        //i+1 ~ n 범위 중에 players[i]보다 최솟값을 가지는 배열의 인덱스 찾아서 least로 설정
        for(int j = i+1; j<n; j++){
            if(players[j]<players[least])
                least = j;
        }
        //제대로 정렬되어있는 경우 교환 안함
        if(i != least){
            swap(players, i, least);
            count++; //교환횟수
        }
        if(count == k)
            break;
    }
    printf("\n%d번의 교환 후 배열: ", count);
    for(int i = 0; i<n; i++){    
        printf("%d ", players[i]);
    }

    return 0;
}