#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
	* struct listint_s - int storage
	* Description: used to store elements in reverse from diff singly
	* @n: numer
	* @next: pointer to next struct
	*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);
void free_singly(listint_t *reversetmp);

#endif
