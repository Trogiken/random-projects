#include <iostream>
#include <string>

int main() {
    std::string name = "John";                              // Create string variable 'name' with value 'John'
    std::cout << "Name: " << name << std::endl;              // Returns 'John'

    std::cout << "Character at index 3: " << name[3] << std::endl;        // Returns 'n'
    std::cout << "Character at index 3 (using at()): " << name.at(3) << std::endl;     // Returns 'n'

    name[3] = 'Z';                                           // Change 'n' to 'Z'
    std::cout << "Modified name: " << name << std::endl;     // Returns 'JohZ'

    std::cout << "Length of name: " << name.length() << std::endl;           // Length, returns 4

    std::cout << "Substring (index 1, length 2): " << name.substr(1, 2) << std::endl;            // Returns 'oh'

    std::cout << "Find 'oh' in name: " << name.find("oh") << std::endl;              // Returns 1

    std::cout << "Erased characters (starting at index 2): " << name.erase(2, 3) << std::endl;     // Returns 'Jo'

    std::cout << "Inserted 'hn' at index 2: " << name.insert(2, "hn") << std::endl;           // Returns 'John'

    std::cout << "Appended ' Doe': " << name.append(" Doe") << std::endl;           // Returns 'John Doe'

    std::cout << "Replaced 'n D' with 'ny': " << name.replace(4, 4, "ny") << std::endl;     // Returns 'Johnny'

    std::cout << "Comparison with 'John': " << name.compare("John") << std::endl;          // Returns 0 (equal), (unequal returns -1)

    std::cout << "Is name empty? " << name.empty() << std::endl;                  // Returns false (0)

    // keep console window open
    std::cin.clear();               // reset any error flags
    std::cin.ignore(32767, '\n');   // ignore any characters in the input buffer until we find an enter character
    std::cin.get();                 // get one more character from the user

    return 0;
}
