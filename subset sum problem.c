#include<stdio.h>
int main(){
    int n,sum;
    printf("enter number of elements: ");
    scanf("%d",&n);
    int arr[n];
    printf("enter array elements: ");
    for(int i=0;i<n;i++){
        scanf("%d",arr[i]);
        printf("enter target sum: ");
        scanf("%d",&sum);
        int dp[n+1][sum+1];
        for(int i=0;i<=n;i++){
            dp[i][0]=1;
        }
        for(int j=0;j<=sum;j++){
            dp[0][j]=0;
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=sum;j++){
                if(arr[i-1]>j)
                    dp[i][j]=dp[i-1][j];
                else
                    dp[i][j]=dp[i-1][j]|| dp[i-1][j-arr[i-1]];
            }
        }
    }
    if(dp[n][sum]==1)
        printf("true\n");
    else
        printf("false\n");
    return 0;
}
