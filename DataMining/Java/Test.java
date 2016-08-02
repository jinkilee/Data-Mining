import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;
import java.lang.Math;

import numjava.NumJava;
import numjava.Matrix;
import numjava.Vector;

public class Test {
	public static void main(String[] args) throws Exception {
		// Create random Vector
		Matrix mat = Matrix.randMat(8000, 8000, 0, 5);

		// Estimate time
		long startTime = System.currentTimeMillis();
		Matrix newmat = Matrix.reshape(mat, 800, 80000);
		long estimatedTime = System.currentTimeMillis() - startTime;

		// Print time
		System.out.println(estimatedTime/1000.0);
	}
}
