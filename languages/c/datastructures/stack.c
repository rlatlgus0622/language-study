#include <stdio.h>

    int stack[100];
    int top = -1;

    int is_empty(){
        if(top<0) return 1;
        else return 0;
    }

    void push(int data){
        stack[++top] = data;
    }

    int pop(){
        if(is_empty()) return __INT_MAX__;
        int data = stack[top--];
        return data;
    }


int main(){
    push(0);
    push(1);
    push(2);

    printf("%d", pop());
    return 0;
}