package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;

import src.Exceptions.InvalidAircraftException;
import src.Exceptions.InvalidInputFileException;
import src.Exceptions.InvalidTotalIterationsException;
import src.Exceptions.NoAircraftRegisteredException;

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

	public void readFile() throws IOException, InvalidInputFileException, InvalidAircraftException, InvalidTotalIterationsException, NoAircraftRegisteredException
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

	private void extractValues() throws InvalidInputFileException, InvalidAircraftException, InvalidTotalIterationsException, NoAircraftRegisteredException
	{
		//parse total iterations
		int first_newline = file_contents.indexOf("\n");
		String first_line = file_contents.substring(0, first_newline);

		first_line = first_line.trim();

		if(!check_all_int(first_line) || first_line.isEmpty())
			throw new InvalidInputFileException("Invalid first line - " + first_line);

		totalIterations = Integer.parseInt(first_line);
		if(totalIterations < 1 || totalIterations > 100000)
			throw new InvalidTotalIterationsException(first_line);

		//parse the rest of the files
		int index = skip_whitespace(first_newline, file_contents);
		int aircrafts_registered = 0;
		while(index < file_contents.length())
		{
			int newline_index = file_contents.indexOf("\n", index);
			String line = file_contents.substring(index, newline_index);
			registerAircraft(line, aircrafts_registered);
			index = skip_whitespace(newline_index, file_contents);
			aircrafts_registered++;
		}

		if(aircrafts_registered == 0)
			throw new NoAircraftRegisteredException();
	}

	private String extractField(String line, int start, boolean check_int, boolean last_line) throws InvalidInputFileException
	{
		String field = "";
		int space = line.indexOf(" ", start);
		if(space == -1 && !last_line)
			throw new InvalidInputFileException("Invalid line - " + line);

		if(last_line)
			field = line.substring(start, line.length()).trim();
		else
			field = line.substring(start, space);

		if(check_int && !check_all_int(field))
			throw new InvalidInputFileException("Invalid line - " + line);

		if(field.isEmpty())
			throw new InvalidInputFileException("Invalid line - " + line);
		
		return field;
	}

	private void registerAircraft(String line, int aircrafts_registered) throws InvalidInputFileException, InvalidAircraftException
	{
		int start = 0;

		//extract type
		String type = extractField(line, start, false, false);
		start = skip_whitespace(line.indexOf(" ", start), line);

		//extract name
		String name = extractField(line, start, false, false);
		start = skip_whitespace(line.indexOf(" ", start), line);

		//extract longitude
		String longitude = extractField(line, start, true, false);
		start = skip_whitespace(line.indexOf(" ", start), line);

		//extract latitude
		String latitude = extractField(line, start, true, false);
		start = skip_whitespace(line.indexOf(" ", start), line);

		//extract height
		String height = extractField(line, start, true, true);

		//register the new aircraft
		Coordinates coords = new Coordinates(Integer.parseInt(longitude), Integer.parseInt(latitude), Math.max(0, Math.min(Integer.parseInt(height), 100)));
		Flyable Aircraft = AircraftFactory.getInstance().newAircraft(type, name, coords);
		weathertower.register(Aircraft);
		Aircraft.registerTower(weathertower);
		
		// System.out.println("Filereader registered aircraft: " + type + " " + name + " at coordinates (" + longitude + ", " + latitude + ", " + height + ")");
		Logger.print(type + "#" + name + "(" + String.valueOf(aircrafts_registered + 1) + ")" + " has been registered to the tower (" + coords.getLongitude() + ", " + coords.getLatitude() + ", " + coords.getHeight() + ")");
	}

	private boolean check_all_int(String str)
	{
		for(int i = 0; i < str.length(); i++)
		{
			if(!Character.isDigit(str.toCharArray()[i]) && str.toCharArray()[i] != '-')
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
