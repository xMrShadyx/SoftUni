import java.util.Scanner;

public class DepositCalculator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double DepositAmount = Double.parseDouble(scan.nextLine());
        int AmountMonths = Integer.parseInt(scan.nextLine());
        double YearlyBonus = Double.parseDouble(scan.nextLine());

        double firstCalc = DepositAmount * YearlyBonus;
        double secondCalc = (firstCalc / 100) / 12;
        double lastCalc = DepositAmount + (AmountMonths * secondCalc);

        System.out.println(lastCalc);
    }
}
