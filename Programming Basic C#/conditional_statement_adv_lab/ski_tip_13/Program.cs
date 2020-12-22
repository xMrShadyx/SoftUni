using System;

namespace ski_tip_13
{
    class Program
    {
        static void Main(string[] args)
        {
            double days = Double.Parse(Console.ReadLine());
            string apartment = Console.ReadLine();
            string mood = Console.ReadLine();

            double roomForOne = 18;
            double apartmentRoom = 25.00;
            double presidentRoom = 35.00;
            double result = 0;
            double nights = days - 1;
            double discount = 0;

            if (days < 10)
            {
                if (apartment == "apartment")
                {
                    discount = 30;
                } else if (apartment == "president apartment")
                {
                    discount = 10;
                }
            } else if (days >= 10 && days < 15)
            {
                if (apartment == "apartment")
                {
                    discount = 35;
                } else if (apartment == "president apartment")
                {
                    discount = 15;
                }
            } else if (days > 15)
            {
                if (apartment == "apartment")
                {
                    discount = 50;
                } else if (apartment == "president apartment")
                {
                    discount = 20;
                }
            }

            switch (apartment)
            {
                case "room for one person":
                    result = nights * roomForOne;
                    break;
                case "apartment":
                    if (days < 10)
                    {
                        result = nights * apartmentRoom;
                        result = result * 0.70;
                    } else if (days >= 10 && days < 15)
                    {
                        result = nights * apartmentRoom;
                        result = result * 0.65;
                    } else if (days > 15)
                    {
                        result = nights * apartmentRoom;
                        result = result * 0.50;
                    }
                    break;
                case "president apartment":
                    if (days < 10)
                    {
                        result = nights * presidentRoom;
                        result = result * 0.90;
                    } else if (days >= 10 && days < 15)
                    {
                        result = nights * presidentRoom;
                        result = result * 0.85;
                    } else if (days > 15)
                    {
                        result = nights * presidentRoom;
                        result = result * 0.80;
                    }
                    break;
            }

            switch (mood)
            {
                case "positive":
                    double curr = result * 0.25;
                    result = result + curr;
                    break;
                case "negative":
                    result = result * 0.90;
                    break;
            }
            Console.WriteLine(result.ToString("F"));
        }
    }
}