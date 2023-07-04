#include <iostream>
#include <string>
#include <limits>

void getNumber() {
    // space is a delimiter, so cin will only get the first word
    // use this method when getting integers, chars, etc
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;
    std::cout << "You entered " << x << std::endl;
    
    // ignore() will ignore the first 1000 characters or until it finds a newline character
    // Doing this because cin leaves the newline character in the input buffer and getline() will read it
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // ignore the rest of the input buffer
}

void getName() {
    // Use this method when getting strings
    // getline() will get the entire line, including spaces
    std::string name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);
    std::cout << "You entered " << name << std::endl;
    std::cin.clear();  // clear the input buffer to prevent getline() from getting the newline character
}

int main() {
    
    getNumber();
    getName();

    // keep console window open
    std::cin.clear();               // reset any error flags
    std::cin.ignore(32767, '\n');   // ignore any characters in the input buffer until we find an enter character
    std::cin.get();                 // get one more character from the user

    return 0;
}