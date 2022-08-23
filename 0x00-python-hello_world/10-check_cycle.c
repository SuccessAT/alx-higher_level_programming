nclude "lists.h"

/**
 * check_cycle - checks if a singly linked list for cycles
 * @list: list pointer
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer;
	listint_t *previous;

	pointer = list;
	previous = list;
	while (list && pointer && pointer->next)
	{
		list = list->next;
		pointer = pointer->next->next;

		if (list == pointer)
		{
			list = previous;
			previous =  pointer;
			while (1)
			{
				pointer = previous;
				while (pointer->next != list && pointer->next != previous)
				{
					pointer = pointer->next;
				}
				if (pointer->next == list)
					break;

				list = list->next;
			}
			return (1);
			
		}
	}

	return (0);
}
