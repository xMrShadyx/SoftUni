import java.util.Scanner;

public class CharityCampaing {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int Days = Integer.parseInt(scan.nextLine());
        int Cookers = Integer.parseInt(scan.nextLine());
        int AmountCakes = Integer.parseInt(scan.nextLine());
        int AmountWaffles = Integer.parseInt(scan.nextLine());
        int AmountPancakes = Integer.parseInt(scan.nextLine());

        double Cakes = AmountCakes * 45;
        double waffles = AmountWaffles * 5.80;
        double pancakes = AmountPancakes * 3.2;

        double ResultForOne = (Cakes + waffles + pancakes) * Cookers;
        double BeforeExpenses = ResultForOne * Days;
        double Result = BeforeExpenses - (BeforeExpenses / 8);

        System.out.printf("%.02f",Result);
    }
}
