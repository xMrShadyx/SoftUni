using System;

namespace max_number_06
{
    class Program
    {
        static void Main(string[] args)
        {
            string number = Console.ReadLine();
            int maxNumber = int.MinValue;

            while (number != "Stop")
            {
                int currNumber = int.Parse(number);
                if (currNumber > maxNumber)
                {
                    maxNumber = currNumber;
                }

                number = Console.ReadLine();
            }

            Console.WriteLine(maxNumber);
        }
    }
}