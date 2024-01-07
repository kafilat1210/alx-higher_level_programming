#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *stack[2048];
	int top = 0;

	if (!head || !*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		stack[top++] = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (slow->n != stack[--top]->n)
			return (0);
		slow = slow->next;
	}

	return (1);
}
