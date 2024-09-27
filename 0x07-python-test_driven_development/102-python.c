#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - Displays detailed information about Python string objects
 *
 * @p: A pointer to the Python object being inspected
 * Return: No return value
 */
void print_python_string(PyObject *p)
{
    PyObject *str, *repr;

    /* Output information about the string object */
    printf("[.] string object info\n");

    /* If the object isn't a string, display an error message */
    if (!p || strcmp((*(p->ob_type)).tp_name, "str"))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Determine if the string is in compact ASCII or compact Unicode format */
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    /* Get the string representation of the object */
    repr = PyObject_Repr(p);

    /* Convert the string to UTF-8 encoding */
    str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

    /* Print the string length and the actual string value */
    printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
    printf("  value: %s\n", PyBytes_AsString(str));
}
