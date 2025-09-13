package src.Exceptions;

public class InvalidTotalIterationsException extends Exception
{
	public InvalidTotalIterationsException(String msg)
	{
		super("Exception thrown: Invalid total iterations - " + msg);
	}
}
