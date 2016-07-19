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
		Number[] data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		NumJava.printNumber(NumJava.sample(data, 7, false));
		NumJava.printNumber(NumJava.sample(data, 7, true));

		/*/
		NumJava nj = new NumJava();
		Number[] sorted = nj.sort(data);
		for(int i = 0; i < sorted.length; i++)
			System.out.print(sorted[i] + " ");
		System.out.println("");

		//nj.swap(data, 1, 2);
		//Number[] data2 = {1, 2, 3, 4, 5, 6};
		//List<Number> list = Arrays.asList(data);

		// Get average
		NumJava nj = new NumJava();
		//System.out.println(nj.average(list));
		//System.out.println(nj.max(list));
		//System.out.println(nj.min(list));
		//System.out.println(nj.sample(list, 3, false));
		//System.out.println(nj.sample(list, 3, true));

		Matrix a = new Matrix(data, 2, 3);
		//Matrix b = new Matrix(data2, 2, 3);
		a.printElem();
		System.out.println("----------------------------");

		//System.out.println(myrandmat.getElem(1, 1));
		//*/
	}
}
