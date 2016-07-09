import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;

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
	// Output : T
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
	// Input  : List<T extends Number>
	// Output : T
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
}
