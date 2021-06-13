import java.util.Scanner;

public class InchesToCm {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double number = Double.parseDouble(scan.nextLine());

        double result = number * 2.54;
        System.out.println(result);
    }
}
