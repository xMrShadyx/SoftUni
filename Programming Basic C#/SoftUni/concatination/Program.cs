using System;

namespace concatination
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = Console.ReadLine();
            string secondName = Console.ReadLine();
            int age = int.Parse(Console.ReadLine());
            string town = Console.ReadLine();

            string test = $"You are {firstName} {secondName}, a {age}-years old person from {town}.";
            Console.WriteLine(test);
        }
    }
}
