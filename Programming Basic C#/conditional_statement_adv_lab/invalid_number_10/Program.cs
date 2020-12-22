using System;

namespace invalid_number_10
{
    class Program
    {
        static void Main(string[] args)
        {
            double number = double.Parse(Console.ReadLine());

            switch (number)
            {
                case 0:
                    break;
                default:
                    if (number < 100)
                    {
                        Console.WriteLine("invalid");
                    } else if (number > 200)
                    {
                        Console.WriteLine("invalid");
                    }
                    break;
                    
            }
            
        }
    }
}