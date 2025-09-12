package src;

public class Coordinates
{
	private int longitude;
	private int latitute;
	private int height;
	
	Coordinates(int p_longitude, int p_latitude, int p_height)
	{
		longitude = p_longitude;
		latitute = p_latitude;
		height = p_height;
	}

	int getLongitude() { return longitude; }
	int getLatitude() { return latitute; }
	int getHeight() { return height; }
}