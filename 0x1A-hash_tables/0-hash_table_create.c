#include "hash_tables.h"
#include <stdlib.h>

/**
 * hash_table_create - Creating a hash table
 * @size: size of table
 * Return: pointer to table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht;

	ht = malloc(sizeof(hash_table_t));
	ht->size = size;
	ht->array = calloc(size, sizeof(unsigned long int *));
	return (ht);
}
