#include<stdio.h>
#include<string.h>
int main(){
    char s[1001];
    printf("enter a string: ");
    fgets(s,sizeof(s),stdin);
    int len=strlen(s);
    if(s[len-1] == '\n'){
        s[len-1] == '\0';
        len--;
    }
    int ispal=1;
    for(int i=0;i<len/2;i++){
        if(s[i]!=s[len-1-i]){
            ispal=0;
            break;
        }
    }
    if(ispal)
        printf("true\n");
    else
        printf("false\n");
    return 0;

}
