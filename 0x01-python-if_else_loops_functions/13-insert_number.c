#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new = NULL;
	listint_t *prev = NULL;

	tmp = *head;
	prev = tmp;
	new = malloc(sizeof(listint_t));
	while(tmp != NULL)
	{
		if (number <= tmp->n)
		{
			prev->next = new;
			new->n = number;
			new->next = tmp;
			return (new);
		}
		tmp = tmp->next;
	}
	new->n = number;
	*head = new;
	new->next = NULL;
	return (new);
}
