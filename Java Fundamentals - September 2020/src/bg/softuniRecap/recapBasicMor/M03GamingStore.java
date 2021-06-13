package bg.softuniRecap.recapBasicMor;

import java.util.Scanner;

public class M03GamingStore {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double amountMoney = Double.parseDouble(scan.nextLine());

        String gameTitle = scan.nextLine();
        double moneySpend = 0;
        while (!gameTitle.equals("Game Time")) {

            switch (gameTitle) {
                case "OutFall 4":
                case "RoverWatch Origins Edition":
                    if (amountMoney >= 39.99) {
                        System.out.printf("Bought %s%n", gameTitle);
                        amountMoney -= 39.99;
                        moneySpend += 39.99;
                    } else {
                        System.out.println("Too Expensive");
                    }
                    break;
                case "CS: OG":
                    if (amountMoney >= 15.99) {
                        System.out.printf("Bought %s%n", gameTitle);
                        amountMoney -= 15.99;
                        moneySpend += 15.99;
                    } else {
                        System.out.println("Too Expensive");
                    }
                    break;
                case "Zplinter Zell":
                    if (amountMoney >= 19.99) {
                        System.out.printf("Bought %s%n", gameTitle);
                        amountMoney -= 19.99;
                        moneySpend += 19.99;
                    } else {
                        System.out.println("Too Expensive");
                    }
                    break;
                case "Honored 2":
                    if (amountMoney >= 59.99) {
                        System.out.printf("Bought %s%n", gameTitle);
                        amountMoney -= 59.99;
                        moneySpend += 59.99;
                    } else {
                        System.out.println("Too Expensive");
                    }
                    break;
                case "RoverWatch":
                    if (amountMoney >= 29.99) {
                        System.out.printf("Bought %s%n", gameTitle);
                        amountMoney -= 29.99;
                        moneySpend += 29.99;
                    } else {
                        System.out.println("Too Expensive");
                    }
                    break;
                default:
                    System.out.println("Not Found");
                    break;
            }

            if (amountMoney < 0) {
                System.out.println("Out of money!");
                break;
            }
            gameTitle = scan.nextLine();
        }
        if (amountMoney > 0)  {
        System.out.printf("Total spent: $%.2f. Remaining: $%.2f%n", moneySpend, amountMoney);
        } else {
            System.out.println("Out of money!");
        }

    }
}
