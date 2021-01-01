using System;

namespace fishing_boat_04
{
    class Program
    {
        static void Main(string[] args)
        {
            double groupBudget = Double.Parse(Console.ReadLine());
            string currentSeason = Console.ReadLine();
            int amountFishermans = int.Parse(Console.ReadLine());

            double boatPrice = 0.0;
            
            switch (currentSeason)
            {
                case ("Spring"):
                    boatPrice = 3000;
                    break;
                case ("Summer"):
                case ("Autumn"):
                    boatPrice = 4200;
                    break;
                case ("Winter"):
                    boatPrice = 2600;
                    break;
            }

            double currPrice = 0.0;
            if (amountFishermans <= 6)
            {
                currPrice = boatPrice * 0.90;
            } else if (amountFishermans > 7 && amountFishermans <= 11)
            {
                currPrice = boatPrice * 0.85;
            } else if (amountFishermans > 12)
            {
                currPrice = boatPrice * 0.75;
            }

            if (amountFishermans % 2 == 0 && currentSeason != "Autumn")
            {
                currPrice = currPrice * 0.95;
            }

            if (currPrice > groupBudget)
            {
                Console.WriteLine($"Not enough money! You need {currPrice - groupBudget:F2} leva.");
            }
            else
            {
                Console.WriteLine($"Yes! You have {groupBudget - currPrice:F2} leva left.");   
            }
        }
    }
}