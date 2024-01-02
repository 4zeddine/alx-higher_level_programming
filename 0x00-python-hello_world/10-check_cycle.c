#include "lists.h"

/**
 * check_cycle - check for cycle in List
 * @head: head of linked list
 *
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *head)
{
	listint_t *n1, *n2;

	if(!head)
		return (0);
	n2 = head;
	n1 = head->next;
	while (n1 && n2 && n1->next)
	{
		if (n2 == n1)
			return (1);
		n2 = n2->next;
		n1 = n1->next->next;
	}
	return (0);
}
