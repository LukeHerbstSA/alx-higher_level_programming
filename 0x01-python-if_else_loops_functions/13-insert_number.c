#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *prev = NULL;
	listint_t *nxtnode = NULL;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	while (tmp != NULL)
	{
		prev = tmp;
		nxtnode = tmp->next;
		if (nxtnode != NULL)
		{
			if (number <= nxtnode->n)
			{
				prev->next = malloc(sizeof(listint_t));
				prev = prev->next;
				prev->n = number;
				prev->next = tmp->next;
				tmp = prev;
				break;
			}
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
