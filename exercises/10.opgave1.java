import java.util.*;

public class opgave1 implements Runnable {
    // Grid where 'X' marks the presence of treasure and '-' indicates empty space.
    private static final char[][] grid = {
        {'-', '-', '-', 'X', '-'},
        {'-', '-', '-', '-', '-'},
        {'X', '-', '-', '-', '-'},
        {'-', '-', 'X', '-', '-'},
        {'-', '-', '-', '-', 'X'}
    };
    private final String name;  // Name of the thread or character in the simulation.

    public opgave1(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        Random random = new Random();
        int x, y;
        
        do {
            // Each thread starts at a random position in the grid.
            x = random.nextInt(grid.length);
            y = random.nextInt(grid[0].length);
        } while (grid[x][y] != 'X'); // Continue to search randomly until treasure ('X') is found.

        // Synchronizing on TreasureHuntTask.class object to ensure mutual exclusion.
        synchronized (opgave1.class) {
            if (grid[x][y] == 'X') {
                // Printing the treasure found message with coordinates and by whom.
                System.out.printf("%s found the treasure at (%d, %d)!%n", name, x, y);
                grid[x][y] = '-'; // Marking this treasure as found to prevent others from finding it.
            }
        }
    }

    public static void main(String[] args) throws InterruptedException {
        String[] names = {"Alice", "Bob", "Charlie", "Diana", "Edward"};
        List<Thread> threads = new ArrayList<>();

        // Creating and starting threads for each character.
        for (String name : names) {
            Thread thread = new Thread(new opgave1(name));
            threads.add(thread);
            thread.start();
        }

        // Waiting for all threads to complete using join.
        for (Thread thread : threads) {
            thread.join();
        }

        // After all threads have completed, printing the closing message.
        System.out.println("The treasure hunt is over!");
    }
}
