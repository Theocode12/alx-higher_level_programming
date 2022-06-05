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
	int i = 0, j, hlf_i, *rev_data;
	int data[8000];
	listint_t *nw_head;

	if (*head == NULL)
		return (1);
	nw_head = *head;
	/*while (nw_head)
	{
		i++;
		nw_head = nw_head->next;
	}
	data = malloc(sizeof(int) * (i));
	nw_head = *head;*/
	for (j = 0; nw_head; j++)
	{
		data[j] = nw_head->n;
		nw_head = nw_head->next;
	}
	i = j;
	hlf_i = (i / 2);
	rev_data = data + (--i);
	for (j = 0, i = 0; j <= hlf_i; j++, i--)
	{
		/*printf("data: %d,   rev_data: %d\n", data[j], rev_data[i]);*/
		if (data[j] != rev_data[i])
		{
			
			/*free(data);*/
			return (0);
		}
	}
	/*free(data);*/
	return (1);
}
