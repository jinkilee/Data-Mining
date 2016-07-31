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
	public static void main(String[] args) throws Exception{
		// Create random Vector

		// Estimate time
		long startTime = System.currentTimeMillis();
		Vector vec1 = Vector.randVec(3000000, 0, 10);
		long estimatedTime = System.currentTimeMillis() - startTime;
		System.out.println(estimatedTime/1000.0);

		startTime = System.currentTimeMillis();
		System.out.println(Vector.normalize(vec1));
		estimatedTime = System.currentTimeMillis() - startTime;
		System.out.println(estimatedTime/1000.0);

		// Print time
		//System.out.println(estimatedTime/1000.0);
	}
}
