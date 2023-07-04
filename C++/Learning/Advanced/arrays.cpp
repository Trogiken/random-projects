#include <iostream>

int main() {
    int luckyNumbersUnfixed[] = {4, 8, 15, 16, 23, 42}; // Array of integers, Unfixed size

    std::cout << luckyNumbersUnfixed[3] << std::endl;  // Returns 16
    luckyNumbersUnfixed[3] = 200;                      // Change 16 to 200
    std::cout << luckyNumbersUnfixed[3] << std::endl;  // Returns 200

    std::cout << '\n' << std::endl;

    int luckyNumbersFixed[10] = {4, 8, 15, 16, 23, 42}; // Array of integers, Fixed size, first parameter is the size of the array (luckNumbers[6])
    luckyNumbersFixed[9] = 200;                        // Set index 9 to 200
    std::cout << luckyNumbersFixed[9] << std::endl;    // Returns 200
}