package Conditional.ConditionalExercise;

import java.util.Scanner;

public class GodzillaVsKong {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double MovieBudget = Double.parseDouble(scan.nextLine());
        int amountStatists = Integer.parseInt(scan.nextLine());
        double pricePerStatists = Double.parseDouble(scan.nextLine());

        double decorPrice = MovieBudget * 0.1;
        double clothingPrice = amountStatists * pricePerStatists;

        if (amountStatists > 150) {
            clothingPrice = clothingPrice * 0.9;
        }

        double someResult = decorPrice + clothingPrice;

        if (someResult <= MovieBudget) {
            System.out.printf("Action!%nWingard starts filming with %.2f leva left.", MovieBudget - someResult);
        } else {
            System.out.printf("Not enough money! %nWingard needs %.2f leva more.", someResult - MovieBudget);
        }

    }
}
