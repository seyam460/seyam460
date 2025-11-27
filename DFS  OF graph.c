#include<stdio.h>
void dfsresult(int adj[][10],int adjsize[],int v){
    int visited[v];
    for(int i=0;i<v;i++){
        visited[i]=0;
    }
    int stack[100],top=-1;
    int result[100],idx=0;
    stack[++top]=0;
    while(top!=-1){
        int node=stack[top--];
        if(!visited[node]){
            visited[node]=1;
            result[idx++]=node;
        }
        for(int i=adjsize[node]-1;i>=0;i--){
            int next=adj[node][i];
            if(!visited[next]){
                    stack[++top]=next;
               }
        }
    }
    printf("DFS traversal:");
    for(int i=0;i<idx;i++){
        printf("%d",result[i]);
    }
}
int main(){
    int adj[5][10]={
        {2,3,1},
        {0},
        {0,4},
        {0},
        {2}};
        int adjsize[]={3,1,2,1,1};
        dfsresult(adj,adjsize,5);
        return 0;
}
