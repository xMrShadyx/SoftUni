using System;

namespace zoo
{
    class Program
    {
        static void Main(string[] args)
        {
            int dogs = int.Parse(Console.ReadLine());
            int other = int.Parse(Console.ReadLine());

            double dogFood = dogs * 2.50;
            double otherFood = other * 4;

            Console.WriteLine(dogFood + otherFood + " lv.");
        }
    }
}
