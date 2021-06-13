package Conditional.ConditionalMore;

import java.util.Scanner;

public class PipesInPool {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int V = Integer.parseInt(scan.nextLine());
        int P1 = Integer.parseInt(scan.nextLine());
        int P2 = Integer.parseInt(scan.nextLine());
        double H = Double.parseDouble(scan.nextLine());


        double PipeOne = P1 * H;
        double PipeTwo = P2 * H;
        double SumOfTwoP = PipeOne + PipeTwo;

        double Fresult = (SumOfTwoP / V) * 100;
        double Sresult = (PipeOne / SumOfTwoP) * 100;
        double Tresult = (PipeTwo / SumOfTwoP) * 100;

        if (SumOfTwoP > V) {
            System.out.printf("For %.1f hours the pool overflows with %.2f liters.", H, SumOfTwoP - V);
        } else {
            System.out.printf("The pool is %.2f%% full. Pipe 1: %.2f%%. Pipe 2: %.2f%%.", Fresult,Sresult,Tresult);

        }

    }

}
