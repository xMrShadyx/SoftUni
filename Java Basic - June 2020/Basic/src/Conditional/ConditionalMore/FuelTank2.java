package Conditional.ConditionalMore;

import java.util.Scanner;

public class FuelTank2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String type = scan.nextLine();
        double amount = Double.parseDouble(scan.nextLine());
        String clubCard = scan.nextLine();

        double DieselPrice = 2.33;
        double GasolinePrice = 2.22;
        double GasPrice = 0.93;

        if (clubCard.equals("Yes")) {
            DieselPrice -= 0.12;
            GasolinePrice -= 0.18;
            GasPrice -= 0.08;
        }
        double result = 0.0;
        if (type.equals("Diesel")) {
            result = DieselPrice * amount;
        } else if (type.equals("Gasoline")) {
            result = GasolinePrice * amount;
        } else if (type.equals("Gas")) {
            result = GasPrice * amount;
        }

        if (amount > 20 && amount <= 25) {
            result = result * 0.92;
        } else if (amount > 25) {
            result = result * 0.9;
        }

        System.out.printf("%.2f lv.", result);
    }
}
