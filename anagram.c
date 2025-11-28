#include<stdio.h>
#include<string.h>
int main(){
    char s1[100],s2[100];
    int freq[26]={0};
    printf("enter first string: ");
    scanf("%s",s1);
    printf("enter second string: ");
    scanf("%s",s2);
    if(strlen(s1)!= strlen(s2)){
        printf("false\n");
        return 0;
    }
    for(int i=0;s1[i]!='\0';i++){
        freq[s1[i]-'a']++;
        freq[s2[i]-'a']--;
    }
    for(int i=0;i<26;i++){
        if(freq[i]!=0){
            printf("false\n");
            return 0;
        }
    }
    printf("true\n");
    return 0;
}
