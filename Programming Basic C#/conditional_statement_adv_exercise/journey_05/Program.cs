using System;

namespace journey_05
{
    class Program
    {
        static void Main(string[] args)
        {
            double realBudget = double.Parse(Console.ReadLine());
            string seasonChoise = Console.ReadLine();

            if (realBudget <= 100)
            {
                Console.WriteLine("Somewhere in Bulgaria");
                if (seasonChoise == "summer")
                {
                    Console.WriteLine($"Camp - {Math.Abs((realBudget * 0.30)):F2}");
                }
                else
                {
                    Console.WriteLine($"Hotel - {Math.Abs(realBudget * 0.70):F2}");
                }
                
            } else if (realBudget > 100 && realBudget <= 1000)
            {
                Console.WriteLine("Somewhere in Balkans");
                if (seasonChoise == "summer")
                {
                    Console.WriteLine($"Camp - {Math.Abs((realBudget * 0.60) - realBudget):F2}");
                }
                else
                {
                    Console.WriteLine($"Hotel - {Math.Abs((realBudget * 0.80)):F2}");
                }
            } else if (realBudget > 1000)
            {
                Console.WriteLine("Somewhere in Europe");
                Console.WriteLine($"Hotel - {Math.Abs((realBudget * 0.90)):F2}");
            }
        }
    }
}