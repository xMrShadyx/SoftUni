using System;

namespace password_02
{
    class Program
    {
        static void Main(string[] args)
        {
            string usrName = Console.ReadLine();
            string usrPws = Console.ReadLine();

            string pwsPws = Console.ReadLine();

            while (pwsPws != usrPws)
            {
                pwsPws = Console.ReadLine();
            }

            Console.WriteLine($"Welcome {usrName}!");
        }
    }
}