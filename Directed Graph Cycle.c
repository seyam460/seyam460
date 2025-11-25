#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    int v;
    struct node*next;
}node;
void addedge(node*adj[];int u;int v){
    node*newnode= (node*)malloc(sizeof(node));
    newNode->v = v;
    newnode->next=adj[u];
    adj[u]=newnode;
}
int dfs(int curr,int visited[],int recStack[],Node* adj[]){
    if (!visited[curr]){
        visited[curr] = 1;
        recStack[curr] = 1;
        Node* temp = adj[curr];
       while (temp != NULL){
            int next = temp->v;
            if (!visited[next] && dfs(next, visited, recStack, adj))
                return 1;
            else if (recStack[next])
                return 1;
            temp =temp->next;}
    }
    recStack[curr]=0;
}

int containsCycle(int V,Node* adj[]) {
    int visited[V];
    int recStack[V];
    for (int i = 0; i < V; i++){
        visited[i] = 0;
        recStack[i] = 0;}
    for (int i = 0; i < V; i++){
        if (dfs(i, visited, recStack, adj))
            return 1;}
      return 0;
}
int main(){
    int V= 4;
    int edges[][2]={{0,1}, {1,2}, {2,0}, {2,3}};
    int E = 4;
    Node* adj[V];
    for (int i = 0; i < V; i++) adj[i] = NULL;

    for (int i = 0; i < E; i++)
        addEdge(adj, edges[i][0], edges[i][1]);
    if (containsCycle(V, adj))
        printf("Cycle Detected\n");
    else
        printf("No Cycle\n");
    return 0;
}
