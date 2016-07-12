import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;
import java.security.SecureRandom;

public class NumJava {
	// Get Average of Number list
	// Input  : List<T extends Number>
	// Output : Double 			# To be precise
	public static <T extends Number> Number average(List<T> data) {
		Number sum = 0.0;
		for(T elem:data) {
			sum = sum.doubleValue() + elem.doubleValue();
		}
		return sum.doubleValue()/data.size();
	}

	// Get Maxinum of data
	// Input  : List<T extends Number>
	// Output : Number
	public static <T extends Number> Number max(List<T> data) {
		Number max = data.get(0);
		for(T elem:data) {
			if(max.doubleValue() > elem.doubleValue())
				continue;
			max = elem.floatValue();
		}

		return max;
	}

	// Get Minimum of data
	// Input  : List<T extends Number>
	// Output : Number
	public static <T extends Number> Number min(List<T> data) {
		Number min = data.get(0);
		for(T elem:data) {
			if(min.doubleValue() <= elem.doubleValue())
				continue;
			min = elem.floatValue();
		}

		return min;
	}

	// Get Minimum of data
	// Input  : List<T> data, int sampleSize, boolean duplicate
	// Output : List<Number>
	public static <T extends Number> List<Number> sample(List<T> data, int sampleSize, boolean duplicate) {
		// Creating Number List for return value
		Number[] sampleData = new Number[sampleSize];

		// Does not allow duplicated sample
		if(false == duplicate) {
			// Shuffling for randomization
			Collections.shuffle(data);
			for(int i = 0; i < sampleSize; i++)
				sampleData[i] = data.get(i);
		}
		// Allow duplicated sample
		else {
			Random rand = new Random(); 
			for(int i = 0; i < sampleSize; i++)
				sampleData[i] = data.get(rand.nextInt(data.size()));
		}
		return Arrays.asList(sampleData);
	}

	// Get a matrix of random Number
	// Input  : int rows, int cols, Number min, Number max
	// Output : Number[][]
	public static Matrix randmat(int rows, int cols, Number min, Number max) {
		// Creating a matrix of rows x cols
		Number[] randNumElem = new Number[rows*cols];

		// Generating random values
		SecureRandom randomNumbers = new SecureRandom();
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				randNumElem[i*cols+j] = randomNumbers.nextDouble()*(max.doubleValue() - min.doubleValue()) + min.doubleValue();
		}

		Matrix mat = new Matrix(randNumElem, rows, cols);
		return mat;
	}

	// Add matrice
	// Input  : Matrix a, Matrix b
	// Output : Matrix
	public static Matrix addmat(Matrix a, Matrix b) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();
		if(rows != b.getRows() || cols != b.getCols()) {
			System.out.println("Error: Size of matrice differ");
			System.exit(1);
		}

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() + b.getElem(i, j).doubleValue();
		}
		Matrix mat = new Matrix(elemNumber, rows, cols);

		return mat;
	}

	// Substract matrice
	// Input  : Matrix a, Matrix b
	// Output : Matrix
	public static Matrix submat(Matrix a, Matrix b) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();
		if(rows != b.getRows() || cols != b.getCols()) {
			System.out.println("Error: Size of matrice differ");
			System.exit(1);
		}

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() - b.getElem(i, j).doubleValue();
		}
		Matrix mat = new Matrix(elemNumber, rows, cols);

		return mat;
	}

	// Multiply matrice
	// Input  : Matrix a, Matrix b
	// Output : Matrix
	public static Matrix mulmat(Matrix a, Matrix b) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();
		if(rows != b.getRows() || cols != b.getCols()) {
			System.out.println("Error: Size of matrice differ");
			System.exit(1);
		}

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() * b.getElem(i, j).doubleValue();
		}
		Matrix mat = new Matrix(elemNumber, rows, cols);

		return mat;
	}

	// Divide matrice
	// Input  : Matrix a, Matrix b
	// Output : Matrix
	public static Matrix divmat(Matrix a, Matrix b) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();
		if(rows != b.getRows() || cols != b.getCols()) {
			System.out.println("Error: Size of matrice differ");
			System.exit(1);
		}

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() / b.getElem(i, j).doubleValue();
		}
		Matrix mat = new Matrix(elemNumber, rows, cols);

		return mat;
	}
}
