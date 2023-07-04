#include <iostream>
#include <cmath>

// Basic Math
void basicMath() {
    std::cout << 5 + 5 << std::endl;        // Returns 10
    std::cout << 5 - 5 << std::endl;        // Returns 0
    std::cout << 5 * 5 << std::endl;        // Returns 25
    std::cout << 5 / 5 << std::endl;        // Returns 1
    std::cout << 5 % 5 << std::endl;        // Returns 0 (5 / 5 = 1, remainder 0)
}

// Order of Operations
void orderOfOperations() {
    std::cout << 5 + 5 * 5 << std::endl;    // Returns 30 (5 * 5 = 25, 25 + 5 = 30)
    std::cout << (5 + 5) * 5 << std::endl;  // Returns 50 (5 + 5 = 10, 10 * 5 = 50)
}

// Increment and Decrement
void incrementDecrement() {
    int i = 5;
    std::cout << i++ << std::endl;          // Returns 5, then increments i to 6
    std::cout << ++i << std::endl;          // Increments i to 7, then returns 7
    std::cout << i-- << std::endl;          // Returns 7, then decrements i to 6
    std::cout << --i << std::endl;          // Decrements i to 5, then returns 5
}

// Compound Assignment
void compoundAssignment() {
    int x = 5;
    x += 5;                                 // x = x + 5
    std::cout << x << std::endl;            // Returns 10
    x -= 5;                                 // x = x - 5
    std::cout << x << std::endl;            // Returns 5
    x *= 5;                                 // x = x * 5
    std::cout << x << std::endl;            // Returns 25
    x /= 5;                                 // x = x / 5
    std::cout << x << std::endl;            // Returns 5
    x %= 5;                                 // x = x % 5
    std::cout << x << std::endl;            // Returns 0
}

// Comparison
void comparison() {
    std::cout << (5 == 5) << std::endl;     // Returns 1 (true)
    std::cout << (5 != 5) << std::endl;     // Returns 0 (false)
    std::cout << (5 > 5) << std::endl;      // Returns 0 (false)
    std::cout << (5 < 5) << std::endl;      // Returns 0 (false)
    std::cout << (5 >= 5) << std::endl;     // Returns 1 (true)
    std::cout << (5 <= 5) << std::endl;     // Returns 1 (true)
}

// Logical
void logical() {
    std::cout << (true && true) << std::endl;   // Returns 1 (true) (both must be true)
    std::cout << (true || false) << std::endl;  // Returns 1 (true) (one must be true)
    std::cout << (!true) << std::endl;          // Returns 0 (false) (inverts true to false, like a NOT gate)
}

// cmath (requires #include <cmath>)
void cmath() {
    std::cout << sqrt(25) << std::endl;         // Returns 5 (square root)
    std::cout << round(2.6) << std::endl;       // Returns 3 (rounds to nearest integer)
    std::cout << ceil(2.1) << std::endl;        // Returns 3 (returns the next highest integer)
    std::cout << floor(2.9) << std::endl;       // Returns 2 (returns the next lowest integer)
    std::cout << fmax(2, 5) << std::endl;       // Returns 5 (larger number)
    std::cout << fmin(2, 5) << std::endl;       // Returns 2 (smaller number)
    std::cout << pow(2, 5) << std::endl;        // Returns 32 (2^5)
}

// Trigonometry
void trigonometry() {
    std::cout << sin(90) << std::endl;          // Returns 0.893997
    std::cout << cos(0) << std::endl;           // Returns 1
    std::cout << tan(45) << std::endl;          // Returns 1.61978
    std::cout << asin(0.893997) << std::endl;   // Returns 1.5708
    std::cout << acos(1) << std::endl;          // Returns 0
    std::cout << atan(1.61978) << std::endl;    // Returns 0.982794
}

// Bitwise
void bitwise() {
    std::cout << (5 & 5) << std::endl;      // Returns 5 (AND)
    std::cout << (5 | 5) << std::endl;      // Returns 5 (OR)
    std::cout << (5 ^ 5) << std::endl;      // Returns 0 (XOR)
    std::cout << (~5) << std::endl;         // Returns -6 (NOT)
    std::cout << (5 << 5) << std::endl;     // Returns 160 (left shift)
    std::cout << (5 >> 5) << std::endl;     // Returns 0 (right shift)
}

int main() {
    // Call each function

    std::cout << "\nBasic Math:" << std::endl;
    basicMath();
    std::cout << "\nOrder of Operations:" << std::endl;
    orderOfOperations();
    std::cout << "\nIncrement and Decrement:" << std::endl;
    incrementDecrement();
    std::cout << "\nCompound Assignment:" << std::endl;
    compoundAssignment();
    std::cout << "\nComparison:" << std::endl;
    comparison();
    std::cout << "\nLogical:" << std::endl;
    logical();
    std::cout << "\ncmath:" << std::endl;
    cmath();
    std::cout << "\nTrigonometry:" << std::endl;
    trigonometry();
    std::cout << "\nBitwise:" << std::endl;
    bitwise();

    // keep console window open
    std::cin.clear();               // reset any error flags
    std::cin.ignore(32767, '\n');   // ignore any characters in the input buffer until we find an enter character
    std::cin.get();                 // get one more character from the user

    return 0;
}
