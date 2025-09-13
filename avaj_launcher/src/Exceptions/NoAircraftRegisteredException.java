package src.Exceptions;

public class NoAircraftRegisteredException extends Exception 
{
	public NoAircraftRegisteredException()
	{
		super("Exception thrown: No aircraft registered!!!!");
	}
}
