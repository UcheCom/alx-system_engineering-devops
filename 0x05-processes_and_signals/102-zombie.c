#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - Function creates an infinite loop to keep
 * the program running
 *
 * Return: 0 always
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Function creats 5 zombie processes
 * Return: 0 always
*/
int main(void)
{
	int i = 0;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (!child_pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)child_pid);
	}
	if (child_pid != 0)
		infinite_while();
	return (0);
}
