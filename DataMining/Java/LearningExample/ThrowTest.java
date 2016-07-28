// http://www.javatpoint.com/throws-keyword-and-difference-between-throw-and-throws

public class ThrowTest {
	public static void validate(int age) {
		if(18 > age)
			throw new ArithmeticException("Not valid");
		else
			System.out.println("Welcome :)");
	}
	public static void main(String[] args) {
		validate(13);
		System.out.println("Rest of codes");
	}
}
