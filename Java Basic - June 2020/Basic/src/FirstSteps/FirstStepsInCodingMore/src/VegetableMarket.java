package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class VegetableMarket {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double kiloVeggies = Double.parseDouble(scan.nextLine());
        double kiloFruits = Double.parseDouble(scan.nextLine());
        int totalVeggies = Integer.parseInt(scan.nextLine());
        int totalFruits = Integer.parseInt(scan.nextLine());

        double VeggiesResult = kiloVeggies * totalVeggies;
        double FruitsResult = kiloFruits * totalFruits;

        double result = (VeggiesResult + FruitsResult) / 1.94;

        System.out.printf("%.02f", result);

    }
}
