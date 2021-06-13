import java.util.Scanner;

public class FishTank {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int Length = Integer.parseInt(scan.nextLine());
        int Width = Integer.parseInt(scan.nextLine());
        int Height = Integer.parseInt(scan.nextLine());
        double Percent = Double.parseDouble(scan.nextLine());

        double Space = (Length * Width * Height) * 0.001;
        //System.out.println(Space);
        double ThePercent = Percent * 0.01;
        //System.out.println(ThePercent);
        double Result = Space * (1 - ThePercent);

        System.out.printf("%.02f",Result);
    }
}
