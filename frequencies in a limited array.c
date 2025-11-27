#include<stdio.h>
void countfrequency(int arr[],int n,int freq[]){
    for(int i=0;i<n;i++){
       freq[i]=0;
    }
    for(int i=0;i<n;i++){
        int val=arr[i];
        freq[val-1]++;
    }
}
int main(){
    int arr[]={2,3,2,3,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    int freq[n];
    countfrequency(arr,n,freq);
    printf("output:[");
    for(int i=0;i<n;i++){
        printf("%d",freq[i]);
        if(i!=n-1)printf(",");
    }
    printf("]\n");
    return 0;
}
