#include <stdio.h>
#include <unistd.h>

int  main()
{
	for (int i=0;i <10; i++){
		printf("you are running a c code insdie a container...!!!!\n");
		sleep(1);
	}
	return 0;
}
