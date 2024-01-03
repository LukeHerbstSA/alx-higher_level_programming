#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *prev = NULL;
	listint_t *nextptr = NULL;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	while (tmp != NULL)
	{
		prev = tmp;
		if (tmp->next != NULL)
		{
			if (number <= (tmp->next)->n)
			{
				nextptr = malloc(sizeof(listint_t));
				nextptr->n = number;
				prev->next = nextptr;
				nextptr->next = tmp->next;
				break;
			}
		}
		tmp = tmp->next;
	}
	if (tmp == NULL)
	{
		tmp = malloc(sizeof(listint_t));
		tmp->next = NULL;
		tmp->n = number;
	}
	return (nextptr);
}
