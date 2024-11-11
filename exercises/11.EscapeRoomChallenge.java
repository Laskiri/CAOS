

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

public class EscapeRoomChallenge {
    
    private final Lock doorLock = new ReentrantLock();
    private final Random rand = new Random();

    public void findKey(String playerName) {
        boolean keyFound = false;
        while (!keyFound) {
            if (doorLock.tryLock()) {
                try {
                    // Randomize the time taken to find the key
                    int timeToFindKey = rand.nextInt(2000); // Up to 2 seconds
                    System.out.println(playerName + " is searching for the key...");
                    Thread.sleep(timeToFindKey);
                    System.out.println(playerName + " found the key!");
                    keyFound = true;
                    // Simulate time taken to unlock the door
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } finally {
                    System.out.println(playerName + " unlocked the door and escaped!");
                    doorLock.unlock();
                }
            } else {
                try {
                    // If the key wasn't found, wait a bit before trying again
                    System.out.println(playerName + " is still searching for the key...");
                    Thread.sleep(rand.nextInt(500)); // Wait up to half a second
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void main(String[] args) {
        EscapeRoomChallenge escapeRoom = new EscapeRoomChallenge();

        // Creating players as threads
        Thread player1 = new Thread(() -> escapeRoom.findKey("Player 1"));
        Thread player2 = new Thread(() -> escapeRoom.findKey("Player 2"));

        // Start the escape room challenge
        player1.start();
        player2.start();
    }
}
