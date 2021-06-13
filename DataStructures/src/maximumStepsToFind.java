public class maximumStepsToFind {
    public static void main(String[] args) {
        System.out.println(getOperationsCount(5000));
    }

    public static long getOperationsCount(int n) {
        long counter = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                counter++;
            }
        }
        return counter;
    }
}
