#include <stdlib.h>
#include <stddef.h>
#include "hash_tables.h"

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *p;

	if (size)
	{
		p = (hash_table_t *)malloc(sizeof(hash_table_t));
		if (p == NULL)
			return NULL;
		else
		{
			p->size = size;
			p->array = calloc(size, sizeof(hash_node_t *));
			return (p);
		}
	}
	else
		return NULL;
}
