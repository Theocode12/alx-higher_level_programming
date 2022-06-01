#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for linked list cycle
 * @list: head of the node
 * Return: 1 if its a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	int i, j;
	listint_t *node_adr[100];

	for (i = 0; list; i++)
	{
		node_adr[i] = list;
		for (j = 0; j < i; j++)
		{
			if (node_adr[j] == list)
				return (1);
		}
		list = list->next;
	}
	return (0);
}
