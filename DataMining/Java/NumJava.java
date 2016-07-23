package numjava;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Random;
import java.security.SecureRandom;


public class NumJava {
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

	// Get Maxinum of data
	// Input  : List<T extends Number>
	// Output : Number
	public static Number max(Number[] data) {
		Number max = data[0];
		for(Number elem:data) {
			if(max.doubleValue() > elem.doubleValue())
				continue;
			max = elem;
			//max = elem.doubleValue();
		}

		return max;
	}

	// Get Minimum of data
	// Input  : List<T extends Number>
	// Output : Number
	public static Number min(Number[] data) {
		Number min = data[0];
		for(Number elem:data) {
			if(min.doubleValue() <= elem.doubleValue())
				continue;
			min = elem;
		}

		return min;
	}

	// Sort Number[]
	public static Number[] sort(Number[] data) {
		return quickSort(data, 0, data.length - 1);
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

	// Print Number[]
	// Input  : Number[] data
	// Output : void
	public static void printNumber(Number[] data) {
		int dataSize = data.length;
		for(int i = 0; i < dataSize; i++)
			System.out.print(data[i] + " ");
		System.out.println("");
	}

	// Get sample of data
	// Input  : Number[] data, int sampleSize, boolean duplicate
	// Output : Number[]
	public static Number[] sample(Number[] data, int sampleSize, boolean duplicate) {
		// Creating sampleData
		Number[] sampleData = new Number[sampleSize];
		int dataSize = data.length;
		Random rand = new Random(); 

		// DO NOT allow duplicate sampling
		if(false == duplicate) {
			// Shuffle data
			for(int i = 0; i < dataSize; i++)
				swap(data, i, rand.nextInt(data.length));

			for(int i = 0; i < sampleSize; i++)
				sampleData[i] = data[i];
		}
		// Allow duplicate sampling
		else {
			for(int i = 0; i < sampleSize; i++)
				sampleData[i] = data[rand.nextInt(dataSize)];
		}

		return sampleData;
	}
}
