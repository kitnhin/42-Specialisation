package src;

public class WeatherProvider
{
	private String[] weather = { "RAIN", "FOG", "SUN", "SNOW"};
	private static WeatherProvider instance = new WeatherProvider();

	//private the constructor so u cannot call new or instantiate it
	private WeatherProvider() {}
	public static WeatherProvider getInstance()
	{	
		return instance;
	}

	public String getCurrentWeather(Coordinates p_Coordinates)
	{
		int seed = p_Coordinates.getHeight() + p_Coordinates.getLatitude() + p_Coordinates.getLongitude();
		return weather[seed % 4];
	}
}
