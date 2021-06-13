package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E09PadawanEquipment {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double amountOfMoney = Double.parseDouble(scan.nextLine());
        int countOfStudents = Integer.parseInt(scan.nextLine());

        double priceOfLightSabers = Double.parseDouble(scan.nextLine());
        double priceOfRobes = Double.parseDouble(scan.nextLine());
        double priceOfBelts = Double.parseDouble(scan.nextLine());

        int freeBelts = 0;
        for (int i = 1; i <= countOfStudents ; i++) {
            if (i % 6 == 0) {
                freeBelts++;
            }
        }
        double neededEquipment = (priceOfLightSabers * Math.ceil(countOfStudents * 1.1)) + (priceOfRobes * (countOfStudents)) + (priceOfBelts * (countOfStudents - freeBelts));

        if (neededEquipment > amountOfMoney) {
            System.out.printf("George Lucas will need %.2flv more.", neededEquipment - amountOfMoney);
        } else {
            System.out.printf("The money is enough - it would cost %.2flv.", neededEquipment);
        }
    }
}
