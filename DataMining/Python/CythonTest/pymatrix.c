#include <Python.h>
#include <numpy/arrayobject.h>
#include "matrix.h"

static char module_docstring[] = "This module provides an interface for calculating matrix using C.";
static char mul_docstring[] = "Calculate matrix multiplication.";

static PyObject *matrix_mul(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
	{"mul", matrix_mul, METH_VARARGS, mul_docstring},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initpymatrix(void)
{
	PyObject *m = Py_InitModule3("pymatrix", module_methods, module_docstring);
	if (m == NULL)
		return;

	/* Load `numpy` functionality. */
	import_array();
}

static PyObject *matrix_mul(PyObject *self, PyObject *args)
{
	PyObject *x_obj, *y_obj;

	/* Parse the input tuple */
	if (!PyArg_ParseTuple(args, "OO", &x_obj, &y_obj))
		return NULL;

	/* Interpret the input objects as numpy arrays. */
	PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
	PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);

	/* If that didn't work, throw an exception. */
	if (x_array == NULL || y_array == NULL) {
		Py_XDECREF(x_array);
		Py_XDECREF(y_array);
		return NULL;
	}

	////////////////////////////////////////////////////////////////////////////////////

	/* How many data points are there? */
	int xrow = (int)PyArray_DIM(x_array, 0);
	int xcol = (int)PyArray_DIM(x_array, 1);
	int yrow = (int)PyArray_DIM(y_array, 0);
	int ycol = (int)PyArray_DIM(y_array, 1);

	/* Get pointers to the data as C-types. */
	double *x    = (double*)PyArray_DATA(x_array);
	double *y    = (double*)PyArray_DATA(y_array);

	if (xcol != yrow) {
		PyErr_SetString(PyExc_RuntimeError, "ERROR : matrix multiplication -> different size of arrays");
		return NULL;
	}

	/* Call the external C function to compute the matrix multiplication. */
	double** res = mul(x, y, xrow, xcol, yrow, ycol);

	/* Clean up. */
	Py_DECREF(x_array);
	Py_DECREF(y_array);

	/* if (res < 0.0) {
		PyErr_SetString(PyExc_RuntimeError, "ERROR : matrix multiplication");
		return NULL;
	} */

	/* Build the output tuple */
	PyObject* ret = Py_BuildValue("O", res);
	PyObject* ret1= PyArray_FROM_OTF(ret, NPY_DOUBLE, NPY_IN_ARRAY);
	return ret1;
}
