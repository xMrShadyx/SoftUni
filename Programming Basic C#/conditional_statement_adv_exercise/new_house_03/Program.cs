using System;

namespace new_house_03
{
    class Program
    {
        static void Main(string[] args)
        {
            string flowerType = Console.ReadLine();
            int amountFlowers = int.Parse(Console.ReadLine());
            int budgedAmount = int.Parse(Console.ReadLine());
            double flowerPrice = 0.0;
            double discountPrice = 0.0;
            
            switch (flowerType)
            {
                case ("Roses"):
                    flowerPrice = 5;
                    break;
                case ("Dahlias"):
                    flowerPrice = 3.8;
                    break;
                case ("Tulips"):
                    flowerPrice = 2.8;
                    break;
                case ("Narcissus"):
                    flowerPrice = 3;
                    break;
                case ("Gladiolus"):
                    flowerPrice = 2.5;
                    break;
            }

            double currPrice = amountFlowers * flowerPrice;

            if (flowerType == "Roses" && amountFlowers > 80)
            {
                discountPrice = 0.90;
                currPrice = currPrice * discountPrice;
            } else if (flowerType == "Dahlias" && amountFlowers > 90)
            {
                discountPrice = 0.85;
                currPrice = currPrice * discountPrice;
            } else if (flowerType == "Tulips" && amountFlowers > 80)
            {
                discountPrice = 0.85;
                currPrice = currPrice * discountPrice;
            } else if (flowerType == "Narcissus" && amountFlowers < 120)
            {
                discountPrice = 0.15 * currPrice;
                currPrice = currPrice + discountPrice;
            } else if (flowerType == "Gladiolus" && amountFlowers < 80)
            {
                discountPrice = 0.20 * currPrice;
                currPrice = currPrice + discountPrice;
            }

            if (currPrice > budgedAmount)
            {
                Console.WriteLine($"Not enough money, you need {currPrice - budgedAmount:F2} leva more.");
            }
            else
            {
                Console.WriteLine($"Hey, you have a great garden with {amountFlowers} {flowerType} and {budgedAmount - currPrice:F2} leva left.");
            }
        }
    }
}