#include "lists.h"

/**
	* free_singly - void func
	* Description: frees passed singly
	* @reversetmp: passed singly
	*/
void free_singly(listint_t **reversetmp)
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
