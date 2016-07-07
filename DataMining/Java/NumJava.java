import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class NumJava {
	// Get Average of Number list
	// Input  : List<T extends Number>
	// Output : Double 			# To be precise
	public static <T extends Number> Double average(List<T> data) {
		Double sum = 0.0;
		for(T elem:data) {
			sum += elem.floatValue();
		}
		return sum/data.size();
	}

	// Get Maxinum of data
	// Input  : List<T extends Number>
	// Output : T
	public static <T extends Number> Number max(List<T> data) {
		Number max = 0;
		for(T elem:data) {
			if(max.doubleValue() > elem.doubleValue())
				continue;
			max = elem.floatValue();
		}

		//return Collections.max(data, null);
		return max;
	}
}
