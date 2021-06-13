import java.util.Scanner;

public class SquareArea {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sideA = Integer.parseInt(scan.nextLine());

        int area = sideA * sideA;
        System.out.println(area);
    }
}
