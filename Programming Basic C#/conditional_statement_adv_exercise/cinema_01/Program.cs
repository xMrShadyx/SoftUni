using System;

namespace cinema_01
{
    class Program
    {
        static void Main(string[] args)
        {
            string cinemaType = Console.ReadLine();
            int rows = int.Parse((Console.ReadLine()));
            int colums = int.Parse(Console.ReadLine());
            double income = 0.0;

            if (cinemaType == "Premiere")
            {
                income = rows * colums * 12.00;
            } else if (cinemaType == "Normal")
            {
                income = rows * colums * 7.50;
            } else if (cinemaType == "Discount")
            {
                income = rows * colums * 5.00;
            }
            Console.WriteLine($"{income:F2} leva");
        }
    }
}