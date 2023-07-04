#include <iostream>
#include <string>

// && = and
// || = or
// ! = not

int getMax(const int num1, const int num2) {
    int result;
    if (num1 > num2) {
        result = num1;
    } else {
        result = num2;
    }
    return result;
}

void ages() {
    std::string name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);
    int age;
    std::cout << "Enter your age: ";
    std::cin >> age;

    if (age < 13) {
        std::cout << "You are young" << std::endl;
    } else if (name == "bob" && age == 99) {
        std::cout << "You are bob" << std::endl;
    } else if (age < 18) {
        std::cout << "You are a teenager" << std::endl;
    } else {
        std::cout << "You are old" << std::endl;
    }
}

int main() {
    ages();
    std::cout << getMax(5, 9) << std::endl;

    return 0;
}