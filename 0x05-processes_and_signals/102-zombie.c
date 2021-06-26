#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>


int infinite_while(void)
{
	sleep(1);
	exit(0);
}

void create_zombies(int nth_child)
{
	pid_t child;

	if (nth_child == 5)
	{
		return;
	}
	child = fork();
	if (child == 0)
	{
		infinite_while();
	}
	else
	{
		sleep(10);
	}
	printf("Zombie process created, PID: %d\n", (int)child);
	create_zombies(nth_child + 1);
}

int main(void)
{
	create_zombies(0);
	return (0);
}





