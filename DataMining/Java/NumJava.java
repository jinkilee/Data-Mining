import java.util.ArrayList;

public class NumJava {
	/*
	// Get average of input array	
	T average(T[] data) {
		T sum = 0;
		int dataLen = data.size();
		for(int i = 0; i < dataLen; i++)
			sum += data.get(i);
		return sum/dataLen;
	}
	*/

	// generic method printArray                         
	public static <T extends Number> float average(T[] data) {
		// Display array elements
		float sum = 0;
		int dataLen = data.length;
		for(int i = 0; i < dataLen; i++)
			sum += data[i].floatValue();
		return sum/dataLen;
	}
}
