#include <iostream>

// Void functions do not return a value
void sayHi(std::string name, int age); // Function prototype, Like declaring a variable without a value (Not needed if function is defined before main())

// Int, float, double specifies the return type of the function
int cube(int num) {
    int result = num * num * num;
    return result;
    // Another way to return the same value
    return num * num * num; // This will not be executed because its after the return statement
}

int main() {
    sayHi("Mike", 40);
    sayHi("Tom", 20);
    sayHi("Steve", 70);

    std::cout << cube(5) << std::endl; // Returns 125

    return 0;
}

void sayHi(std::string name, int age) { // Function definition
    std::cout << "Hello " << name << ", you are " << age << std::endl;
}