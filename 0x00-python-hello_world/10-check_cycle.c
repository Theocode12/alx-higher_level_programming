#include "lists.h"

/**
 * check_cycle - checks for linked list cycle
 * @list: head of the node
 * Return: 1 if its a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	int i, j;
	listint_t **node_add;

	node_add = malloc(sizeof(listint_t *) * 50);
	for (i = 0; list; i++)
	{
		node_add[i] = list;
		for (j = 0; j < i; j++)
		{
			if (node_add[j] == list)
			{
				free(node_add);
				return (1);
			}
		}
		list = list->next;
	}
	free(node_add);
	return (0);
}
