package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;

import src.Exceptions.InvalidAircraftException;
import src.Exceptions.InvalidInputFileException;

public class MyFileReader
{
	private String file_contents = "";
	private String filename;
	private long totalIterations = 0;
	private WeatherTower weathertower;

	public MyFileReader(String p_filename, WeatherTower p_weatertower)
	{
		filename = p_filename;
		weathertower = p_weatertower;
	}

	public void readFile() throws IOException, InvalidInputFileException, InvalidAircraftException
	{
		//try with block, so the fd closes after the code even if an error is thrown ornot
        try (BufferedReader reader = new BufferedReader(new FileReader(filename)))
		{
			String line;
			
			while((line = reader.readLine()) != null)
				file_contents += line + "\n";
			
			// System.out.println(file_contents);

			if(file_contents.trim().length() == 0)
				throw new InvalidInputFileException("File empty!");

			extractValues();
		}
	}

	private void extractValues() throws InvalidInputFileException, InvalidAircraftException
	{
		//parse total iterations
		int first_newline = file_contents.indexOf("\n");
		String first_line = file_contents.substring(0, first_newline);

		first_line = first_line.trim();

		if(!check_all_int(first_line))
			throw new InvalidInputFileException("Invalid first line!");

		totalIterations = Integer.parseInt(first_line);

		//parse the rest of the files
		int index = skip_whitespace(first_newline, file_contents);
		while(index < file_contents.length())
		{
			int newline_index = file_contents.indexOf("\n", index);
			String line = file_contents.substring(index, newline_index);
			registerAircraft(line);
			index = skip_whitespace(newline_index, file_contents);
		}
	}

	private void registerAircraft(String line) throws InvalidInputFileException, InvalidAircraftException
	{
		int start = 0;

		//extract type
		int space = line.indexOf(" ");
		String type = line.substring(start, space);
		start = skip_whitespace(space, line);
		
		if(!(type.equals("Baloon") || type.equals("Helicopter") || type.equals("JetPlane")))
    		throw new InvalidInputFileException("Invalid line - " + line);

		//extract name
		space = line.indexOf(" ", start);

		String name = line.substring(start, space);
		start = skip_whitespace(space, line);

		//extract longitude
		space = line.indexOf(" ", start);
		String longitude = line.substring(start, space);
		start = skip_whitespace(space, line);
		if(!check_all_int(longitude))
			throw new InvalidInputFileException("Invalid line - " + line);

		//extract latitude
		space = line.indexOf(" ", start);
		String latitude = line.substring(start, space);
		start = skip_whitespace(space, line);
		if(!check_all_int(latitude))
			throw new InvalidInputFileException("Invalid line - " + line);

		//extract height
		String height = line.substring(start, line.length()).trim();
		if(!check_all_int(height))
			throw new InvalidInputFileException("Invalid line - " + line);

		//register the new aircraft
		Coordinates coords = new Coordinates(Integer.parseInt(longitude), Integer.parseInt(latitude), Integer.parseInt(height));
		Flyable Aircraft = AircraftFactory.getInstance().newAircraft(type, name, coords);
		weathertower.register(Aircraft);
		
		System.out.println("Filereader registered aircraft: " + type + " " + name + " at coordinates (" + longitude + ", " + latitude + ", " + height + ")");
	}

	private boolean check_all_int(String str)
	{
		for(int i = 0; i < str.length(); i++)
		{
			if(!Character.isDigit(str.toCharArray()[i]))
				return false;
		}
		return true;
	}

	private int skip_whitespace(int index, String str)
	{
		while(index < str.length() && Character.isWhitespace(str.toCharArray()[index]))
			index++;
		
		return index;
	}

	public long getTotalIterations()
	{
		return totalIterations;
	}
}
