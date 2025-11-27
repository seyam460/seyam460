#include<stdio.h>
void movezerostoend(int arr[],int n){
    int j=0;
    for(int i=0;i<n;i++){
        if(arr[i] != 0){
            arr[j]=arr[i];
            j++;
        }
    }

    while(j<n){
        arr[j]=0;
        j++;
    }
}
int main(){
    int arr[]={1,2,0,4,3,0,5,0};
    int n=sizeof(arr)/sizeof(arr[0]);
    movezerostoend(arr,n);
    printf("output:");
    for(int i=0;i<n;i++){
        printf("%d",arr[i]);
    }
    return 0;
}
