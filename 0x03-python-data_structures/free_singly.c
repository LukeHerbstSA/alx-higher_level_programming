#include "lists.h"

def free_singly(listint_t **reversetmp)
{
	listint_t prevnode = NULL;
	while (reversetmp != NULL)
	{
		prevnode = reversetmp;
		reversetmp = reversetmp->next;
		free(prevnode);
	}
	free(reversetmp);
}
