using System;

namespace on_time_for_exam_08
{
    class Program
    {
        static void Main(string[] args)
        {
            int examHour = int.Parse(Console.ReadLine());
            int examMin = int.Parse(Console.ReadLine());
            int arrivalHour = int.Parse(Console.ReadLine());
            int arrivalMin = int.Parse((Console.ReadLine()));

            int examTotalMins = examHour * 60 + examMin;
            int arrivalTotalMins = arrivalHour * 60 + arrivalMin;

            if (examTotalMins - 30 <= arrivalTotalMins)
            {
                if (arrivalTotalMins <= examTotalMins)
                {
                    Console.WriteLine("On time");
                } 
                if (examTotalMins != arrivalHour)
                {
                    int diff = examTotalMins - arrivalTotalMins;
                    Console.WriteLine($"{diff} minutes before the start");
                }
            } else if (arrivalTotalMins < examTotalMins - 30)

            {
                Console.WriteLine("Early");
                int diff = examTotalMins - arrivalTotalMins;
                if (diff < 60 || diff > 0)
                {
                    Console.WriteLine($"{diff} minutes before the start");
                }
                else
                {
                    double diffHour = (1.00 * diff) / 60;
                    double diffMin = (1.00 * diff) % 60;
                    if (diffMin < 10)
                    {
                        Console.WriteLine($"{diffHour}:0{diffMin} hours before the start");
                    }
                    else
                    {
                        Console.WriteLine($"{diffHour}:{diffMin} hours before the start");
                    }

                }
            }
            else
            {
                Console.WriteLine("Late");
                int diff = arrivalTotalMins - examTotalMins;
                if (diff < 60 || diff > 0)
                {
                    Console.WriteLine($"{Math.Abs(diff)} minutes after the start");
                }
                else
                {
                    double diffHour = (1.00 * diff) / 60;
                    double diffMin = (1.00 * diff) % 60;
                    if (diffMin < 10)
                    {
                        Console.WriteLine($"{diffHour}:0{diffMin} hours after the start");
                    }
                    else
                    {
                        Console.WriteLine($"{diffHour}:{diffMin} hours after the start");
                    }
                }
            }

            
        }
    }
}