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
		Vector a = Vector.randVec(1000, 0, 10);
		Vector b = Vector.randVec(1000, 0, 10);

		// Estimate time
		long startTime = System.currentTimeMillis();
		Matrix c = Vector.outer(a, b);
		long estimatedTime = System.currentTimeMillis() - startTime;

		// Print time
		System.out.println(estimatedTime/1000.0);
	}
}
