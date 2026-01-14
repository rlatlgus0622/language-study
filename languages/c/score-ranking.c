#include <stdio.h>

#define SUBJECTS 3

typedef struct Student{
    char name[20];
    int id;
    int score[SUBJECTS];
    int total;
} Student;

void swap(Student* s1, Student* s2){
    Student temp;
    temp = *s1;
    *s1 = *s2;
    *s2 = temp;
}

int main(){
    Student group[100]; //추후 동적메모리로 구현
    int student_count;
    
    scanf("%d", &student_count);
    
    //추후 포인터 사용해 간소화
    for(int i = 0; i<student_count; i++){
        group[i].total = 0; 
        scanf("%s %d", group[i].name, &group[i].id); //이름, 학번 입력
        for(int j = 0; j<SUBJECTS; j++){
            scanf("%d", &group[i].score[j]); //과목당 점수 입력
            group[i].total += group[i].score[j];
        }
    }
    
    for(int i = 0; i<student_count-1; i++){
        for(int j = 0; j<student_count-i-1; j++){
            if(group[j].total < group[j+1].total || (group[j].total == group[j+1].total && group[j].id > group[j+1].id)){
                swap(&group[j], &group[j+1]);
            }
        }
    }


    printf("\n--- 성적 랭킹 ---\n");
    for (int i = 0; i < student_count; i++) {
        printf("%d등: %s (총점: %d, 학번: %d)\n", i + 1, group[i].name, group[i].total, group[i].id);
    }
    return 0;
}