using System;

namespace min_number_07
{
    class Program
    {
        static void Main(string[] args)
        {
            string number = Console.ReadLine();
            int minValue = int.MaxValue;

            while (number != "Stop")
            {
                int currNumber = int.Parse(number);
                if (currNumber < minValue)
                {
                    minValue = currNumber;
                }

                number = Console.ReadLine();
            }

            Console.WriteLine(minValue);
        }
    }
}