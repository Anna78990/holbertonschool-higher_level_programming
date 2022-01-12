#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert int node at the correct position
 * @head: linked list
 * @numner: number of the node
 * Return: the address of the new node, or NULL if it failed
 */


listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *tmp;
listint_t *current;

current = *head;
tmp = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
	return (NULL);
new->n = number;
if (head)
{
	if (number < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	tmp = tmp->next;
	while (number > tmp->n)
	{
		if(tmp == NULL)
			break;
		current = current->next;
		tmp = tmp->next;
	}
	current->next = new;
	new->next = tmp;
	return (new);
}
else
{
	new->next = NULL;
	*head = new;
	return (new);
}
}
