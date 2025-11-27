#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    int data;
    node * next;
}node;
node*reverselist(node*head){
    node * prev=null;
    node * curr=head;
    node * nextnode=null;
    while(curr != null){
        nextnode=curr->next;
        curr->next=prev;
        prev=curr;
        curr=nextnode;
    }
    return prev;
}
node * newnode(int data){
    node * node=(node*)malloc(sizeof(node));
    node->data=data;
    node->=null;
    return node;
}
void printlsit(node*head){
    while(head != null){
        printf("%d",head->data);
        head=head->next;
    }
}
    int main(){
        node*head=newnode(1);
        head->next=newnode(2);
        head->next->next=newnode(3);
        head->next->next->next=newnode(4);
        printf("original list: ");
        printlist(head );
        head=reverselist(head);
        printf("\nreversed list: ");
        printlist(head);
        return 0;

}
