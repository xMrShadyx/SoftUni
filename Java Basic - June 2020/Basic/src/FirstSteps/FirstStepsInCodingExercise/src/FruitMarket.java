import java.util.Scanner;

public class FruitMarket {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double PriceStrawberry = Double.parseDouble(scan.nextLine());
        double AmountBananas = Double.parseDouble(scan.nextLine());
        double AmountOranges = Double.parseDouble(scan.nextLine());
        double AmountBerries = Double.parseDouble(scan.nextLine());
        double AmountStrawBe = Double.parseDouble(scan.nextLine());

        double BerriesPrice = PriceStrawberry / 2;
        double OrangesPrice = BerriesPrice - (0.4 * BerriesPrice);
        double BananasPrice = BerriesPrice - (0.8 * BerriesPrice);

        double Result = (AmountBerries * BerriesPrice) + (AmountOranges * OrangesPrice) + (AmountBananas * BananasPrice) + (AmountStrawBe * PriceStrawberry);

        System.out.printf("%.02f",Result);
    }
}
