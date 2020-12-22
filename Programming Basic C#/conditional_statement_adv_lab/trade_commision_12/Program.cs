using System;

namespace trade_commision_12
{
    class Program
    {
        static void Main(string[] args)
        {
            string town = Console.ReadLine();
            double money = Double.Parse(Console.ReadLine());
            double commision = 0.0;

            switch (town)
            {
                case "Sofia":
                    if (money >= 0 && money <= 500)
                    {
                        commision = 5;
                    } else if (money > 500 && money <= 1000)
                    {
                        commision = 7;
                    } else if (money > 1000 && money <= 10000)
                    {
                        commision = 8;
                    } else if (money > 10000)
                    {
                        commision = 12;
                    }
                    break;
                case "Varna":
                    if (money >= 0 && money <= 500)
                    {
                        commision = 4.5;
                    } else if (money > 500 && money <= 1000)
                    {
                        commision = 7.5;
                    } else if (money > 1000 && money <= 10000)
                    {
                        commision = 10;
                    } else if (money > 10000)
                    {
                        commision = 13;
                    }
                    break;
                case "Plovdiv":
                    if (money >= 0 && money <= 500)
                    {
                        commision = 5.5;
                    } else if (money > 500 && money <= 1000)
                    {
                        commision = 8;
                    } else if (money > 1000 && money <= 10000)
                    {
                        commision = 12;
                    } else if (money > 10000)
                    {
                        commision = 14.5;
                    }
                    break;
            }

            if (commision > 0)
            {
                Console.WriteLine(((commision / 100) * money).ToString("F"));
            }
            else
            {
                Console.WriteLine("error");
            }
            
        }
    }
}