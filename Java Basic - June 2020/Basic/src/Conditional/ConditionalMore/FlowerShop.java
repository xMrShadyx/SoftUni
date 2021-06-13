package Conditional.ConditionalMore;

import java.util.Scanner;

public class FlowerShop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int amountMagnoliyi = Integer.parseInt(scan.nextLine());
        int amountZyumbyuli = Integer.parseInt(scan.nextLine());
        int amountRozi = Integer.parseInt(scan.nextLine());
        int amountCactus = Integer.parseInt(scan.nextLine());
        double giftPrice = Double.parseDouble(scan.nextLine());

        double sum = amountMagnoliyi * 3.25 + amountZyumbyuli * 4 + amountRozi * 3.50 + amountCactus * 8;
        double afterTax = sum * 0.95;

        if (afterTax < giftPrice) {
            System.out.printf("She will have to borrow %.0f leva.", Math.ceil(giftPrice - afterTax));
        } else {
            System.out.printf("She is left with %.0f leva.", Math.floor(afterTax - giftPrice));
        }
    }
}
