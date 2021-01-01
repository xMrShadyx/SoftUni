using System;

namespace moving_09
{
    class Program
    {
        static void Main(string[] args)
        {
            int widthFreeSpace = int.Parse(Console.ReadLine());
            int lenghtFreeSpace = int.Parse(Console.ReadLine());
            int heightFreeSpace = int.Parse(Console.ReadLine());
            int currentFreeSpace = widthFreeSpace * lenghtFreeSpace * heightFreeSpace;

            string command = Console.ReadLine();
            int ownedCubics = 0;
            int anotherCubics = 0;
            
            while (command != "Done" || ownedCubics >= currentFreeSpace)
            {
                
                anotherCubics = int.Parse(command);
                ownedCubics += anotherCubics;
                if (ownedCubics > currentFreeSpace)
                {
                    break;
                }
                command = Console.ReadLine();
            }

            if (command == "Done")
            {
                Console.WriteLine($"{currentFreeSpace - ownedCubics} Cubic meters left.");
            }
            else
            {
                Console.WriteLine($"No more free space! You need {ownedCubics - currentFreeSpace} Cubic meters more.");

            }
        }
    }
}