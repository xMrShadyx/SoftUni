using System;

namespace small_shop_05
{
    class Program
    {
        static void Main(string[] args)
        {
            string article = Console.ReadLine();
            string town = Console.ReadLine();
            double amount = double.Parse(Console.ReadLine());
            double price = 0;

            switch (town)
            {
                case "Sofia":
                    switch (article)
                    {
                        case "coffee":
                            price = 0.5;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "water":
                            price = 0.8;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "beer":
                            price = 1.2;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "sweets":
                            price = 1.45;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "peanuts":
                            price = 1.6;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                    }
                    break;
                case "Plovdiv":
                    switch (article)
                    {
                        case "coffee":
                            price = 0.4;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "water":
                            price = 0.7;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "beer":
                            price = 1.15;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "sweets":
                            price = 1.30;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "peanuts":
                            price = 1.5;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                    }
                    break;
                case "Varna":
                    switch (article)
                    {
                        case "coffee":
                            price = 0.45;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "water":
                            price = 0.70;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "beer":
                            price = 1.10;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "sweets":
                            price = 1.35;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                        case "peanuts":
                            price = 1.55;
                            Console.WriteLine("{0:0.00}", price * amount);
                            break;
                    }
                    break;
            }
            
            
        }
    }
}