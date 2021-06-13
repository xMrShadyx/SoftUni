import java.util.Scanner;

public class YardGreening {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double SquareMeters = Double.parseDouble(scan.nextLine());

        double FinalPrice = SquareMeters * 7.61;
        double DiscountPrice = FinalPrice * 0.18;

        System.out.println("The final price is: " + (FinalPrice - DiscountPrice) + " lv.");
        System.out.println("The discount is: " + DiscountPrice + " lv.");

    }
}
