package Conditional.ConditionalMore;

import java.util.Scanner;

public class Harvest {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int SizeOfFarm = Integer.parseInt(scan.nextLine());
        double GrapePerSqm = Double.parseDouble(scan.nextLine());
        int NeededWine = Integer.parseInt(scan.nextLine());
        int Workers = Integer.parseInt(scan.nextLine());

        double totalWine = SizeOfFarm * GrapePerSqm;
        double SizeForWine = (totalWine * 0.4) / 2.5;
        double ForWorkers = Math.abs(SizeForWine - NeededWine);

        if (SizeForWine < NeededWine) {
            System.out.printf("It will be a tough winter! More %.0f liters wine needed.", Math.floor(ForWorkers));
        } else {
            System.out.printf("Good harvest this year! Total wine: %.0f liters.%n", Math.floor(SizeForWine));
            System.out.printf("%.0f liters left -> %.0f liters per person.", Math.ceil(ForWorkers), Math.ceil(ForWorkers / Workers));
        }

    }
}
