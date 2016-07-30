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
		Number[] data = NumJava.randNum(100000);

		// Estimate time
		long startTime = System.currentTimeMillis();
		//NumJava.average(data);
		NumJava.stdev(data);
		long estimatedTime = System.currentTimeMillis() - startTime;

		// Print time
		System.out.println(estimatedTime/1000.0);
	}
}
