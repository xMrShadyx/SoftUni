package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class SmallShop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String product = scan.nextLine();
        String town = scan.nextLine();
        double amount = Double.parseDouble(scan.nextLine());
        double price = 0.0;

        switch (town) {
            case "Sofia":
                if (product.equals("coffee")) {
                    price = 0.5;
                } else if (product.equals("water")) {
                    price = 0.8;
                } else if (product.equals("beer")) {
                    price = 1.2;
                } else if (product.equals("sweets")) {
                    price = 1.45;
                } else if (product.equals("peanuts")) {
                    price = 1.60;
                }
                break;
            case "Plovdiv":
                if (product.equals("coffee")) {
                    price = 0.4;
                } else if (product.equals("water")) {
                    price = 0.7;
                } else if (product.equals("beer")) {
                    price = 1.15;
                } else if (product.equals("sweets")) {
                    price = 1.30;
                } else if (product.equals("peanuts")) {
                    price = 1.50;
                }
                break;
            case "Varna":
                if (product.equals("coffee")) {
                    price = 0.45;
                } else if (product.equals("water")) {
                    price = 0.70;
                } else if (product.equals("beer")) {
                    price = 1.10;
                } else if (product.equals("sweets")) {
                    price = 1.35;
                } else if (product.equals("peanuts")) {
                    price = 1.55;
                }
                break;
        }

        System.out.println(price * amount);
    }
}
