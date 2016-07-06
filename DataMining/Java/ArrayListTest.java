import java.util.List;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class ArrayListTest {
	public static void main(String[] args) {
		// Add color list
		String[] colors   = {"MAGENTA", "RED", "WHITE", "BLUE", "CYAN"};
		List<String> list = new ArrayList<String>();
		for(String color:colors)
			list.add(color);

		// Add removeColor list
		String[] removeColors   = {"RED", "WHITE", "BLUE"};
		List<String> removeList = new ArrayList<String>();
		for(String color:removeColors)
			removeList.add(color);

		// Print color list
		System.out.println("ArrayList: ");
		for(int i = 0; i < list.size(); i++)
			System.out.print(list.get(i) + " ");
		System.out.println("");

		// Remove removeColors from colors
		removeColors(list, removeList);

		// Print removeColor list
		System.out.println("ArrayList: ");
		for(String color:list)
			System.out.print(color + " ");
		System.out.println("");
	}

	private static void removeColors(Collection<String> collection1, Collection<String> collection2) {
		Iterator<String> iterator = collection1.iterator();

		while(iterator.hasNext()) {
			if(collection2.contains(iterator.next())) {
				iterator.remove();
			}
		}
	}
}
