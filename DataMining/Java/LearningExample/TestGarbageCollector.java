import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class TestGarbageCollector {  
	/*
	protected void finalize() throws Throwable {
		try {
			close();
		}
		finally {
			super.finalize();
		}
	}
	*/

	public static void main(String args[]) {
		try {
			BufferedReader br = new BufferedReader(new FileReader("data.txt"));
			String strLine;
			//Read File Line By Line
			while (null != (strLine = br.readLine()))   {
				System.out.println(strLine);
			}
		}
		catch(FileNotFoundException ex) {
			System.out.println("No File Found");
		}
		catch(IOException ex) {
			System.out.println("IOException");
		}
		/*
		finally {
			try {
				br.close();
			}
			catch(FileNotFoundException ex) {
			}
			catch(IOException e){
			}
		}*/

		System.gc();
	}  
}  

