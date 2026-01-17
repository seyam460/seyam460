#include<stdio.h>
int main(){
    int n,d;
    printf("the number of left rotation to perform: ");
    scanf("%d",&d);
    printf("enter the size of an array: ");
    scanf("%d",&n);
    int arr[n];
    for (int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    d = d%n;
    for (int i=d;i<n;i++){
        printf("%d",arr[i]);
    }
    for (int i=0;i<d;i++){
        printf("%d",arr[i]);
    }
    return 0;
}
