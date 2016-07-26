public class MountainBike extends Bicycle {
	public int seatHeight;
	
	///////////////////////////////////////////////
	// Initialize an Object
	public MountainBike(int cadence, int gear, int speed, int seatHeight) {
		super(cadence, gear, speed);
		this.seatHeight = seatHeight;
	}

	///////////////////////////////////////////////
	// SET methods
	public void setHeight(int seatHeight) {
		this.seatHeight = seatHeight;
	}
	
	///////////////////////////////////////////////
	// GET methods
	public int getHeight() {
		return seatHeight;
	}

	///////////////////////////////////////////////
	// Abstract methods
	public void fly() {
		System.out.println("No I can't fly :(");
	}
}
