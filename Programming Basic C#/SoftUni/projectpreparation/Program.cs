using System;

namespace projectpreparation
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int projects = int.Parse(Console.ReadLine());

            string result = $"The architect {name} will need {projects * 3} hours to complete {projects} project/s.";
            Console.WriteLine(result);
        }
    }
}
