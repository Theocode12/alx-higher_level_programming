#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked_list is a palindrome
 * @head: head of the linked list
 * Return: 1 if its a palindrome else 0
 * Description: This is an implementation of find if a linked list
 * is a palidrome using arrays
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j, hlf_i, *rev_data;
	int data[2000];
	listint_t *nw_head;

	if (*head == NULL)
		return (1);
	nw_head = *head;
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
		if (data[j] != rev_data[i])
			return (0);
	}
	return (1);
}
