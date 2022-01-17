#include "lists.h"

/**
 * check_cycle - checks if the node has cycle or not
 * @list: pointer to head of list
 * Return: if it has a cycle return 1, otherwise 0.
 */

int check_cycle(listint_t *list)
{
listint_t *comp, *scd;

if (list)
{
	comp = list;
	while (comp->next)
	{
		scd = comp;
		while (scd)
		{
			scd = scd->next;
			if (scd == comp)
				return (1);
		}
		comp = comp->next;
	}
}
return (0);
}
