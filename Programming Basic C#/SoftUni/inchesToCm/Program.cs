using System;

namespace inchesToCm
{
    class Program
    {
        static void Main(string[] args)
        {
            double inches = 2.54;
            double number = double.Parse(Console.ReadLine());

            double area = number * inches;
            Console.WriteLine(area);
        }
    }
}
