import java.util.Scanner;

public class ConcatinateData {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.nextLine();
        String lastName = scan.nextLine();
        int age = Integer.parseInt(scan.nextLine());
        String town = scan.nextLine();

        System.out.println("You are " + firstName + " " + lastName + ", a " + age + "-years old person from " + town + ".");
    }
}
