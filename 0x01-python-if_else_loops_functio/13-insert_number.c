#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head of list
 * @number: number to be included in new node
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *previous = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	/* If the list is empty new nodeshould be inserted before the first node */
	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		/* Traverse the list to find the insertion position */
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}

		/* Insert the new node */
		new->next = current;
		previous->next = new;
	}

	return (new);
}
