import java.util.Scanner;

public class ProjectsCreations {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String nameArchitect = scan.nextLine();
        int amountProjects = Integer.parseInt(scan.nextLine());

        System.out.println("The architect " + nameArchitect + " will need " + amountProjects * 3 + " hours to complete " + amountProjects + " project/s.");
    }
}
