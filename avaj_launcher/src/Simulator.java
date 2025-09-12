package src;

public class Simulator
{
	private static WeatherTower weathertower;
	private static MyFileReader filereader;

	public static void main(String[] args)
	{
		if(args.length != 1)
		{
			System.err.println("wrong usage bruh");
			return;
		}

		try
		{
			// Coordinates coords = new Coordinates(100, 100, 100);
			// Flyable jett = AircraftFactory.getInstance().newAircraft("JetPlane", "Jett", coords);
			// jett.updateConditions();

			weathertower = new WeatherTower();
			filereader =  new MyFileReader(args[0], weathertower);
			filereader.readFile();
		}
		catch(Exception e)
		{
			System.err.println(e.getMessage());
		}
	}
};
