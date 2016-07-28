public class TryCatchTest {
	public static void main(String[] args) {
	
		/*/
		try{  
			int data = 25/0;  
			System.out.println(data);  
		}  
		catch(NullPointerException e) {
			System.out.println(e);
		}  
		finally {
			System.out.println("finally block is always executed");
		}  
		System.out.println("rest of the code...");  
		/*/
		//*/
		try {
			int data = 5/0;
			System.out.println(data);
		}
		// If there is no catch-block that handles divide-by-zero
		// Java default exception handler will be called and program will be terminated
		// However, even in this case, finally-block will be executed!!!
		catch(ArithmeticException e) {
			System.out.println(e);
		}
		catch(ArrayIndexOutOfBoundsException e) {
			System.out.println(e);
		}
		finally {
			// To handle sonething important code, such as closing files or network sessions
			// finally blocks will be always executed no matter error was occurred or not
			System.out.println("I am a finally-block");
		}
		System.out.println("Rest of the codes");
		//*/
	}
}
