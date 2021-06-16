package bg.softuniDataTypes.DataTypesLab;

import java.util.Scanner;

public class L05ConcatNames {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String name1 = scan.nextLine();
        String name2 = scan.nextLine();
        String delimiter = scan.nextLine();

        System.out.printf("%s%s%s", name1, delimiter, name2);
    }
}
