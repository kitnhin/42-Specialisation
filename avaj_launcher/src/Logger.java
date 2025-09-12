package src;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Logger
{
	private Logger() {};

	static public void print(String str)
	{
		String file = "simulation.txt";

		try
		{
			Files.writeString(Paths.get(file), str); //paths.get transforms the file string to a path object
		}
		catch (IOException e)
		{
            System.err.println("Logging failed: " + e.getMessage());
        }
	}
}
