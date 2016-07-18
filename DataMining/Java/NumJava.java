package numjava;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;
import java.security.SecureRandom;


public class NumJava {
	//////////////////////////////////////////////////////////////////
	// Get Average of Number list
	// Input  : List<T extends Number>
	// Output : Double 			# To be precise
	public static <T extends Number> Number average(Number[] data) {
		Number sum = 0.0;
		for(Number elem:data) {
			sum = sum.doubleValue() + elem.doubleValue();
		}
		return sum.doubleValue()/data.length;
	}
	//////////////////////////////////////////////////////////////////

	/*
	// Sort Number[]
	public static Number[] sort(Number[] data) {
		return quickSort(data, 0, data.length - 1);
	}

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

	// Get sample of data
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

	// Call from sort()
	// Input  : Number[] data, int low, int high
	// Output : Number[]
	private static Number[] quickSort(Number[] data, int low, int high) {
		double pivot = data[low+(high-low)/2].doubleValue();
		int i = low;
		int j = high;
		//if(1 == data.length)
			//return data.length;

		while(i <= j) {
			while(data[i].doubleValue() < pivot)
				i++;
			while(data[j].doubleValue() > pivot)
				j--;
			if(i <= j) {
				swap(data, i, j);
				i++;
				j--;
			}
		}
		if(low < j)  quickSort(data, low, j);
		if(i < high) quickSort(data, i, high);

		return data;
	}

	private static void swap(Number[] array, int a, int b) {
		Number tmp;
		tmp = array[a];
		array[a] = array[b];
		array[b] = tmp;
	}
	*/
}
