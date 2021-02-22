/*sum of n numbers*/
#include<stdio.h>

int main()
{
	int a, i;
	int sum =0;
	printf("Enter total number:\n");
	scanf("%d", &a);

	for (i =1 ; i<= a; i++)
	{
		sum = i+sum;
	}
	printf("Sum: %d\n", sum);

	return 0;
}
