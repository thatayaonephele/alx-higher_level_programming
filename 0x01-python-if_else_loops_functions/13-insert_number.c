#include "lists.h"
/**
 *insert_node - Inserts a number into a sorted singly linked list
 *@h: A ptr pointing the head of the sorted singly linked list
 *@number: The number parameter to be inserted
 *Return: A ptr pointing to a temporarary "new" node
 *else NULL on failure
 */
listint_t *insert_node(listint_t **h, int number)
{
	listint_t *tmp = *h, *new;

	new = malloc(sizeof(listint_t)); /*dynamic memory allocation*/
	if (new == NULL) /*test for malloc failure*/
		return (NULL);
	new->n = number; /*define data int number*/
	if (tmp->n >= number || tmp == NULL)
	{
		new->next = tmp;
		*h = new;
		return (new);
	}
	while (tmp && tmp->next && tmp->next->n < number) /*iterate*/
		tmp = tmp->next; /*new to next ptr of node*/
	new->next = tmp->next; /*tmp to next ptr of new*/
	tmp->next = new; /*next ptr of new eq tmp node*/

	return (new);
}
