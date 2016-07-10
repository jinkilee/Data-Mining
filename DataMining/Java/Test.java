import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;

public class Test {
	public static void main(String[] args) {
		Number[] data = {0, 1, 2, 3, 4, 5.1};
		List<Number> list = Arrays.asList(data);

		//*/
		// Get average
		NumJava nj = new NumJava();
		//System.out.println(nj.average(list));
		//System.out.println(nj.max(list));
		//System.out.println(nj.min(list));
		//System.out.println(nj.sample(list, 3, false));
		//System.out.println(nj.sample(list, 3, true));
		Number[][] myrandmat = nj.randmat(2, 3, -1, 1);
		for(int i = 0; i < 2; i++) {
			for(int j = 0; j < 3; j++)
				System.out.print(myrandmat[i][j] + " ");
			System.out.println("");
		}
		//*/
	}
}
