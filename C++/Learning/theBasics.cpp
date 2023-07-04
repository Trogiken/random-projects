#include <iostream>
#include <string>

// data types
int a = 1; // int is a whole number
float b = 1.1;  // float is less precise than double
double c = 1.11;  // double is more precise than float
char d = 'a'; // char is a single character
std::string e = "Hello World!"; // string is a collection of characters
bool f = true; // bool is a boolean value (true or false)

static int g = 2; // static variables are only accessible in the file they are declared in
const int h = 3; // const variables cannot be changed

// function prototypes
int sum(int a, int b);
void printData(const std::string& name, int age);

// create dummy function that returns the sum of two numbers
int sum(int a, int b) {
    return a + b;
}

// create dummy function with parameters but doesn't return anything
void printData(const std::string& name, const int age) {    // '&' means that the variable is passed by reference (not copied)
                                                            // Do this for large objects to avoid copying the entire object
                                                            // const is used because we don't want to change the value of the variable, good practice
    std::cout << "\nThis is a dummy function with parameters..." << std::endl;
    std::cout << "Hello " << name << ", you are " << age << " years old." << std::endl;
}

// main function
int main() {
    std::cout << "\nRunning Program...\n" << std::endl;


    // get data from user
    std::string name;
    int age;
    std::cout << "What is your name? ";
    std::getline(std::cin, name);std::cin.clear();  // use getline to get the entire line of input for first and last name, then clear the input buffer
    std::cout << "How old are you? ";
    std::cin >> age;

    // print data to console
    printData(name, age);

    std::cout << "\nSum of 5 and 6 = " << sum(5, 6) << std::endl;


    std::cout << "\nProgram Complete." << std::endl;
    // keep console window open
    std::cin.clear();  // reset any error flags
    std::cin.ignore(32767, '\n');  // ignore any characters in the input buffer until we find an enter character
    std::cin.get();  // get one more character from the user

    return 0;
}