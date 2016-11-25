#include <Python.h>
#include <numpy/arrayobject.h>
#include "chi2.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "dataobj.h"

static char module_docstring[] = "This module provides an interface for calculating chi-squared using C.";
static char chi2_docstring[] = "Calculate the chi-squared of some data given a model.";

static PyObject* chi2_chi2(PyObject* self, PyObject* args);
static PyObject* sample_frange(PyObject* self, PyObject* args);

static PyMethodDef module_methods[] = {
	{"chi2", chi2_chi2, METH_VARARGS, chi2_docstring},
	{"frange", sample_frange, METH_VARARGS, chi2_docstring},
	{"readfile", read_file, METH_VARARGS, chi2_docstring},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC init_chi2(void)
{
	PyObject *m = Py_InitModule3("_chi2", module_methods, module_docstring);
	if (m == NULL)
		return;

	/* Load `numpy` functionality. */
	import_array();
}

static PyObject* read_file(PyObject* self, PyObject* args)
{
	PyObject* flist;
	char* infile;

	FILE* file;
	char* line = NULL;
	char* pch;
	char  read;
	size_t len, numline = 0;

	if(!PyArg_ParseTuple(args, "s", &infile))
		return NULL;

	file = fopen(infile, "r");
	while (-1 != (read = getline(&line, &len, file))) {
		numline ++;
	}

	rewind(file);
	struct DataObject* data = (struct DataObject*)malloc(sizeof(struct DataObject)*numline);
	int i = 0;
	while (-1 != (read = getline(&line, &len, file))) {
		int cnt = 0;
		char* path;
		char* onefile;
		struct tm time;
		pch = strtok(line, " ");
		while(NULL != pch) {
			if(0 == cnt)
				strcpy(data[i].ip, pch);
			else if(3 == cnt) {
				strptime(pch+1, "%d/%b/%Y:%H:%M:%S", &time);
				data[i].time = time;
			}
			else if(6 == cnt) {
				onefile = pch;
				path = strtok(pch, "?");
				path = strtok(path, "/");

				while(NULL != path) {
					onefile = path;
					path = strtok(NULL, "/");
				}
				strcpy(data[i].url, onefile);
			}

			pch = strtok(NULL, " ");
			cnt ++;
		}
		//printf("%s %d %d %d %d %ld %s\n", data[i].ip, time.tm_year+1900, time.tm_mon+1, time.tm_mday, time.tm_hour, mktime(&time), data[i].url);
		//printf("%s %d %d %d %d %s\n", data[i].ip, data[i].time.tm_year+1900, data[i].time.tm_mon+1, data[i].time.tm_mday, data[i].time.tm_hour, data[i].url);

		i++;
	}

	flist = PyList_New(numline);
	for(i = 0; i < numline; i++) {
		//printf("%s %d %d %d %d %s\n", data[i].ip, data[i].time.tm_year+1900, data[i].time.tm_mon+1, data[i].time.tm_mday, data[i].time.tm_hour, data[i].url);
		PyList_SetItem(flist, i, Py_BuildValue("[siiiils]", data[i].ip, data[i].time.tm_year+1900, data[i].time.tm_mon+1, data[i].time.tm_mday, data[i].time.tm_hour, mktime(&data[i].time), data[i].url));
	}

	free(data);

	return flist;
}

static PyObject* sample_frange(PyObject* self, PyObject* args)
{
	PyObject* flist;
	double v, from, to, step;
	int size, k;

	if(!PyArg_ParseTuple(args, "ddd", &from, &to, &step))
		return NULL;

	size = (to-from) / step;
	flist = PyList_New(size);
	v = from;

	for(k = 0; k < size; k++) {
		PyList_SetItem(flist, k, PyFloat_FromDouble(v));
		v += step;
	}

	return flist;
}

static PyObject *chi2_chi2(PyObject *self, PyObject *args)
{
	double m, b;
	PyObject *x_obj, *y_obj, *yerr_obj;

	/* Parse the input tuple */
	if (!PyArg_ParseTuple(args, "ddOOO", &m, &b, &x_obj, &y_obj, &yerr_obj))
		return NULL;

	/* Interpret the input objects as numpy arrays. */
	PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
	PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);
	PyObject *yerr_array = PyArray_FROM_OTF(yerr_obj, NPY_DOUBLE, NPY_IN_ARRAY);

	/* If that didn't work, throw an exception. */
	if (x_array == NULL || y_array == NULL || yerr_array == NULL) {
		Py_XDECREF(x_array);
		Py_XDECREF(y_array);
		Py_XDECREF(yerr_array);
		return NULL;
	}

	/* How many data points are there? */
	int N = (int)PyArray_DIM(x_array, 0);

	/* Get pointers to the data as C-types. */
	double *x    = (double*)PyArray_DATA(x_array);
	double *y    = (double*)PyArray_DATA(y_array);
	double *yerr = (double*)PyArray_DATA(yerr_array);

	/* Call the external C function to compute the chi-squared. */
	double value = chi2(m, b, x, y, yerr, N);

	/* Clean up. */
	Py_DECREF(x_array);
	Py_DECREF(y_array);
	Py_DECREF(yerr_array);

	if (value < 0.0) {
		PyErr_SetString(PyExc_RuntimeError,
				"Chi-squared returned an impossible value.");
		return NULL;
	}

	/* Build the output tuple */
	PyObject *ret = Py_BuildValue("d", value);
	return ret;
}
