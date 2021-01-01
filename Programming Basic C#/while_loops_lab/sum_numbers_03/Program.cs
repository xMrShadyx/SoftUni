using System;

namespace sum_numbers_03
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());
            int sumNum = 0;
            
            while (sumNum < number)
            {
                sumNum += int.Parse(Console.ReadLine());
            }

            Console.WriteLine(sumNum);
        }
    }
}