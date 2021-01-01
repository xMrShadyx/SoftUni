using System;

namespace graduation_pt2_08
{
    class Program
    {
        static void Main(string[] args)
        {
            string studentName = Console.ReadLine();
            int grade = 0;
            int badGrade = 0;
            double curnGrade = 0.0;
            
            while (grade < 12) {
                double currGrade = Double.Parse(Console.ReadLine());
                if (currGrade < 4) {
                    badGrade++;
                } else {
                    curnGrade += currGrade;
                }
                
                if (badGrade == 2) {
                    Console.WriteLine($"{studentName} has been excluded at {grade} grade");
                    break;
                }
                grade++;
            }

            if (badGrade != 2) {
                Console.WriteLine($"{studentName} graduated. Average grade: {curnGrade / grade:F2}");
            }
            
        }
    }
}