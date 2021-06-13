package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E07VendingMachine {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();

        double totalMoney = 0;
        while (!input.equals("Start")) {
            double currentCoins = Double.parseDouble(input);
            if (currentCoins == 0.1 || currentCoins == 0.2 || currentCoins == 0.5 || currentCoins == 1 || currentCoins == 2) {
                totalMoney += currentCoins;
            } else {
                System.out.println(String.format("Cannot accept %.2f", currentCoins));
            }

            input = scan.nextLine();
        }

        input = scan.nextLine();
        while (!input.equals("End")) {
            switch (input) {
                case "Nuts":
                    if (totalMoney >= 2) {
                        totalMoney -= 2;
                        System.out.println("Purchased Nuts");
                    } else {
                        System.out.println("Sorry, not enough money ");
                    }
                    break;
                case "Water":
                    if (totalMoney >= 0.7) {
                        totalMoney -= 0.7;
                        System.out.println("Purchased Water");
                    } else {
                        System.out.println("Sorry, not enough money ");
                    }
                    break;
                case "Crisps":
                    if (totalMoney >= 1.5) {
                        totalMoney -= 1.5;
                        System.out.println("Purchased Crisps");
                    } else {
                        System.out.println("Sorry, not enough money ");
                    }
                    break;
                case "Soda":
                    if (totalMoney >= 0.8) {
                        totalMoney -= 0.8;
                        System.out.println("Purchased Soda");
                    } else {
                        System.out.println("Sorry, not enough money ");
                    }
                    break;
                case "Coke":
                    if (totalMoney >= 1.0) {
                        totalMoney -= 1.0;
                        System.out.println("Purchased Coke");
                    } else {
                        System.out.println("Sorry, not enough money ");
                    }
                    break;
                default:
                    System.out.println("Invalid product");
                    break;
            }
            input = scan.nextLine();
        }

        System.out.printf("Change: %.2f", totalMoney);

    }
}
