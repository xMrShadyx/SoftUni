package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E03Elevator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int waitingPersons = Integer.parseInt(scan.nextLine());
        int amountPerElevator = Integer.parseInt(scan.nextLine());

        int courses = (int) Math.ceil((double) waitingPersons / amountPerElevator);

        System.out.println(courses);



    }
}
