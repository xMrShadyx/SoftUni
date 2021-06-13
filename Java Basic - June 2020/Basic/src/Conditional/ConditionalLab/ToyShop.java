package Conditional.ConditionalLab;

import java.util.Scanner;

public class ToyShop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double TravelPrice = Double.parseDouble(scan.nextLine());
        int AmPuzzles = Integer.parseInt(scan.nextLine());
        int AmDolls = Integer.parseInt(scan.nextLine());
        int AmTeddyBears = Integer.parseInt(scan.nextLine());
        int Minions = Integer.parseInt(scan.nextLine());
        int Trucks = Integer.parseInt(scan.nextLine());

        double AmountToys = AmPuzzles + AmDolls + AmTeddyBears + Minions + Trucks;
        double TotalPrice = AmPuzzles * 2.6 + AmDolls * 3 + AmTeddyBears * 4.1 + Minions * 8.2 + Trucks * 2;


        double discount = 0.0;
        if (AmountToys >= 50) {
            discount = TotalPrice * 0.25;
        }
        TotalPrice -= discount;

        double rent = TotalPrice * 0.1;
        TotalPrice -= rent;

//        Math.abs(TotalPrice -= TravelPrice);

        if (TotalPrice >= TravelPrice) {
            System.out.printf("Yes! %.2f lv left.",Math.abs(TotalPrice - TravelPrice));
        } else {
            System.out.printf("Not enough money! %.02f lv needed.",Math.abs(TotalPrice - TravelPrice) );
        }


//        System.out.println(TotalPrice);

    }
}
