#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop.
 *
 * Return: Always returns 0.
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
 * main - Creates 5 zombie processes.
 *
 * Return: Always returns 0.
 */
int main(void)
{
pid_t zombie_pid;
int i;

for (i = 0; i < 5; i++)
{
	zombie_pid = fork();

	if (zombie_pid > 0)
	{
		printf("Zombie process created, PID: %d\n", zombie_pid);
		sleep(1);
	}
	else
	{
		exit(0);
	}
}

infinite_while();

return (0);
}
