﻿using System;
using System.Diagnostics;

namespace cinema_ticket_08
{
    class Program
    {
        static void Main(string[] args)
        {
            string day = Console.ReadLine();

            switch (day)
            {
                case "Monday":
                case "Tuesday":
                case "Friday":
                    Console.WriteLine(12);
                    break;
                case "Wednesday":
                case "Thursday":
                    Console.WriteLine(14);
                    break;
                case "Saturday": 
                case "Sunday":
                    Console.WriteLine(16);
                    break;
            }
        }
    }
}