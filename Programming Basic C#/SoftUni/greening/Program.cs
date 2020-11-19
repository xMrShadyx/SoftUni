using System;

namespace greening
{
    class Program
    {
        static void Main(string[] args)
        {
            double sqrtm = double.Parse(Console.ReadLine());
            double wholePlace = sqrtm * 7.61;
            double discount = wholePlace * 0.18;
            double totalPrice = wholePlace - discount;

            Console.WriteLine("The final price is: " + totalPrice + " lv.");
            Console.WriteLine("The discount is: " + discount + " lv.");
        }
    }
}
