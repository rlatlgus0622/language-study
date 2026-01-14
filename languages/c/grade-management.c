#include <stdio.h>

void cal_average(int student_grade[][3], int num, int* ammount, float* average){
    //포인터 사용해서 전역변수 느낌으로 사용
    *ammount = 0;    
    for(int j = 0; j<3; j++){
            *ammount += student_grade[num][j];    
        }
        *average = *ammount/3.0;

}

int main(){
    int student_grade[2][3] = {{90, 80, 80},{95, 90, 95}};
    for (int num = 0; num < 2; num++) {
        int ammount = 0;
        float average = 0.0;

        cal_average(student_grade, num, &ammount, &average);
        printf("%d번 학생 - 총점: %d, 평균: %.1f\n", num + 1, ammount, average);
    }
    return 0;
}