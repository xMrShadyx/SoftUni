package bg.softuniRecap.recapBasicMor;

import java.util.Scanner;

public class M01SortNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num1 = Integer.parseInt(scan.nextLine());
        int num2 = Integer.parseInt(scan.nextLine());
        int num3 = Integer.parseInt(scan.nextLine());

        if (num1 > num2 && num1 > num3){
            System.out.println(num1);
            if (num2 > num3) {
                System.out.println(num2);
                System.out.println(num3);
            } else {
                System.out.println(num3);
                System.out.println(num2);
            }
        } else if (num2 > num1 && num2 > num3) {
            System.out.println(num2);
            if (num1 > num3) {
                System.out.println(num1);
                System.out.println(num3);
            } else {
                System.out.println(num3);
                System.out.println(num1);
            }
        } else if (num3 > num1 && num3 > num2) {
            System.out.println(num3);
            if (num1 > num2) {
                System.out.println(num1);
                System.out.println(num2);
            } else {
                System.out.println(num2);
                System.out.println(num1);
            }
        }
    }
}
