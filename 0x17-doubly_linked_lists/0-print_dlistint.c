#include "lists.h"

/**
	* print_dlistint - size_t func
	* Description: prints all elements of singly
	* @h: pointer to doubly linked list
	* Return: returns number of elements
	*/
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *tmp = *h;
	size_t i = 0;

	while (tmp != NULL)
	{
		printf("%zu\n", tmp->n);
		tmp = tmp->next;
		i++;
	}
	return (i)
}
