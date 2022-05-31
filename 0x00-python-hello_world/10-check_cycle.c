#include "lists.h"

/**
 * check_cycle - checks for linked list cycle
 * @list: head of the node
 * Return: 1 if its a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	int i, j, size = 10, nw_size;
	listint_t **node_add;

	node_add = malloc(sizeof(listint_t *) * size);
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
		if (i >= size - 1)
		{
			nw_size = size * 2;
			node_add = _realloc(node_add, size, nw_size);
			size = nw_size;
		}
	}
	free(node_add);
	return (0);
}

/**
 * _realloc - replicate realloc on stdlib
 * @ptr: pointer to original memory
 * @old_size: size of previous memory
 * @new_size: size of new memory
 * Return: returns pointer to new memory
 */

void *_realloc(listint_t **ptr, int old_size, int new_size)
{
	int i;
	listint_t **str, **old_ptr;

	old_ptr = ptr;
	str = malloc(new_size);
	if (!str)
	{
		free(ptr);
		return (NULL);
	}
	for (i = 0; i < (old_size || new_size--); i++)
	{
		str[i] = old_ptr[i];
	}
	free(ptr);
	return (str);
}
