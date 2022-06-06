#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int _mid_len(listint_t *head);
listint_t *_reverse_node(listint_t **head);

/**
 * is_palindrome - checks if a linked_list is a palindrome
 * @head: head of the linked list
 * Return: 1 if its a palindrome else 0
 * Description: This is the most efficient implementation of
 * finding if a linked list is a palidrome by manipulation of the list
 */

int is_palindrome(listint_t **head)
{
	listint_t *mid_node;
	int i = 0, mid_len;

	if (*head == NULL)
		return (1);
	mid_node = *head;
	mid_len = _mid_len(*head);
	for (i = 0; i < mid_len; i++)
		mid_node = mid_node->next;
	mid_node = _reverse_node(&mid_node);
	for (i = 0; i < mid_len; i++)
	{
		if (mid_node->n != (*head)->n)
			return (0);
		*head = (*head)->next;
		mid_node = mid_node->next;
	}
	return (1);
}

/**
 * _reverse_node - reverses the node from the middle
 * @head: head of the middle node
 * Return: a pointer to the new head
 */

listint_t *_reverse_node(listint_t **head)
{
	listint_t *prev, *next, *current;

	prev = NULL;
	next = current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * _mid_len - checks for the middle node
 * @head: head node
 * Return: returns the number of the middle node
 */

int _mid_len(listint_t *head)
{
	int len = 0;

	while (head)
	{
		len++;
		head = head->next;
	}
	return ((len / 2));
}
