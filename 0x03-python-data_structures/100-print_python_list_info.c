#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <stdlib.h>
/**
 *print_python_list_info - Prints some basic info about Python lists
 *@p: A ptr to an opaque data type repr arbitrary Python obj
 *Return: Nothing (Void Function)
*/
void print_python_list_info(PyObject *p)
{
	int x = 0; /*loop index pos variable*/
	long int obj_len = PyList_Size(p);/*acc ob_size mem of Python obj*/
	PyListObject *o = (PyListObject *)p;/*acc ob_type mem of Python obj*/

	printf("[*] Size of the Python List = %li\n", obj_len);
	printf("[*] Allocated = %li\n", o->allocated);
	while (x < obj_len)
	{
		printf("Element %i: %s\n", x, Py_TYPE(o->ob_item[x])->tp_name);
		x++;
	}
}
