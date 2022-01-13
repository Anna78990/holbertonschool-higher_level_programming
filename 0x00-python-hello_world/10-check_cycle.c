#include "lists.h"

/**
 * check_cycle - checks if the node has cycle or not
 * @list: pointer to head of list
 * Return: if it has a cycle return 1, otherwise 0.
 */

int check_cycle(listint_t *list)
{
listint_t *comp;

comp = list;
while (list->next)
{
	while (comp->next)
	{
		if (comp == list)
			comp = comp->next;
		if (list == comp->next)
			return (1);
		comp = comp->next;
	}
	list = list->next;
}
return (0);
}
