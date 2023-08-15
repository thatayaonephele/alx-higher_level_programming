#include "lists.h"
/**
 * reverse_listint - A function that reverses a listint_t list.
 * @head: A pointer pointing to the pointers' address
 * of the head of the list_t list.
 * Return: A pointer to the 1st node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *lagging_node, *foward_node;

	if (*head != NULL || head != NULL)
	{
	lagging_node = NULL;

	for (; (*head)->next != NULL; *head = foward_node)
	{
		foward_node = (*head)->next;
		(*head)->next = lagging_node;
		lagging_node = *head;
	}

	(*head)->next = lagging_node;
	return (*head);
	}
	else
		return (NULL);
}
/**
 *is_palindrome - A function that checks if linked list is palindrome or not
 *@head: The 1st initial node in a signle linked list
 *Return: 1 if linked list is a palindrome else 0.
*/
int is_palindrome(listint_t **head)
{
	listint_t *s1 = *head;
	listint_t *s2 = *head;
	listint_t *n1, *n2;

	if (head == NULL) /*An empty list is considered a palindrome*/
		return (1);

	while ((s1->next != NULL)  && (s1->next->next != NULL))
	{
		s1 = s1->next->next; /*1st node must move at twice the speed*/
		s2 = s2->next; /*2nd node must move at half the speed of s1*/
	}
	n1 = *head;
	n2 = reverse_listint(&(s2->next));
	while (n2 != NULL && n1 != NULL)
	{
		if (n1->n != n2->n)
		{
			return (0);
		}
	}
	n1 = n1->next;
	n2 = n2->next;

	return (1);
}
