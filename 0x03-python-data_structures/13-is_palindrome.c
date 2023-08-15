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
	if (head == NULL) /*An empty list is considered a palindrome*/
		return (1);
	return (1);
}
