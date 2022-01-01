#include "lists.h"

int check_cycle(listint_t *list)
{
	int i = 0;
while (list != NULL)
{
	list = list->next;
	i++;
}
if (i == 0)
{
	return (0);
}
else
{
	return (1);
}
}
