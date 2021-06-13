package Conditional.ConditionalMore;

import java.util.Locale;
import java.util.Scanner;

public class FuelTank {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String type = scan.nextLine();
        int amount = Integer.parseInt(scan.nextLine());

        if (type.equals("Diesel") || type.equals("Gasoline") || type.equals("Gas")) {
            if (amount < 25) {
                System.out.printf("Fill your tank with %s!", type.toLowerCase());
            } else {
                System.out.printf("You have enough %s.", type.toLowerCase());
            }
        } else {
            System.out.println("Invalid fuel!");
        }
    }
}
