#include<stdio.h>
int main(){
     int T;
     scanf("%d",&T);
     while(T--){
        int n,x;
        scanf("%d %d",&n,&x);
        int subs=(n+5)/6;
        int cost=subs * x;
        printf("%d",&cost);
       }
       return 0;
}

