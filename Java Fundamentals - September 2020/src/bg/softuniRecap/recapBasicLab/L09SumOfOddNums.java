package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L09SumOfOddNums {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int sum = 0;

        for (int i = 1; i <= num; i++)
        {
            System.out.println(2 * i -1);
            sum += 2 * i - 1;
        }
        System.out.printf("Sum: %d",sum);

        }
}
