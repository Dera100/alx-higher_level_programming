#iinclude <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert node to the code 
 *
 *
 * @head: head start of the code
 *
 *
 * @number: num use to make specicification
 *
 * Return: the address of new ncode
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *actual = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (actual->next)
	{
		if ((actual->next)->n >= number)
		{
			new->next = actual->next;
			actual->next = new;
			return (new);
		}
		actual = actual->next;
	}

	new->next = NULL;
	actual->next = new;

	return (new);
}
