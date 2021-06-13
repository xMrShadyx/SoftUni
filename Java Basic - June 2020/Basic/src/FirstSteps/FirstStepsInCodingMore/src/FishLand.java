package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class FishLand {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double priceSkumria = Double.parseDouble(scan.nextLine());
        double priceCaca = Double.parseDouble(scan.nextLine());

        double kgPalamud = Double.parseDouble(scan.nextLine());
        double kgSafrid = Double.parseDouble(scan.nextLine());
        int kgMidi = Integer.parseInt(scan.nextLine());


        double pricePalamud = kgPalamud * (priceSkumria * 1.60);
        double priceSafrid = kgSafrid * (priceCaca * 1.80);
        double priceMidi = kgMidi * 7.50;

        double result = priceMidi + priceSafrid + pricePalamud;
        System.out.printf("%.02f ",result);
    }
}
