import java.util.*;

public class CollectionsDemo {
	public static void main(String args[]) { 
		// create link list object 
		LinkedList<Integer> list = new LinkedList<Integer>();
		Number[] data = {1, 2, 3, 4, 5};
		List<Number> dataList = Arrays.asList(data);

		System.out.println(dataList);
	  
		// populate the list  
		list.add(-18);  
		list.add(40);  
		list.add(-45);  
		list.add(12);

		// comparing using natural ordering
		System.out.println("Max val: " + Collections.max(list,null));          
		System.out.println("Max val: " + Collections.max(dataList,null));          
	}  
}
