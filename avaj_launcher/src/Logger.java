package src;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class Logger
{
	private Logger() {};
	private static boolean clearfile = true;

	static public void print(String str)
	{
		String file = "simulation.txt";

		try
		{
			if(clearfile)
			{
				Files.writeString(Paths.get(file), "");
				clearfile = false;
			}

			Files.writeString(Paths.get(file), str + "\n", StandardOpenOption.CREATE, StandardOpenOption.APPEND); //paths.get transforms the file string to a path object
		}
		catch (IOException e)
		{
            System.err.println("Logging failed: " + e.getMessage());
        }
	}
}
