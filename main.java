import java.util.Scanner;
class ElectricityBill {
    int consumerNo;
    String consumerName;
    int previousReading;
    int currentReading;
    String connectionType;
    int units;
    double billAmount;
    void inputData() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Consumer Number: ");
        consumerNo = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Consumer Name: ");
        consumerName = sc.nextLine();
        System.out.print("Enter Previous Month Reading: ");
        previousReading = sc.nextInt();
        System.out.print("Enter Current Month Reading: ");
        currentReading = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Connection Type (Domestic/Commercial): ");
        connectionType = sc.nextLine();
        units = currentReading - previousReading;
    }
    void calculateBill() {
        if (connectionType.equalsIgnoreCase("Domestic")) {
            if (units <= 100) {
                billAmount = units * 1;
            }
            else if (units <= 200) {
                billAmount = (100 * 1) + ((units - 100) * 2.5);
            }
            else if (units <= 500) {
                billAmount = (100 * 1) + (100 * 2.5)
                           + ((units - 200) * 4);
            }
            else {
                billAmount = (100 * 1) + (100 * 2.5)
                           + (300 * 4)
                           + ((units - 500) * 6);
            }
        }
        else {
            System.out.println("Commercial connection tariff not defined.");
        }
    }
    void displayBill() {
        System.out.println("\n------ ELECTRICITY BILL ------");
        System.out.println("Consumer No      : " + consumerNo);
        System.out.println("Consumer Name    : " + consumerName);
        System.out.println("Connection Type  : " + connectionType);
        System.out.println("Units Consumed   : " + units);
        System.out.println("Bill Amount      : Rs. " + billAmount);
    }
    public static void main(String[] args) {
        ElectricityBill eb = new ElectricityBill();
        eb.inputData();
        eb.calculateBill();
        eb.displayBill();
    }
}
