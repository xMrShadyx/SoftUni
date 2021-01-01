using System;

namespace hotel_room_07
{
    class Program
    {
        static void Main(string[] args)
        {
            string month = Console.ReadLine();
            int amountNights = int.Parse(Console.ReadLine());

            double strudioPrice = 0.0;
            double apartmentPrice = 0.0;

            switch (month)
            {
                case "May":
                case "October":
                    strudioPrice = 50;
                    apartmentPrice = 65;
                    if (amountNights > 7 && amountNights < 14)
                    {
                        strudioPrice = strudioPrice * 0.95;
                    }
                    else if (amountNights > 14)

                    {
                        strudioPrice = strudioPrice * 0.70;
                    }
                    break;
                case "June":
                case "September":
                    strudioPrice = 75.20;
                    apartmentPrice = 68.70;
                    if (amountNights > 14)
                    {
                        strudioPrice = strudioPrice * 0.80;
                    }
                    break;
                case "July":
                case "August":
                    strudioPrice = 76;
                    apartmentPrice = 77;
                    break;
            }

            if (amountNights > 14)
            {
                apartmentPrice = apartmentPrice * 0.90;
            }
            Console.WriteLine($"Apartment: {apartmentPrice * amountNights:F2} lv.");
            Console.WriteLine($"Studio: {strudioPrice * amountNights:F2} lv.");
            
        }
    }
}