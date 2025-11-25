#include <stdio.h>
#include <stdlib.h>
typedef struct Node{
    int data;
    struct Node* left;
    struct Node* right;
}Node;

    Node* newNode(int val){
    Node* temp =(Node*)malloc(sizeof(Node));
    temp->data = val;
    temp->left = temp->right = NULL;
    return temp;
}

void leftViewUtil(Node* root, int level, int *maxLevel){
    if (root == NULL) return;
    if (*maxLevel < level){
        printf("%d ", root->data);
        *maxLevel = level;
    }
    leftViewUtil(root->left, level + 1, maxLevel);
    leftViewUtil(root->right, level + 1, maxLevel);
}

void leftView(Node* root){
    int maxLevel = 0;
    leftViewUtil(root, 1, &maxLevel);
}

int main(){
    Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    printf("Left View: ");
    leftView(root);
    return 0;
}

