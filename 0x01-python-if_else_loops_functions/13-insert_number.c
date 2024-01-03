#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *prev = NULL;

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
