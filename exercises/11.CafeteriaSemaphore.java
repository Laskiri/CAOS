import java.util.concurrent.Semaphore;

public class CafeteriaSemaphore {

    // Semaphore representing the number of available seats in the cafeteria
    private final Semaphore availableSeats;
    
    // Constructor
    public CafeteriaSemaphore(int seats) {
        availableSeats = new Semaphore(seats);
    }
    
    // Method to simulate customer entering and sitting in the cafeteria
    public void tryToSit(String customerName) {
        try {
            System.out.println(customerName + " is trying to find a seat.");
            availableSeats.acquire();
            System.out.println(customerName + " sat down at a table.");
            // Simulate time taken for having a meal
            Thread.sleep(1000);
            System.out.println(customerName + " finished eating and left the table.");
            availableSeats.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        // Creating a cafeteria with 2 seats
        CafeteriaSemaphore cafeteria = new CafeteriaSemaphore(2);

        // Creating customers as threads
        for(int i = 1; i <= 5; i++) {
            String customerName = "Customer " + i;
            new Thread(() -> cafeteria.tryToSit(customerName)).start();
        }
    }
}
