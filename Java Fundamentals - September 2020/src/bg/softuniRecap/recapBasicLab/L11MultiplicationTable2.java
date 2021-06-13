package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L11MultiplicationTable2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = Integer.parseInt(scan.nextLine());
        int num2 = scan.nextInt();

        if (num2 <= 10) {
            for (int i = num2; i <= 10; i++) {
                System.out.printf("%d X %d = %d%n", num1, i, i * num1);
            }
        } else {
            System.out.printf("%d X %d = %d%n", num1, num2, num2 * num1);
        }
    }
}
