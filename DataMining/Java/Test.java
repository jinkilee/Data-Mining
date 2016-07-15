import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;

public class Test {
	public static void main(String[] args) {
		Number[] data = {1, 2, 3, 4, 5, 6};
		Vector a = new Vector(data, 6);
		Vector b = new Vector(data, 6);

		NumJava nj = new NumJava();
		System.out.println(nj.dotprod(a, b));
		//Number[] data2 = {1, 2, 3, 4, 5, 6};
		//List<Number> list = Arrays.asList(data);

		/*/
		// Get average
		NumJava nj = new NumJava();
		//System.out.println(nj.average(list));
		//System.out.println(nj.max(list));
		//System.out.println(nj.min(list));
		//System.out.println(nj.sample(list, 3, false));
		//System.out.println(nj.sample(list, 3, true));

		Matrix a = new Matrix(data, 2, 3);
		//Matrix b = new Matrix(data2, 2, 3);
		a.printElem();
		System.out.println("----------------------------");

		//System.out.println(myrandmat.getElem(1, 1));
		//*/
	}
}
