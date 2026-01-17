#include<stdio.h>
#include<conio.h>
#define MAXSIZE 10
int stack[MAXSIZE];
int top = -1;
void push();
void pop();
void display();
int main(){
    int choice;
    do{
    printf("----stack list----");
    printf("\n1. push");
    printf("\n2. pop");
    printf("\n3. display");
    printf("\n4. exit");
    printf("enter number of choice");
    scanf("%d",&choice);
    switch(choice){
    case 1:
        push();break;
    case 2:
        pop();break;
    case 3:
        display();break;
    default: printf("invalid choice");
    }
    while(choice != 4);
    getch();
    return 0;
    }
    void push(){
        int x;
        if(top == MAXSIZE-1){
            printf("stack is overflow");
            return;
        }
    printf("enter the element to push\n:");
    scanf("%d",&x);
    top++;
    stack[top]= x;
    printf("element pushed successfully");
        }
void pop(){
    if(top == -1){
        printf("stack is underflow");
        return;
    }
    printf("\n popped element:%d",stack[top]);
    top--;
}
void display(){
    int n;
    if (top == -1){
        printf("\n stack is empty");
        return ;
    }
    for(int i=top;i>0;i--){
            printf("stack display programme:%d",stack[i]);

    }

}
    }
