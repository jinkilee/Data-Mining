package numjava;

import java.util.Random;
import java.lang.Math;
import java.security.SecureRandom;

public class NumJava {
	// Get Average of Number list
	// Input  : Number[] data
	// Output : Number
	public static Number average(Number[] data) {
		Number sum = 0.0;
		for(Number elem:data) {
			sum = sum.doubleValue() + elem.doubleValue();
		}
		return sum.doubleValue()/data.length;
	}

	// Get standard deviation of Number list
	// Input  : Number[] data
	// Output : Number
	public static Number stdev(Number[] data) {
		double avg = average(data).doubleValue();
		double sum = 0.0;
		for(Number elem:data) {
			sum += (Math.pow(elem.doubleValue() - avg, 2));
		}
		return Math.sqrt(sum/(data.length - 1));
	}

	// Get Maxinum of data
	// Input  : Number[] data
	// Output : Number
	public static Number max(Number[] data) {
		double max = data[0].doubleValue();
		for(Number elem:data) {
			if(max > elem.doubleValue())
				continue;
			max = elem.doubleValue();
		}
		return max;
	}

	// Get Minimum of data
	// Input  : Number[] data
	// Output : Number
	public static Number min(Number[] data) {
		double min = data[0].doubleValue();
		for(Number elem:data) {
			if(min <= elem.doubleValue())
				continue;
			min = elem.doubleValue();
		}
		return min;
	}

	// Create random data of length size
	// Input  : int size
	// Output : Number[]
	public static Number[] randNum(int size) {
		Number[] randNum = new Number[size];

		// Generating random values
		SecureRandom randomNumbers = new SecureRandom();
		for(int i = 0; i < size; i++)
			randNum[i] = randomNumbers.nextDouble();

		return randNum;
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
