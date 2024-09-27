#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * disp_py_info - Displays information about a Python string object.
 *
 * @ptr: Python Object pointer
 * Return: No return
 */
void disp_py_info(PyObject *ptr)
{
	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	/* Check if the object type is a string */
	if (strcmp((*(ptr).ob_type).tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Identify and print the type of Python Unicode string */
	if (PyUnicode_IS_COMPACT_ASCII(ptr))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	/* Get the string representation and length */
	repr = PyObject_Repr(ptr);
	str = PyUnicode_AsEncodedString(ptr, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(ptr));
	printf("  value: %s\n", PyBytes_AsString(str));
}
