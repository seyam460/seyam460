#include <stdio.h>

void findDuplicates(int arr[], int n) {
    int freq[n + 1];
    for (int i = 0; i <= n; i++) {
        freq[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }
    int found = 0;
    printf("Duplicates: ");
    for (int i = 1; i <= n; i++) {
        if (freq[i] == 2) {
            printf("%d ", i);
            found = 1; }
    }
    if (!found) {
        printf("[]");}
}
 int main() {
    int arr[] = {2, 3, 1, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    findDuplicates(arr, n);
    return 0;
}

