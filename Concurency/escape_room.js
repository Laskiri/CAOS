class EscapeRoomChallenge {
    constructor() {
        this.lock = false;
    }

    findKey(playerName) {
        return new Promise((resolve) => {
            const tryToFindKey = () => {
                if (!this.lock) {
                    const searchTime = Math.random() * 10000; // Random time up to 10 seconds
                    setTimeout(() => {
                        if (!this.lock) {
                            this.lock = true;
                            console.log(`${playerName} found the key!`);
                            console.log(`${playerName} has escaped!`);
                            resolve();
                        }
                    }, searchTime);
                }
            };
            tryToFindKey();
        });
    }
}

const game = new EscapeRoomChallenge();
const player1 = game.findKey('Player 1');
const player2 = game.findKey('Player 2');

Promise.race([player1, player2]);