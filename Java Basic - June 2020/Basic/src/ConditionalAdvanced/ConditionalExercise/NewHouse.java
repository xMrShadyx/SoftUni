package ConditionalAdvanced.ConditionalExercise;
import java.util.Scanner;

public class NewHouse {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String typeFlower = scan.nextLine();
        int amountFlower = scan.nextInt();
        int budget = scan.nextInt();

        double pricePerFlower = 0.0;

        switch (typeFlower) {
            case "Roses":
                pricePerFlower = 5.00;
                break;
            case "Dahlias":
                pricePerFlower = 3.80;
                break;
            case "Tulips":
                pricePerFlower = 2.80;
                break;
            case "Narcissus":
                pricePerFlower = 3.00;
                break;
            case "Gladiolus":
                pricePerFlower = 2.50;
                break;
        }

        double finalPrice = amountFlower * pricePerFlower;

        if (typeFlower.equals("Roses") && amountFlower > 80) {
            finalPrice *= 0.90;
        }
        if (typeFlower.equals("Dahlias") && amountFlower > 90) {
            finalPrice *= 0.85;
        }
        if (typeFlower.equals("Tulips") && amountFlower > 80) {
            finalPrice *= 0.85;
        }
        if (typeFlower.equals("Narcissus") && amountFlower < 120) {
            finalPrice *= 1.15;
        }
        if (typeFlower.equals("Gladiolus") && amountFlower < 80) {
            finalPrice *= 1.2;
        }

        if (finalPrice > budget) {
            System.out.printf("Not enough money, you need %.2f leva more.", finalPrice - budget);
        } else {
            System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left.", amountFlower, typeFlower, budget - finalPrice);

        }
    }
}
