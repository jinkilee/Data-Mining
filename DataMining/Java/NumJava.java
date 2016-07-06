import java.util.ArrayList;

public class NumJava {
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
