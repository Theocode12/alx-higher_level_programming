#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked_list is a palindrome
 * @head: head of the linked list
 * Return: 1 if its a palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, hlf_i;
	listint_t *nw_head;
	int *data, *rev_data;

	if (*head == NULL)
		return (1);
	nw_head = *head;
	while (nw_head)
	{
		i++;
		nw_head = nw_head->next;
	}
	data = malloc(sizeof(int) * (i));
	if (data == NULL)
		exit(0);
	nw_head = *head;
	while (nw_head)
	{
		data[j] = nw_head->n;
		nw_head = nw_head->next;
		j++;
	}
	hlf_i = (i / 2) + 1;
	rev_data = data + (--i);
	for (j = 0, i = 0; j <= hlf_i; j++, i--)
	{
		if (data[j] != rev_data[i])
		{
			free(data);
			return (0);
		}
	}
	free(data);
	return (1);
}
