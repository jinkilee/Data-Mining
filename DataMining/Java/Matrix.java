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

	public String size() {
		return "(" + getRows() + "," + getCols() + ")";
	}

	public int elemSize() {
		return getRows() * getCols();
	}

	public int getCols() {
		return this.cols;
	}

	public Number getElem(int row, int col) {
		return this.mat[row][col];
	}

	public void printMat() {
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
	public static Matrix randMat(int rows, int cols, Number min, Number max) {
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
	public static Matrix addMat(Matrix a, Matrix b) {
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
	public static Matrix addMat(Matrix a, Number num) {
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
	public static Matrix subMat(Matrix a, Matrix b) {
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
	public static Matrix subMat(Matrix a, Number num) {
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
	public static Matrix mulMat(Matrix a, Matrix b) {
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
	public static Matrix mulMat(Matrix a, Number num) {
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
	public static Matrix divMat(Matrix a, Matrix b) {
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
	public static Matrix divMat(Matrix a, Number num) {
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

	// Remove some rows or cols
	// Input  : int[] rowlist, int[] collist
	// Output : Matrix
	public Matrix removeElem(int[] rowlist, int[] collist) {
		// Size check
		int rows = getRows();
		int cols = getCols();
		int rowlistlen = rowlist.length;
		int collistlen = collist.length;

		if(rows == rowlistlen || cols == collistlen) {
			System.out.println("Error: it removes all elements of Matrix");
			System.exit(1);
		}
	
		int newrow = rows - rowlistlen;
		int newcol = cols - collistlen;
		int skiprow = 0;
		Number[] elemNumber = new Number[newrow*newcol];
		for(int i = 0; i < rows; i++) {
			// Check if skip i row
			if(true == hasElem(rowlist, i)) {
				skiprow++;
				continue;
			}

			int skipcol = 0;
			for(int j = 0; j < cols; j++) {
				// Check if skip j col
				if(true == hasElem(collist, j)) {
					skipcol++;
					continue;
				}
				elemNumber[(i-skiprow)*newcol + (j-skipcol)] = getElem(i, j);
			}
		}
		Matrix mat = new Matrix(elemNumber, newrow, newcol);
		return mat;
	}
	
	public boolean hasElem(int[] a, int num) {
		int len = a.length;
		for(int i = 0; i < len; i++) {
			if(a[i] == num)
				return true;
		}
		return false;
	}

	// Divide matrice : Overloaded
	// Input  : Matrix a, Number num
	// Output : Matrix
	public static Matrix dotprod(Matrix a, Matrix b) {
		int rows = a.getRows();
		int cols = a.getCols();
		int brows = b.getRows();
		int bcols = b.getCols();

		if(cols != b.getRows()) {
			System.out.println("Error: Matrix Size Error");
			System.exit(1);
		}

		Number[] elemNumber = new Number[rows*bcols];
		for(int j = 0; j < bcols; j++) {
			Number[] bnum = new Number[cols];
			for(int k = 0; k < cols; k++)
				bnum[k] = b.getElem(k, j);

			for(int i = 0; i < rows; i++) {
				Number sum = 0;
				for(int k = 0; k < cols; k++)
					sum = sum.doubleValue() + (a.getElem(i, k).doubleValue() * bnum[k].doubleValue());
				elemNumber[j*rows+i] = sum;
			}
		}
		Matrix mat = new Matrix(elemNumber, bcols, rows);

		return transpose(mat);
	}

	// Transpose Matrix
	// Input  : Matrix a
	// Output : Matrix
	public static Matrix transpose(Matrix a) {
		int rows = a.getRows();
		int cols = a.getCols();

		Number[] elemNumber = new Number[rows*cols];
		for(int i = 0; i < rows; i++) {
			for(int j = 0 ; j < cols; j++)
				elemNumber[j*rows+i] = a.getElem(i,j);
		}
		Matrix mat = new Matrix(elemNumber, cols, rows);
		return mat;
	}
}
