package numjava;

import java.security.SecureRandom;

public class Matrix {
	int rows;
	int cols;
	Number[][] mat;

	public Matrix(int rows, int cols) {
		this.rows = rows;
		this.cols = cols;
	}

	public Matrix(Number[] elem, int rows, int cols) {
		this.rows = rows;
		this.cols = cols;
		mat = new Number[rows][cols];
		mat = setMatrix(mat, elem, rows, cols);
	}

	private Number[][] setMatrix(Number[][] mat, Number[] elem, int rows, int cols) {
		if(elem.length != rows * cols) {
			System.out.println("Error: rows*cols != elem.size()");
			System.exit(1);
		}

		for(int i = 0; i < rows; i++)
			for(int j = 0; j < cols; j++)
				mat[i][j] = elem[i*cols+j];
		return mat;
	}

	public int getRows() {
		return this.rows;
	}

	public int getCols() {
		return this.cols;
	}

	public Number getElem(int row, int col) {
		return this.mat[row][col];
	}

	public void printElem() {
		int rows = getRows();
		int cols = getCols();
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				System.out.print(getElem(i, j) + " ");
			System.out.println("");
		}
	}
	
	public static void nofunction() {
		System.out.println("I am doing nothing");
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

	// Add matrice : Overloaded
	// Input  : Matrix a, Number num
	// Output : Matrix
	public static Matrix addmat(Matrix a, Number num) {
		int rows = a.getRows();
		int cols = a.getCols();

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() + num.doubleValue();
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

	// Sub matrice : Overloaded
	// Input  : Matrix a, Number num
	// Output : Matrix
	public static Matrix submat(Matrix a, Number num) {
		int rows = a.getRows();
		int cols = a.getCols();

		// Sub matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() - num.doubleValue();
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

	// Multiply matrice : Overloaded
	// Input  : Matrix a, Number num
	// Output : Matrix
	public static Matrix mulmat(Matrix a, Number num) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() * num.doubleValue();
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

	// Divide matrice : Overloaded
	// Input  : Matrix a, Number num
	// Output : Matrix
	public static Matrix divmat(Matrix a, Number num) {
		// Size check
		int rows = a.getRows();
		int cols = a.getCols();

		if(0 == num.doubleValue()) {
			System.out.println("Error: Cannot divide with zero");
			System.exit(1);
		}

		// Add matrix
		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < cols; j++)
				elemNumber[i*cols+j] = a.getElem(i, j).doubleValue() / num.doubleValue();
		}
		Matrix mat = new Matrix(elemNumber, rows, cols);

		return mat;
	}
}
