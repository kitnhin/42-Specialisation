package src;

import java.util.ArrayList;
import java.util.List;

public class Tower
{
	private List <Flyable> observers = new ArrayList<>();

	public void register(Flyable p_flyable)
	{
		observers.add(p_flyable);
		System.out.println("Registered flyable!!");
	}

	public void unregister(Flyable p_flyable)
	{
		observers.remove(p_flyable);
	}

	protected void conditionChanged()
	{
		//implement ltr
	}
}

// not pointers in java!!!!
