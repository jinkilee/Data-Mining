// http://www.javatpoint.com/throws-keyword-and-difference-between-throw-and-throws
import java.io.IOException;

class ExceptionThrow {
	//void method(int a) {
	void method(int a) throws IOException {
		if(a > 10)
			throw new IOException("divide by zero");
			//throw new ArithmeticException("divide by zero");
	}
}

public class ThrowTest {
	public static void main(String[] args) {
	//public static void main(String[] args) throws IOException {
		//ExceptionThrow m = new ExceptionThrow();
		//m.method(3);
		//*/
		try {
			ExceptionThrow m = new ExceptionThrow();
			m.method(3);
		}
		catch(IOException e) {
			System.out.println(e);
		}

		//*/
		System.out.println("normal flow");
	}
}
