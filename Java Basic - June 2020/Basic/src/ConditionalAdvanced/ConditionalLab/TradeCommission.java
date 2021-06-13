package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class TradeCommission {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String town = scan.nextLine();
        double price = Double.parseDouble(scan.nextLine());
        double commission = 0.0;

        switch (town) {
            case "Sofia":
                if (price >= 0 && price <= 500) {
                    commission = price * 0.05;
                } else if (price > 500 && price <= 1000) {
                    commission = price * 0.07;
                } else if (price > 1000 && price <= 10000) {
                    commission = price * 0.08;
                } else if (price > 10000) {
                    commission = price * 0.12;
                } else {
                    commission = 0;
                }
                break;
            case "Varna":
                if (price >= 0 && price <= 500) {
                    commission = price * 0.045;
                } else if (price > 500 && price <= 1000) {
                    commission = price * 0.075;
                } else if (price > 1000 && price <= 10000) {
                    commission = price * 0.1;
                } else if (price > 10000) {
                    commission = price * 0.13;
                } else {
                    commission = 0;
                }
                break;
            case "Plovdiv":
                if (price >= 0 && price <= 500) {
                    commission = price * 0.055;
                } else if (price > 500 && price <= 1000) {
                    commission = price * 0.08;
                } else if (price > 1000 && price <= 10000) {
                    commission = price * 0.12;
                } else if (price > 10000) {
                    commission = price * 0.145;
                } else {
                    commission = 0;
                }
                break;
        }

        if (commission != 0) {
            System.out.printf("%.2f", commission);
        } else {
            System.out.println("error");
        }

    }
}
