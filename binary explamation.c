#include<stdio.h>
int binarysearchfirst(int arr[],int n,int k){
    int low=0,high=n-1;
    int result=-1;
    while(low<=high){
        int mid=low+(high-low)/2;
        if(arr[mid] == k){
            result=mid;
            high=mid-1;
        }
        else if(arr[mid]<k){
            low=mid+1;
        }
        else{
            high=mid-1;
        }
    }
    return result;
}
int main(){
    int arr[]={1,1,1,1,2};
    int n=sizeof(arr)/sizeof(arr[0]);
    int k=1;
    int index=binarysearchfirst(arr,n,k);
    printf("%d",index);
    return 0;
}

