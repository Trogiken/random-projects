#include <iostream>
#include <string>

void DoWhileLoopGuessingGame() {
    int secretNum = 7;
    int guess;
    int guessCount = 0;
    int guessLimit = 3;
    bool outOfGuesses = false;

    do {
        if (guessCount < guessLimit) {
            std::cout << "Enter guess: ";
            std::cin >> guess;
            guessCount++;
        } else {
            outOfGuesses = true;
        }
    } while (secretNum != guess && !outOfGuesses);

    if (outOfGuesses) {
        std::cout << "You lose!" << std::endl;
    } else {
        std::cout << "You win!" << std::endl;
    }
}

void WhileLoopGuessingGame() {
    int secretNum = 7;
    int guess;
    int guessCount = 0;
    int guessLimit = 3;
    bool outOfGuesses = false;

    while (secretNum != guess && !outOfGuesses) {
        if (guessCount < guessLimit) {
            std::cout << "Enter guess: ";
            std::cin >> guess;
            guessCount++;
        } else {
            outOfGuesses = true;
        }
    }

    if (outOfGuesses) {
        std::cout << "You lose!" << std::endl;
    } else {
        std::cout << "You win!" << std::endl;
    }
}

int main() {
    WhileLoopGuessingGame();
    DoWhileLoopGuessingGame();

    return 0;
}