package Conditional.ConditionalMore;

import java.util.Scanner;

public class Pets {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int amountOfDays = Integer.parseInt(scan.nextLine());
        int leftFood = Integer.parseInt(scan.nextLine());
        double foodPerDayDog = Double.parseDouble(scan.nextLine());
        double foodPerDayCat = Double.parseDouble(scan.nextLine());
        double foodPerDayTut = Double.parseDouble(scan.nextLine());

        double totalEatenFood = foodPerDayCat * amountOfDays + foodPerDayDog * amountOfDays + ((foodPerDayTut * amountOfDays) / 1000);
        double leftFood1 = Math.abs(leftFood - totalEatenFood);

        if (totalEatenFood > leftFood) {
            System.out.printf("%.0f more kilos of food are needed.", Math.ceil(leftFood1));
        } else {
            System.out.printf("%.0f kilos of food left.", Math.floor(leftFood1));
        }
//        System.out.printf("");
    }
}
