package src;

import src.Exceptions.InvalidAircraftException;

public class AircraftFactory
{
	private static AircraftFactory instance = new AircraftFactory();
	private static long id = 1;
	private AircraftFactory() {};

	public Flyable newAircraft(String p_type, String p_name, Coordinates p_coordinates) throws InvalidAircraftException
	{
		switch (p_type)
		{
			case "JetPlane":
				return new JetPlane(id++, p_name, p_coordinates);
			case "Helicopter":
				return new Helicopter(id++, p_name, p_coordinates);
			case "Baloon":
				return new Baloon(id++, p_name, p_coordinates);
			default:
				throw new InvalidAircraftException(p_type);
		}
	}

	public static AircraftFactory getInstance()
	{	
		return instance;
	}
}
