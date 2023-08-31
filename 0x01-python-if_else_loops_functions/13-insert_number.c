#include "lists.h"
/**
 *insert_node - A function that inserts a number into a sorted singly linked list
 *@head: A ptr pointing the head of the sorted singly linked list
 *@number: The number parameter to be inserted
 *Return: A ptr pointing to a temporarary "new" node
 *else NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = *head, *tmp;

	tmp = malloc(sizeof(listint_t)); /*dynamic memory allocation*/
	if (tmp == NULL) /*test for malloc failure*/
		return (NULL);
	tmp->n = number; /*define data int number*/
	if (new == NULL || new->n >= number)
	{
		tmp->next = new;
		*head = tmp;
		return (tmp);
	}
	while (new && new->next && new->next->n < number) /*iterate*/
		new = new->next; /*new to next ptr of node*/
	tmp->next = new->next; /*tmp to next ptr of new*/
	new->next = tmp; /*next ptr of new eq tmp node*/

	return (tmp);
}
