package bg.softuniDataTypes.DataTypesLab;

import java.util.Scanner;

public class L08LowerOrUpper {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String character = scan.nextLine();
        char test = character.charAt(0);

        if (test >= 65 && test <= 90) {
            System.out.println("upper-case");
        } else {
            System.out.println("lower-case");
        }
    }
}
