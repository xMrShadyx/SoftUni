using System;

namespace read_text_01
{
    class Program
    {
        static void Main(string[] args)
        {
            string command = Console.ReadLine();

            while (command != "Stop")
            {
                Console.WriteLine(command);
                command = Console.ReadLine();
            }
        }
    }
}