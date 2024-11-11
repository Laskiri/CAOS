

class Cafeteria {
    constructor(seats) {
        this.availableSeats = seats;
    }

    async enterCafeteria(customerName) {


        
        while (this.availableSeats <= 0) {
            console.log(`${customerName} is waiting for a seat.`);
            await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for 1 second
        } 

        this.availableSeats--;
        console.log(`${customerName} has found a seat and is now eating.`);

        // Simulate eating process
        const eatingTime = Math.random() * 5000; // Random time up to 5 seconds
        await new Promise(resolve => setTimeout(resolve, eatingTime));

        console.log(`${customerName} has finished eating and is leaving the cafeteria.`);
        this.availableSeats++;
    
    }
}

// Program execution
const cafeteria = new Cafeteria(3); // Cafeteria with 3 seats
const customers = ['Lasse_glad', 'Lasse_sej', 'Lasse_med_hatten', 'Basse', 'Lasse_kan_en_masse', 'Laskiri', 'Sally'];

cafeteria.enterCafeteria(customers[0])
cafeteria.enterCafeteria(customers[1])
cafeteria.enterCafeteria(customers[2])
cafeteria.enterCafeteria(customers[3])
cafeteria.enterCafeteria(customers[4])
cafeteria.enterCafeteria(customers[5])




