#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *tmp;
listint_t *current;

current = *head;
tmp = *head;
tmp = tmp->next;
new = malloc(sizeof(listint_t));
if (new == NULL)
	return (NULL);
new->n = number;
while (number > tmp->n)
{
	current = current->next;
	tmp = tmp->next;
}
current->next = new;
new->next = tmp;
return (new);
}
