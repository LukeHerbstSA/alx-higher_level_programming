#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nxtnode = NULL;
	listint_t *tmp = NULL;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	while (tmp != NULL)
	{
		if (number >= tmp->n)
		{
			nxtnode = tmp->next;
			tmp->next = malloc(sizeof(listint_t));
			tmp = tmp->next;
			tmp->n = number;
			tmp->next = nxtnode;
			break;
		}
		tmp = tmp->next;
	}
	if (tmp == NULL)
	{
		tmp = malloc(sizeof(listint_t));
		tmp->n = number;
		tmp->next = NULL;
	}
	return (tmp);
}
