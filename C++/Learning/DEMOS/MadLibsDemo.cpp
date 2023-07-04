#include <iostream>
#include <string>
#include <limits>

int main() {
    std::string color, pluralNoun, celebrity;

    // get int
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // ignore the rest of the input buffer

    std::cout << "Enter a color: ";
    getline(std::cin, color);
    std::cout << "Enter a plural noun: ";
    getline(std::cin, pluralNoun);
    std::cout << "Enter a celebrity: ";
    getline(std::cin, celebrity);

    // convert int to string
    std::string numberString = std::to_string(number);

    std::cout << "Roses are " << color.append(numberString) << std::endl;
    std::cout << pluralNoun << " are blue" << std::endl;
    std::cout << "I love " << celebrity << std::endl;

    // keep console window open
    std::cin.clear();               // reset any error flags
    std::cin.ignore(32767, '\n');   // ignore any characters in the input buffer until we find an enter character
    std::cin.get();                 // get one more character from the user
    return 0;
}
