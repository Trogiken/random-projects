#include <iostream>
#include <string>


int calculate(int num1, int num2, std::string op) {
    if (op == "*") {
        return num1 * num2;
    } else if (op == "/") {
        return num1 / num2;
    } else if (op == "+") {
        return num1 + num2;
    } else if (op == "-") {
        return num1 - num2;
    } else {
        return 01;
    }
}

int main() {
    int num1, num2;
    std::string op;
    const std::string valid_ops[4] = {"*", "/", "+", "-"};

    std::cout << "Enter first number: ";
    std::cin >> num1;
    std::cout << "Enter operator (*, /, +, -): ";
    std::cin >> op;
    std::cout << "Enter second number: ";
    std::cin >> num2;

    int result = calculate(num1, num2, op);
    if (result == 001) {
        std::cout << "Wrong Operator" << std::endl;
        main();
    }
    

    std::cout << calculate(num1, num2, op) << std::endl;
    
}