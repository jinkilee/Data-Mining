class demo
{
	/* Lesson leart : To call non-static method inside the static method, you should create an instance */
	public static void main(String args[]) {
		demo dm = new demo();	// create an instance
		dm.add(10,20);		// can call non-static function because of the instance.
	}

	public void add(int x ,int y) {
		int a=x;
		int b=y;
		int c=a+b;
		System.out.println("addition"+c);
	}
}
