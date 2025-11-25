#include<stdio.h>
int findcelebrity(int mat[][100],int n){
    int i=0,j=n-1;
    while(i<j){
        if(mat[i][j]==1)
            i++;
        else
            j--;
    }
    int cand=i;
    for(int k=0;k<n;k++){
        if(k != cand){
            if(mat[cand][k]== 1 || mat[k][cand]==0)
                return -1;
        }
    }
    return cand;
}
int main(){
    int mat[100][100]={
        {1,1,0},
        {0,1,0},
        {0,1,1},
    };
  int n=3;
  int celeb=findcelebrity(mat,n);
  if(celeb == -1)
        printf("no celebrity\n");
  else
    printf("celebrity is:%d\n",celeb);
  return 0;
}




