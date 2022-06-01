#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - sorted insertion of a node in a singly linked list
 * @head: the head of the list
 * @number: data for the new node
 * Return: return the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pr = *head, *nx = *head, *nw_node;

	nw_node = malloc(sizeof(listint_t));
	if (!nw_node)
		return (NULL);
	nw_node->n = number;
	nw_node->next = NULL;
	if (*head == NULL)
	{
		*head = nw_node;
		return (nw_node);
	}
	if (pr->n >= nw_node->n)
	{
		nw_node->next = *head;
		*head = nw_node;
		return (nw_node);
	}
	while ((nx = nx->next) != NULL)
	{
		if (nx->n >= nw_node->n)
		{
			nw_node->next = pr->next;
			pr->next = nw_node;
			return (nw_node);
		}
		pr = pr->next;
	}
	pr->next = nw_node;
	return (nw_node);
}
