#include "lists.h"

/**
 * check_cycle -  linked list contains a cycle or not
 *
 * @list: linked list to the program
 *
 * Return: 1(ONE) if the list has a cycle, 0(ZERO) if it doesn't in the program
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
