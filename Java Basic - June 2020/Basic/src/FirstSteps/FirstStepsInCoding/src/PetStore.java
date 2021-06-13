import java.util.Scanner;

public class PetStore {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int amountDogs = Integer.parseInt(scan.nextLine());
        int otherAnimals = Integer.parseInt(scan.nextLine());

        double result = amountDogs * 2.50 + otherAnimals * 4;

        System.out.println(result + " lv.");
    }
}
