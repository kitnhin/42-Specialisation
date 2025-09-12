package src.Exceptions;

public class InvalidInputFileException extends Exception
{
	public InvalidInputFileException(String msg)
	{
		super("Exception thrown: " + msg);
	}
}
