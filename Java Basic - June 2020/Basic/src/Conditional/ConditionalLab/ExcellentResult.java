package Conditional.ConditionalLab;

import java.util.Scanner;

public class ExcellentResult {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int number = Integer.parseInt(scan.nextLine());

        String result = "";
        if (number == 5 || number == 6) {
            result = "Excellent!";
        }
        System.out.println(result);
    }
}
