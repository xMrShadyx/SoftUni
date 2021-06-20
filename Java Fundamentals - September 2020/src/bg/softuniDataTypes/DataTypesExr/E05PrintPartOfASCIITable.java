package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E05PrintPartOfASCIITable {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int StartingPoint = Integer.parseInt(scan.nextLine());
        int EndingPoint = Integer.parseInt(scan.nextLine());

        for (int i = StartingPoint; i <= EndingPoint; i++) {
            System.out.print((char) i + " ");

        }
    }
}
