#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int count = 0,front;
int arr[1000];

void push(int x) {
	arr[count] = x;
	count++;
}

void pop() {
	count--;
	front = arr[0];
	for (int i = 0; i < count; i++) {
		arr[i] = arr[i + 1];
	}
}

int main(void) {
	int n,k;

	scanf("%d %d", &n,&k);
	for (int i = 0; i < n; i++) {
		arr[i] = i + 1;
		count++;
	}
	printf("<");
	while (count > 1) {
		for (int i = 1; i < k; i++) {
			pop();
			push(front);
		}
		pop();
		printf("%d, ", front);
	}
	printf("%d>", arr[0]);
}