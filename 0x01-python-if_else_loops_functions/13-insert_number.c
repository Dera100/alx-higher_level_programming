#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted sin and code ddd
 *
 * @head: A pointer to the head of the code ddd
 *
 * @number: The number in the code ddd
 *
 * Return: 0 If the function fails or pointer to the new node is zero.
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
