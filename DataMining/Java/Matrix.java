
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
		for(int i = 0; i < this.rows; i++) {
			for(int j = 0; j < this.cols; j++)
				System.out.print(this.mat[i][j] + " ");
			System.out.println("");
		}
	}
}
