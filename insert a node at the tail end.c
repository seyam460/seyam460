#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *add;
};
struct node *start = NULL,*new1,*temp;
void create();
void display();
void insert_first();
void insert_last();
int  main(){
    int choice;
    do{
    printf("-----make a linked list------");
    printf("\n1. create");
    printf("\n2. display");
    printf("\n3. insert_first");
    printf("\n4. insert_last");
    printf("\n5. exit\n");
    printf("enter your choice\n");
    scanf("%d",&choice);
    switch (choice){
    case 1:
        create();
        break;
    case 2:
        display();
        break;

    default: printf("invalid choice");
    }
    }
    while(choice!= 5);

}
 void create(){
    int n;
    char ch;
    printf("enter first element");
    scanf("%d",&n);
    start = (struct node*)malloc(sizeof(struct node));
    start->data = n;
    start->add = NULL;
    start = temp;
    printf("do you want to continue\n");
    ch = getche();
    while(ch == 'y' || ch == 'Y'){
        printf("enter next element to insert");
        scanf("%d",&n);
        new1=(struct node*)malloc(sizeof(struct node));
        new1->data = n;
        new1->add = NULL;
        temp->add = new1;
        temp= temp->add;
        printf("do you want to continue");
        ch = getche();
    }}
void display(){
    if (start == NULL){
        printf("list is not found");}
    else{
        temp = start;
        while(temp != NULL){
            printf("%d",temp->data);
            temp = temp->add;
        }
    }
    }
void insert_first(){
    int n;
    if(start==NULL){
        printf("list not found");
    else{
        printf("enter the element for insert");
        scanf("%d",&n);
        new1=(struct node*)malloc(sizeof(struct node));
        new1->data = n;
        new1->add = NULL;
        new1->add = start;
        new1 = start;
    }
    }
    void insert_last(){
        int n;
        if(start == NULL){
            printf("list is not found");
        }
        else {
            printf("enter the element for insert last");
            scanf("%d",&n);
            new1= (struct node*)malloc(sizeof(struct node));
            new1->data = n;
            new1->add= NULL;
            temp = start;
            while(temp->add != NULL){
                temp = temp->add;
                temp->add = new1;
            }
        }
    }
}

