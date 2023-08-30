#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list - A ptr pointing to a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *x = list; /*initialization of x ptr*/
	list_t *y = list; /*defining of y ptr*/	

	while (x && y) /*iterate if both y and x are defined*/
	{
		if (y->next == NULL) /*chech if we at the head node*/
			return (0); /*There's no cycle*/
		x = x->next; /*set x node to next ptr of x*/
		y = y->next->next; /*set y node to next of next ptr of y*/
		if (x == y) /*test if nodes are equal*/
			return (1); /*cycle exits if true*/
	}

	return (0); /*no cycle exits*/
}
