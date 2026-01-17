#include<stdio.h>
#include<limits.h>
int main(){
    int arr[6][6];
    for (int i=0;i<6;i++){
        for (int j=0;j<6;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int maxsum = INT_MIN;
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            int hourglasssum =
                                 a[i][j]+ a[i][j+1] + a[i][j+2]
                                        + a[i+1][j+1]
                                +a[i+2][j]+ a[i+2][j+1]+a[i+2][j+2];
                        if (hourglassum > maxsum){
                            maxsum = hourglasssum;
                        }
        }
    }
    printf("%d" ,maxsum);
    return 0;
}
