import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;

import numjava.NumJava;
import numjava.Matrix;
import numjava.Vector;

public class Test {
	public static void main(String[] args) {
		int[] rowlist = {0, 3, 4};
		int[] collist = {0, 1, 3};
		Number[] data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
		Matrix mat = new Matrix(data, 5, 4);
		mat.printMat();
		System.out.println("----------------------------");

		mat = mat.removeElem(rowlist, collist);
		mat.printMat();
	}
}
