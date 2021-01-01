using System;

namespace operation_between_numbers_06
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = int.Parse(Console.ReadLine());
            int n2 = int.Parse(Console.ReadLine());
            string operand = Console.ReadLine();
            double result = 0;

            if ((n1 == 0 || n2 == 0) && (operand == "/" || operand == "%"))
            {
                Console.WriteLine($"Cannot divide {n1} by zero");
            } else if (operand == "/")
            {
                result = 1.00 * n1 / n2;
                Console.WriteLine($"{n1} / {n2} = {result:F2}");
            }else if (operand == "%")
            {
                result = n1 % n2;
                Console.WriteLine($"{n1} % {n2} = {result}");
            }

            if (operand == "+")
            {
                result = n1 + n2;
                if (result % 2 == 0)
                {
                    Console.WriteLine($"{n1} + {n2} = {result} - even");
                }
                else
                {
                    Console.WriteLine($"{n1} + {n2} = {result} - odd");
                }
                
            } else if (operand == "-")
            {
                result = n1 - n2;
                if (result % 2 == 0)
                {
                    Console.WriteLine($"{n1} - {n2} = {result} - even");
                }
                else
                {
                    Console.WriteLine($"{n1} - {n2} = {result} - odd");
                }
            } else if (operand == "*")
            {
                result = n1 * n2;
                if (result % 2 == 0)
                {
                    Console.WriteLine($"{n1} * {n2} = {result} - even");
                }
                else
                {
                    Console.WriteLine($"{n1} * {n2} = {result} - odd");
                }
            }
        }
        
    }
}