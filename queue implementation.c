#include<stdio.h>
#include<conio.h>
#define MAXSIZE 10
int queue[MAXSIZE];
int rear = -1,front = 0;
void insertion();
void deletion();
void display();
int main(){
    int choice;
    do{
        printf("-----queue menu------");
        printf("\n1. insertion");
        printf("\n2. deletion");
        printf("\n3. display");
        printf("\n4. exit");
        printf("enter the choice:");
        scanf("%d",&choice);
        switch(choice){
        case 1:
            insertion();break;
        case 2:
            deletion();break;
        case 3:
            display();break;
        default : printf("invalid choice");
        }
    }while(choice!=4);

}
void insertion(){
    int item;
    if (rear == MAXSIZE-1){
        printf("\nqueue is overflow");
    }
    else{
        printf("enter elements to insert: ");
        scanf("%d",&item);
        rear++;
        queue[rear]= item;
        printf("\n inserted successfully");
    }

}
void deletion(){
    if(front>rear){
        printf("\n queue is empty");
    }
    else{
        printf("\n deleted element: %d",queue[front]);
        front++;

    }
}
void display(){
    int i;
    if (front >rear){
        printf("\n queue is empty");
    }
    else {
        printf("queue elments are:\n");
        for (i=front;i<=rear;i++){
            printf("%d",queue[i]);
        }
    }
}
