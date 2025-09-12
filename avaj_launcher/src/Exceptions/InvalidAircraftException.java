package src.Exceptions;

public class InvalidAircraftException extends Exception
{
	public InvalidAircraftException(String p_type)
	{
		super("Exception thrown: invalid aircraft specified - " + p_type);
	}
}
