#include <Python.h>
#include "chi2.h"

double chi2(double m, double b, double *x, double *y, double *yerr, int N) {
	int n;
	double result = 0.0, diff;

	for (n = 0; n < N; n++) {
		diff = (y[n] - (m * x[n] + b)) / yerr[n];
		result += diff * diff;
	}

	return result;
}

/*/
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
/*/

