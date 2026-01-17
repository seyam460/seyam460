#include<stdio.h>
#include<conio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node* add;
};
struct node *start = NULL, *new1, *temp;
void create();
void display();
void insert_first();
int main(){
    int choice;
    do{
    printf("----linked list menu---");
    printf("\n1.create");
    printf("\n2. display");
    printf("\n3. deleted");
    printf("\n4. insert_first");
    printf ("\n5. exit");
    printf("enter the choice: ");
    scanf("%d",&choice);
    switch (choice){
        case 1:
            create();
            break;
        case 2:
             display();
             break;
        case 3:
            insert_first();
            break;
        printf("invalid choice");
    }
    }while(choice != 5);
}void create(){
int n;
char ch;
printf("enter the number:");
scanf("%d",&n);
start = (struct node*)malloc(sizeof(struct node));
start-> data =n;
start -> add = NULL;
temp = start ;
printf("do you want to continue: ");
ch = getche();
while(ch == 'y' || ch == 'Y'){
    printf("enter next element: ");
    scanf("%d",&n);
    new1 = (struct node*)malloc(sizeof(struct node));
    new1->data = n;
    new1->add = NULL;
    temp->add = new1;
    temp = temp->add;
    printf("\n do you want to continue");
    ch = getche();}}
void display(){
    if (start == NULL )
        printf("list is not found");
    else {
        temp = start;
        while (temp!= NULL){
            printf("&d",temp->data);
            temp = temp->add;
        }
    }
void insert_first(){
    int n;
    if(start == NULL){
        printf("list is not created");}
    else{
        printf("enter the element for insert: ");
        scanf("%d",&n);
        new1 = (struct node*)malloc(sizeof(struct node));
        new1-> data = n;
        new1-> add =  NULL;
        new1->add = start;
        start = new1;
        printf("Inserted: %d\n", new1->data);
    } }
}
