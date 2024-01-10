#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the start of the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (tortoise != hare)
	{
		tortoise = tortoise->next;

		if (hare->next == NULL || hare->next->next == NULL)
			return (0);

		hare = hare->next->next;
	}

	return (1);
}
