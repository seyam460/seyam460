#include<stdio.h>
int main(){
    int n;
    printf("enter a number: ");
    scanf("%d",&n);
    if(n == 0){
    printf("false\n");
    return 0;
}
 if(n&(n-1)== 0)
   printf("true\n");
   else
    printf("false\n");
return 0;
}
