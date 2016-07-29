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
		// Random matrices creation
		Matrix m1 = Matrix.randMat(1000, 1000, 0, 10);
		Matrix m2 = Matrix.randMat(1000, 1000, 0, 10);
		System.out.println("------------------------");

		// Estimate time
		long startTime = System.currentTimeMillis();
		Matrix m3 = Matrix.dot(m1, m2);
		long estimatedTime = System.currentTimeMillis() - startTime;

		// Print time
		System.out.println(estimatedTime/1000.0);
	}
}
