package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class FruitShop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String fruit = scan.nextLine();
        String dayOfWeek = scan.nextLine();
        double amount = Double.parseDouble(scan.nextLine());
        double price = 0.0;

        switch (dayOfWeek) {
            case "Monday":
            case "Tuesday":
            case "Friday":
            case "Wednesday":
            case "Thursday":
                if (fruit.equals("banana")) {
                    price = 2.5;
                } else if (fruit.equals("apple")) {
                    price = 1.2;
                } else if (fruit.equals("orange")) {
                    price = 0.85;
                } else if (fruit.equals("grapefruit")) {
                    price = 1.45;
                } else if (fruit.equals("kiwi")) {
                    price = 2.7;
                } else if (fruit.equals("pineapple")) {
                    price = 5.50;
                } else if (fruit.equals("grapes")) {
                    price = 3.85;
                }
                break;
            case "Saturday":
            case "Sunday":
                if (fruit.equals("banana")) {
                    price = 2.7;
                } else if (fruit.equals("apple")) {
                    price = 1.25;
                } else if (fruit.equals("orange")) {
                    price = 0.90;
                } else if (fruit.equals("grapefruit")) {
                    price = 1.6;
                } else if (fruit.equals("kiwi")) {
                    price = 3;
                } else if (fruit.equals("pineapple")) {
                    price = 5.6;
                } else if (fruit.equals("grapes")) {
                    price = 4.2;
                }
                break;
        }

        double someResult = amount * price;
        if (price == 0) {
            System.out.println("error");
        } else {
            System.out.printf("%.2f", someResult);
        }
    }
}
