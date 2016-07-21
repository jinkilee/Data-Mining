package numjava;

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

	public Number getElem(int idx) {
		return this.elem[idx];
	}

	public int size() {
		return getDim();
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
		int size = a.size();
		if(size != b.size()){
			System.out.println("Error: a.size() != b.size()");
			System.exit(1);
		}

		Number dotprod = 0.0;
		for(int i = 0; i < size; i++)
			dotprod = dotprod.doubleValue() + (a.getElem(i).doubleValue() * b.getElem(i).doubleValue());

		return dotprod;
	}

	// Add two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector addVector(Vector a, Vector b) {
		int size = a.size();
		if(size != b.size()){
			System.out.println("Error: a.size() != b.size()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() + b.getElem(i).doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Add vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector addVector(Vector a, Number num) {
		int size = a.size();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() + num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Subtract two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector subVector(Vector a, Vector b) {
		int size = a.size();
		if(size != b.size()){
			System.out.println("Error: a.size() != b.size()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() - b.getElem(i).doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Subtract vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector subVector(Vector a, Number num) {
		int size = a.size();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() - num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Multiply two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector mulVector(Vector a, Vector b) {
		int size = a.size();
		if(size != b.size()){
			System.out.println("Error: a.size() != b.size()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() * b.getElem(i).doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Multiply vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector mulVector(Vector a, Number num) {
		int size = a.size();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() * num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Divide two vectors
	// Input  : Vector a, Vector b
	// Output : Vector
	public static Vector divVector(Vector a, Vector b) {
		int size = a.size();
		if(size != b.size()){
			System.out.println("Error: a.size() != b.size()");
			System.exit(1);
		}

		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() / b.getElem(i).doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}

	// Divide vector : Overloaded
	// Input  : Vector a, Number num
	// Output : Vector
	public static Vector divVector(Vector a, Number num) {
		int size = a.size();
		Number[] resultData = new Number[size];
		for(int i = 0; i < size; i++)
			resultData[i] = a.getElem(i).doubleValue() / num.doubleValue();
		Vector result = new Vector(resultData, size);

		return result;
	}
}
