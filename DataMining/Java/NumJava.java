import java.util.ArrayList;

//public class NumJava {
public class NumJava<T extends Number> {
	// Get average of input array	
	T average(ArrayList<T> data) {
		T sum = 0;
		int dataLen = data.size();
		for(int i = 0; i < dataLen; i++)
			//System.out.println(data.get(i));
			sum += data.get(i);
		return sum/dataLen;
	}	
}
