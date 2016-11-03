#include "matrix.h"
#include <stdio.h>
#include <stdlib.h>

/*
void printmat(double* mat, int row, int col)
{
	for(int i = 0; i < row; i++) {
		for(int j = 0; j < col; j++)
			printf("%f ", mat[i][j]);
		printf("\n");
	}
}
*/

double** mul(double* x, double* y, int xrow, int xcol, int yrow, int ycol) {
	//double** res = (double**)malloc(xrow*sizeof(double*));
	//for(int i = 0; i < xrow; i++)
	//	res[i] = (double*)malloc(ycol*sizeof(double*));
	double res[3][5] = {0};

	int resi;
	int resj;
	for(int i = 0; i < xrow; i++) {
		for(int j = 0; j < ycol; j++) {
			double sum = 0.0;
			resi = i*xcol;
			resj = j;
			for(int k = 0; k < xcol; k++) {
				sum += (x[resi+k]*y[resj]);
				resj += ycol;
			}
			res[i][j] = sum;
		}
	}

	return res[0];
}
