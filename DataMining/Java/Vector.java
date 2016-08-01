package numjava;

import java.lang.Math;
import java.security.SecureRandom;
import numjava.Matrix;

public class Vector {
	int ndim;
	Number[] elem;

	public Vector(Number[] data, int ndim) {
		if(ndim != data.length) {
			System.out.println("data length != ndim");
			System.exit(1);
		}
		this.ndim = ndim;
		this.elem = setValue(data);
	}

	public int getDim() {
		return this.ndim;
	}

	public double getElem(int idx) {
		return this.elem[idx].doubleValue();
	}

	public void printVector() {
		int ndim = getDim();
		for(int i = 0; i < ndim; i++)
			System.out.print(getElem(i) + " ");
		System.out.println("");
	}

	private Number[] setValue(Number[] data) {
		int ndim = getDim();
		Number[] elem  = new Number[ndim];
		for(int i = 0; i < ndim; i++)
			elem[i] = data[i];
		return elem;
	}

	// Calculate dot-product of two vectors
	// Input  : Vector a, Vector b
	// Output : Number
	public static Number dotprod(Vector a, Vector b) {
		int size = a.getDim();
		if(size != b.getDim()){
			System.out.println("Error: a.getDim() != b.getDim()");
			System.exit(1);
		}

		Number dotprod = 0.0;
		for(int i = 0; i < size; i++)
			dotprod = dotprod.doubleValue() + (a.getElem(i) * b.getElem(i));

		return dotprod;
	}

	// Add two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector addVector(Vector a, Vector b) {
		int size = a.getDim();
		if(size != b.getDim()){
			System.out.println("Error: a.getDim() != b.getDim()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) + b.getElem(i);
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Add vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector addVector(Vector a, Number num) {
		int size = a.getDim();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) + num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Subtract two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector subVector(Vector a, Vector b) {
		int size = a.getDim();
		if(size != b.getDim()){
			System.out.println("Error: a.getDim() != b.getDim()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) - b.getElem(i);
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Subtract vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector subVector(Vector a, Number num) {
		int size = a.getDim();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) - num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Multiply two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector mulVector(Vector a, Vector b) {
		int size = a.getDim();
		if(size != b.getDim()){
			System.out.println("Error: a.getDim() != b.getDim()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) * b.getElem(i);
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Multiply vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector mulVector(Vector a, Number num) {
		int size = a.getDim();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) * num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Divide two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector divVector(Vector a, Vector b) {
		int size = a.getDim();
		if(size != b.getDim()){
			System.out.println("Error: a.getDim() != b.getDim()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) / b.getElem(i);
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Divide vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector divVector(Vector a, Number num) {
		int size = a.getDim();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i) / num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Get a vector of random Number
	// Input  : int ndim, Number min, Number max
	// Output : Number
	public static Vector randVec(int ndim, Number min, Number max) throws Exception {
		Number[] randNumElem = new Number[ndim];
		double maxValue = max.doubleValue();
		double minValue = min.doubleValue();
		double interval = maxValue - minValue;

		if(maxValue <= minValue) {
			throw new Exception("max < min");
		}
		// Generating random values
		SecureRandom randomNumbers = new SecureRandom();
		for(int i = 0; i < ndim; i++)
			randNumElem[i] = randomNumbers.nextDouble()*interval + minValue;

		Vector vec = new Vector(randNumElem, ndim);
		return vec;
	}

	// Get normalize of vector
	// Input  : Vector a
	// Output : double
	public static double normalize(Vector a) {
		int alen = a.getDim();
		double sum = 0.0;
		for(int i = 0; i < alen; i++) {
			sum = sum + Math.pow(a.getElem(i), 2);
		}
		return Math.sqrt(sum);
	}

	// Get outer vector
	// Input  : Vector a, Vector b
	// Output : Matrix
	public static Matrix outer(Vector a, Vector b) {
		int rows = a.getDim();
		int cols = b.getDim();

		Number[] elem = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			double aValue = a.getElem(i);
			for(int j = 0; j < cols; j++)
				elem[i*cols + j] = aValue * b.getElem(j);
		}
		Matrix mat = new Matrix(elem, rows, cols);
		return mat;
	}
}
