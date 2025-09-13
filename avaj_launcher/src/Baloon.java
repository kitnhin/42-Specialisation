package src;

public class Baloon extends Aircraft
{
	public Baloon(long p_id, String p_name, Coordinates p_coordinate)
	{
		super(p_id, p_name, p_coordinate);
	}

	private String formatCoordinatesString()
	{
		return "(" + coordinates.getLongitude() + ", " + coordinates.getLatitude() + ", " + coordinates.getHeight() + ")";
	}

	public void updateConditions()
	{
		String weather = WeatherProvider.getInstance().getCurrentWeather(coordinates);
		String aircraft_info = "Balloon#" + name + "(" + id + "): ";

		switch (weather)
		{
			case "SUN":
				coordinates = new Coordinates(coordinates.getLongitude() + 2, coordinates.getLatitude(), Math.min(coordinates.getHeight() + 4, 100));
				Logger.print(aircraft_info + "[BALOON] SUN " + formatCoordinatesString());
				break;
			case "RAIN":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 5);
				Logger.print(aircraft_info + "[BALOON] RAIN " + formatCoordinatesString());
				break;
			case "FOG":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 3);
				Logger.print(aircraft_info + "[BALOON] FOG " + formatCoordinatesString());
				break;
			case "SNOW":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 	15);
				Logger.print(aircraft_info + "[BALOON] SNOW " + formatCoordinatesString());
				break;
		}

		if(coordinates.getHeight() <= 0)
		{
			Logger.print(aircraft_info + "[BALOON] unregistered from weather tower " + formatCoordinatesString());
			this.weatherTower.unregister(this);
		}
	}
}
