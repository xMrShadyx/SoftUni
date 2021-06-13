package ConditionalAdvanced.ConditionalExercise;

import java.util.Scanner;

public class FishingBoat {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int budget = Integer.parseInt(scan.nextLine());
        String season = scan.nextLine();
        int fishers = Integer.parseInt(scan.nextLine());

        double boatPrice = 0.0;

        switch (season) {
            case "Spring":
                boatPrice = 3000.0;
                break;
            case "Summer":
            case "Autumn":
                boatPrice = 4200.0;
                break;
            case "Winter":
                boatPrice = 2600.0;
                break;
        }

        if (fishers > 0 && fishers <= 6) {
            boatPrice *= 0.90;
        } else if (fishers <= 11) {
            boatPrice *= 0.85;
        } else if (fishers > 12) {
            boatPrice *= 0.75;
        }

        if (fishers % 2 == 0 && (!season.equals("Autumn"))) {
            boatPrice *= 0.95;
        }

        if (budget < boatPrice) {
            System.out.printf("Not enough money! You need %.2f leva.", boatPrice- budget);
        } else {
            System.out.printf("Yes! You have %.2f leva left.", budget - boatPrice);
        }
    }
}
