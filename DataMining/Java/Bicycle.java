public class Bicycle {
	public  int cadence;
	public  int gear;
	public  int speed;
	private String tag;

	///////////////////////////////////////////////
	// Initialize an Object
	public Bicycle(int cadence, int gear, int speed) {
		this.cadence = cadence;
		this.gear    = gear;
		this.speed   = speed;
		this.tag     = "NA";
	}

	///////////////////////////////////////////////
	// SET members
	public void setCadence(int cadence) {
		this.cadence = cadence;
	}

	public void setGear(int gear) {
		this.gear = gear;
	}

	public void applyBreak(int decrement) {
		speed -= decrement;
	}

	public void speedUp(int increment) {
		speed += increment;
	}

	private void setTag(String tag) {
		this.tag = tag;
	}

	///////////////////////////////////////////////
	// GET members
	public int getCadence() {
		return cadence;
	}

	public int getGear() {
		return gear;
	}

	public int getSpeed() {
		return speed;
	}

	private String getTag() {
		return tag;
	}
}
