#include <Python.h>

void print_python_float(PyObject *p);
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 *print_python_list - Print some basic info about Python lists
 *@p: A ptr pointing to PyObject p parameter
 *Description: If p is not a valid PyListObject, print an error msg
 *
 * Return: Nothing(Void Function)
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t x = 0, my_size;
        const char *data_type;
        Py_ssize_t mem_alloc;
        PyVarObject *object_var = (PyVarObject *)p;
        PyListObject *object_list = (PyListObject *)p;

        my_size = object_var->ob_size;
        mem_alloc = object_list->allocated;

        fflush(stdout);

        printf("[*] Python list info\n");
        if (strcmp(p->ob_type->tp_name, "list") != 0) /*lexigraphic cmp*/
        {
                printf("  [ERROR] Invalid List Object\n"); /*disp err msg*/
                return;
        }

        printf("[*] Size of the Python List = %ld\n", object_size);
        printf("[*] Allocated = %ld\n", mem_alloc);

        while (x < object_size)
        {
                object_type = object_list->ob_item[x]->ob_type->tp_name;
                printf("Element %ld: %s\n", x, object_type);
                if (strcmp(object_type, "float") == 0) /*lexigraphic cmp*/
                        print_python_float(object_list->ob_item[x]);
                else if (strcmp(object_type, "bytes") == 0)
                        print_python_bytes(object_list->ob_item[x]);
                x++;
        }
}

/**
 *print_python_bytes - Print some basic info about Python byte objects
 *@p: A ptr pointing to PyObject p parameter
 *Description: Line “first X bytes”: print a maximum of 10 bytes
 *If p is not a valid PyBytesObject, print an error msg
 *
 * Return - Nothing(Void Function)
 */
void print_python_bytes(PyObject *p)
{
        Py_ssize_t x = 0;
        PyBytesObject *object_bytes = (PyBytesObject *)p;
        Py_ssize_t object_size;

        fflush(stdout);

        printf("[.] bytes object info\n");
        if (strcmp(p->ob_type->tp_name, "bytes") != 0) /*lexigraphic cmp*/
        {
                printf("  [ERROR] Invalid Bytes Object\n"); /*disp err msg*/
                return;
        }

        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", object_bytes->ob_sval);

        ((PyVarObject *)p)->ob_size < 10 ?
                object_size == ((PyVarObject *)p)->ob_size + 1 :
                object_size == 10;

        printf("  first %ld bytes: ", object_size);
        while (x < object_size)
        {
                printf("%02hhx", object_bytes->ob_sval[x]);
                x != (object_size - 1) ? printf(" ") : printf("\n");
                x++;
        }
}

/**
 *print_python_float - Print some basic info about Python float objects
 *@p: A ptr pointing to PyObject p parameter
 *Description: If p is not a valid PyFloatObject, print an error msg
 *Return: Nothing (void function)
 */
void print_python_float(PyObject *p)
{
        char *my_buf = NULL;

        PyFloatObject *object_float = (PyFloatObject *)p;

        fflush(stdout);

        printf("[.] float object info\n");
        if (strcmp(p->ob_type->tp_name, "float") != 0) /*lexigraphic cmp*/
        {
                printf("  [ERROR] Invalid Float Object\n"); /*disp err msg*/
                return;
        }
        my_buf = PyOS_double_to_string(object_float->ob_fval, 'r', 0,
                        Py_DTSF_ADD_DOT_0, NULL);
        printf("  value: %s\n", my_buf);
        PyMem_Free(my_buf); /*Deallocate memory*/
}
