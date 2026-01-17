#include <stdio.h>
int main() {
    int n;
    printf("enter the size of an array: ");
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    for (int i = n - 1; i >= 0; i--) {
        printf("the reversed array: %d ", arr[i]);
    }
    return 0;
}
