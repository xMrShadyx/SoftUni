import java.util.Scanner;

public class VacationBookList {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int AmountPages = Integer.parseInt(scan.nextLine());
        int Pages = Integer.parseInt(scan.nextLine());
        int AmountDays = Integer.parseInt(scan.nextLine());

        int ReadingTime = AmountPages / Pages;
        int hoursPerDay = ReadingTime / AmountDays;

        System.out.println(hoursPerDay);
    }
}
