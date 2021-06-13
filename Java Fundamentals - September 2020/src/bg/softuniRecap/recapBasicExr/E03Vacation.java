package bg.softuniRecap.recapBasicExr;
import java.util.Scanner;

public class E03Vacation {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int AmountPersons = Integer.parseInt(scan.nextLine());
        String TypeofTrip = scan.nextLine();
        String DayOfWeek = scan.nextLine();


        double price = 0.0;
        switch (DayOfWeek){
            case "Friday":
                if (TypeofTrip.equals("Students")) {
                    price = 8.45;
                } else if (TypeofTrip.equals("Business")) {
                    price = 10.90;
                } else if (TypeofTrip.equals("Regular")) {
                    price = 15;
                }
                break;
            case "Saturday":
                if (TypeofTrip.equals("Students")) {
                    price = 9.80;
                } else if (TypeofTrip.equals("Business")) {
                    price = 15.60;
                } else if (TypeofTrip.equals("Regular")) {
                    price = 20;
                }
                break;
            case "Sunday":
                if (TypeofTrip.equals("Students")) {
                    price = 10.46;
                } else if (TypeofTrip.equals("Business")) {
                    price = 16;
                } else if (TypeofTrip.equals("Regular")) {
                    price = 22.50;
                }
                break;
        }

        if (TypeofTrip.equals("Students") && AmountPersons >= 30) {
            price *= 0.85;
        }
        if (TypeofTrip.equals("Business") && AmountPersons >= 100) {
            AmountPersons -= 10;
        }
        if (TypeofTrip.equals("Regular") && (AmountPersons >= 10 && AmountPersons <= 20)) {
            price *= 0.95;
        }

        double LastResult = AmountPersons * price;
        System.out.printf("Total price: %.2f", LastResult);
    }
}
