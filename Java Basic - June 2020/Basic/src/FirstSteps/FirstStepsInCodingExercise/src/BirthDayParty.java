import java.util.Scanner;

public class BirthDayParty {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double Salary = Double.parseDouble(scan.nextLine());

        double CakePrice = Salary * 0.20;
        double DrinkPrice = CakePrice - (CakePrice * 0.45);
        double AnimatorPrice = Salary / 3;

        double Result = Salary + CakePrice + DrinkPrice + AnimatorPrice;
        System.out.println(Result);
    }
}
