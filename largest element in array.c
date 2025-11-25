#include<stdio.h>
int findlargest(int arr[],int n){
    int max=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>max)
            max=arr[i];
    }
    return max;
}
int main(){
    int arr[]={1,2,5,78,90};
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("largest element:%d\n",findlargest(arr,n));
    return 0;
}
