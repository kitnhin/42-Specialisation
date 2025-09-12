package src;

public class Helicopter extends Aircraft
{
	public Helicopter(long p_id, String p_name, Coordinates p_coordinate)
	{
		super(p_id, p_name, p_coordinate);
	}

	public void updateConditions()
	{
		String weather = WeatherProvider.getInstance().getCurrentWeather(coordinates);
		String aircraft_info = "Helicopter#" + name + "(" + id + "): ";

		switch (weather)
		{
			case "SUN":
				coordinates = new Coordinates(coordinates.getLongitude() + 10, coordinates.getLatitude(), Math.min(coordinates.getHeight() + 2, 100));
				Logger.print(aircraft_info + "[HELICOPTER] SUN");
				break;
			case "RAIN":
				coordinates = new Coordinates(coordinates.getLongitude() + 5, coordinates.getLatitude(), coordinates.getHeight());
				Logger.print(aircraft_info + "[HELICOPTER] RAIN");
				break;
			case "FOG":
				coordinates = new Coordinates(coordinates.getLongitude() + 1, coordinates.getLatitude(), coordinates.getHeight());
				Logger.print(aircraft_info + "[HELICOPTER] FOG");
				break;
			case "SNOW":
				coordinates = new Coordinates(coordinates.getLongitude(), coordinates.getLatitude(), coordinates.getHeight() - 12);
				Logger.print(aircraft_info + "[HELICOPTER] SNOW");
				break;
		}

		if(coordinates.getHeight() <= 0)
		{
			Logger.print(aircraft_info + "[HELICOPTER] unregistered");
			this.weatherTower.unregister(this);
		}
	}
}
