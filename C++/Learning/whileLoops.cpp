#include <iostream>

// The while loop will execute while the condition is true
void whileLoop() {
    int index = 1;
    while (index <= 5) {
        std::cout << index << std::endl;
        index++;
    }
}

// The do while loop will always execute at least once, executes code first then checks the condition
void doWhileLoop() {
    int index = 6;
    do {
        std::cout << index << std::endl;
        index++;
    } while (index <= 5);
}

int main() {
    whileLoop();
    doWhileLoop();

    return 0;
}