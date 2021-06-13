package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E04PrintAndSum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = Integer.parseInt(scan.nextLine());
        int num2 = scan.nextInt();

        int result = 0;
        for (int i = num1; i <= num2; i++) {
            result += i;
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.printf("Sum: %d",result);
    }
}
