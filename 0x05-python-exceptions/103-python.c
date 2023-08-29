#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <listobject.h>
#include <floatobject.h>
#include <bytesobject.h>
#include <object.h>

/**
 *print_python_list - Print some basic info about Python lists
 *@p: A ptr pointing to PyObject p parameter
 *Description: If p is not a valid PyListObject, print an error msg
 *Return: Nothing (void function)
 */
void print_python_list(PyObject *p)
{
	PyListObject *py_list;
	size_t bytes_alloc, byte_size, x = 0;
	const char *type_of_data;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	byte_size = PyList_GET_SIZE(p);
	py_list = (PyListObject *)p;
	bytes_alloc = py_list->bytes_alloc;

	printf("[*] Size of the Python List = %ld\n", byte_size);
	printf("[*] Allocated = %li\n", bytes_alloc);
	while (x < byte_size)
	{
		type_of_data = (py_list->ob_item[x])->ob_type->tp_name;
		printf("Element %li: %s\n", x, type_of_data);
		if (strcmp(type_of_data, "float") == 0)
			print_python_float(py_list->ob_item[x]);
		else if (strcmp(type_of_data, "bytes") == 0)
			print_python_bytes(py_list->ob_item[x]);
		x++;
	}
	fflush(stdout);
}
/**
 *print_python_bytes - Print some basic info about Python byte objects
 *@p: A ptr pointing to PyObject p parameter
 *Description: Line “first X bytes”: print a maximum of 10 bytes
 *If p is not a valid PyBytesObject, print an error msg
  *Return: Nothing (void function)
 */
void print_python_bytes(PyObject *p)
{
	char *s = NULL;
	size_t byte_size, x;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	byte_size = PyBytes_Size(p);
	s = ((PyBytesObject *)(p))->ob_sval;
	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", s);
	(byte_size < 10) ? byte_size++ : byte_size = 10;
	printf("  first %ld bytes: ", byte_size);
	while (x < bytes - 1)
	{
		printf("%02hhx ", s[x]);
		x++;
	}
	printf("%02hhx", s[x]);
	printf("\n");
	fflush(stdout);
}
/**
 *print_python_float - Print some basic info about Python float objects
 *@p: A ptr pointing to PyObject p parameter
 *Description: If p is not a valid PyFloatObject, print an error msg
 *Return: Nothing (void function)
 */
void print_python_float(PyObject *p)
{
	char *s = NULL;
	double float_num;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	float_num = ((PyFloatObject *)(p))->ob_fval;
	s = PyOS_double_to_string(float_num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
	fflush(stdout);
}
