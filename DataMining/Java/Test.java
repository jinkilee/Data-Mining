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
		Bicycle bicycle = new Bicycle(1, 2, 3);
		Object obj = new Bicycle(1, 2, 3);

		if(obj instanceof Bicycle) {
			Bicycle mybike = (Bicycle)obj;
			System.out.println(mybike.getGear());
		}
		//System.out.println(bicycle.getGear());

		/*/
		int[] rowlist = {0, 3, 4};
		int[] collist = {0, 1, 3};
		Number[] data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

		Matrix mat = new Matrix(data, 4, 5);
		mat.printMat();
		System.out.println(mat.size());
		System.out.println(mat.elemSize());
		/*/
	}
}
