
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
}
