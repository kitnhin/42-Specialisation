package src;

public class JetPlane extends Aircraft
{
	public JetPlane(long p_id, String p_name, Coordinates p_coordinate)
	{
		super(p_id, p_name, p_coordinate);
	}

	public void updateConditions()
	{
		String weather = WeatherProvider.getInstance().getCurrentWeather(coordinates);
		String aircraft_info = "JetPlane#" + name + "(" + id + "): ";
		System.out.println("current weather: " + weather);

		switch (weather)
		{
			case "SUN":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 10, Math.min(coordinates.getHeight() + 2, 100));
				Logger.print(aircraft_info + "[JETPLANE] SUN");
				break;
			case "RAIN":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 5, coordinates.getHeight());
				Logger.print(aircraft_info + "[JETPLANE] RAIN");
				break;
			case "FOG":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude() + 1, coordinates.getHeight());
				Logger.print(aircraft_info + "[JETPLANE] FOG");
				break;
			case "SNOW":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 7);
				Logger.print(aircraft_info + "[JETPLANE] SNOW");
				break;
		}

		if(coordinates.getHeight() <= 0)
		{
			Logger.print(aircraft_info + "[JETPLANE] unregistered");
			this.weatherTower.unregister(this);
		}
	}
}
