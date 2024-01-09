#include "lists.h"

/**
	* is_palindrome - int func
	* Description: checks if a singly is a palindrome
	* @head: singly list pointer to ints
	* Return: 1 if palindrome 0 if not
	*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *revtmpstart = NULL;
	listint_t *reversetmp = NULL;
	listint_t *prevnode = NULL;
	int range = 0;

	if (*head == NULL)
		return (0);
	while (tmp != NULL)
	{
		reversetmp = malloc(sizeof(listint_t));
		reversetmp->next = NULL;
		reversetmp->n = tmp->n;
		if (tmp != *head)
			reversetmp->next = prevnode;
		prevnode = reversetmp;
		tmp = tmp->next;
		range++;
		if (tmp == NULL)
                {
			revtmpstart = reversetmp;
			reversetmp->next = prevnode;
			break;
                }
	}
	tmp = *head;
	range = (range % 2 == 0) ? range / 2 : ((range + 1) / 2);
	prevnode = revtmpstart;

	while (range != 0)
	{
		if (revtmpstart->n != tmp->n)
			break;
		revtmpstart = revtmpstart->next;
		tmp = tmp->next;
		--range;
	}
	free_singly(prevnode);
	return (range == 0 ? 1 : 0);
}
