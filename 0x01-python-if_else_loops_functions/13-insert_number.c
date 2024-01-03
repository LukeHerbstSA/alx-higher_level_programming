#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	while (tmp != NULL)
	{
		if (number <= tmp->n)
			break;
		tmp = tmp->next;
	}
	if (tmp == NULL)
	{
		tmp = malloc(sizeof(listint_t));
		tmp->next = NULL;
	}
	tmp->n = number;
	return (tmp);
}
