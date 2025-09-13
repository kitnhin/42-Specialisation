package src;

import src.Exceptions.InvalidArgumentsException;

public class Simulator
{
	private static WeatherTower weathertower;
	private static MyFileReader filereader;
	private static long totalIterations;

	public static void main(String[] args)
	{
		// AircraftFactory INVALID = new AircraftFactory();
		try
		{
			if(args.length != 1)
				throw new InvalidArgumentsException();

			weathertower = new WeatherTower();
			filereader =  new MyFileReader(args[0], weathertower);
			filereader.readFile();
			totalIterations = filereader.getTotalIterations();

			//looopppp
			for(int current_iteration = 1; current_iteration <= totalIterations; current_iteration++)
			{
				Logger.print("\n=============== Iteration: " + String.valueOf(current_iteration) + " ===============");
				weathertower.changeWeather();
			}

		}
		catch(Exception e)
		{
			System.err.println("\n=============== Simulation stopped ===============");
			System.err.println(e.getMessage() + "\n");
			Logger.print("\n=============== Simulation stopped ===============");
			Logger.print(e.getMessage());
		}
	}
};
