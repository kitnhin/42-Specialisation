package src;

public class JetPlane extends Aircraft
{
	public JetPlane(long p_id, String p_name, Coordinates p_coordinate)
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
		String aircraft_info = "JetPlane#" + name + "(" + id + "): ";

		switch (weather)
		{
			case "SUN":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 10, Math.min(coordinates.getHeight() + 2, 100));
				Logger.print(aircraft_info + "[JETPLANE] SUN " + formatCoordinatesString());
				break;
			case "RAIN":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 5, coordinates.getHeight());
				Logger.print(aircraft_info + "[JETPLANE] RAIN " + formatCoordinatesString());
				break;
			case "FOG":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 1, coordinates.getHeight());
				Logger.print(aircraft_info + "[JETPLANE] FOG " + formatCoordinatesString());
				break;
			case "SNOW":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 7);
				Logger.print(aircraft_info + "[JETPLANE] SNOW " + formatCoordinatesString());
				break;
		}

		if(coordinates.getHeight() <= 0)
		{
			Logger.print(aircraft_info + "[JETPLANE] unregistered from weather tower " + formatCoordinatesString());
			this.weatherTower.unregister(this);
		}
	}
}
