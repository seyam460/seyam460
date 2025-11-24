#include<stdio.h>
#include<string.h>
int main(){
    char str[200], rev[200];
    printf("enter a string: ");
    scanf("%s",str);
    int len=strlen(str);
    for(int i=0;i<len;i++){
        rev[i]=str[len-i-1];
    }
    rev[len]='\0';
    if(strcmp(str,rev) == 0){
        printf("the string is a palindrome:\n");
    }
    else {
        printf("the string is not a palindrome:\n");
    }
    return 0;
}
