package src;

public class WeatherTower extends Tower
{
	public String getWeather(Coordinates p_coordinate)
	{
		return WeatherProvider.getInstance().getCurrentWeather(p_coordinate);
	}

	public void changeWeather()
	{
		
	}
}
