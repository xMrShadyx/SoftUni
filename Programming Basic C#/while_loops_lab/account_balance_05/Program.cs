using System;

namespace account_balance_05
{
    class Program
    {
        static void Main(string[] args)
        {
            string command = Console.ReadLine();
            double balance = 0.0;

            while (command != "NoMoreMoney")
            {
                double found = Double.Parse(command);
                if (found > 0)
                {
                    balance += found;
                    Console.WriteLine($"Increase: {found:F2}");
                }
                else
                {
                    Console.WriteLine("Invalid operation!");
                    break;
                } 
                command = Console.ReadLine();
            }

            Console.WriteLine($"Total: {balance:F2}");
        }
    }
}