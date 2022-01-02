#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *tmp;
listint_t *current;

current = *head;
tmp = current->next;
new = malloc(sizeof(listint_t));
new->n = number;
if (new == NULL)
	return (NULL);
while (number > current->n)
{
	if(tmp->n > number)
		continue;
	current = current->next;
	tmp = tmp->next;
}
current->next = new;
new->next = tmp->next;
return (new);
}
