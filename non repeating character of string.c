#include<stdio.h>
#include<string.h>

int main(){
    char s[200];
    int freq[26]={0};
    printf("enter string: ");
    scanf("%s",s);
    int len=strlen(s);
    for(int i=0;i<len;i++){
        freq[s[i]-'a']++;
    }
    for(int i=0;i<len;i++){
        if(freq[s[i]- 'a'] == 1){
            printf("first non-repeating character=%c\n",s[i]);
            return 0;
        }
    }
    printf("first non-repeating character=$\n");
    return 0;
}
