#include <iostream>

/*
    Each variable has a memory address
    A pointer is a variable that stores the memory address of another variable
    They are just another type of data (like int, double, string, etc.)

    Pointers are useful for:
    - passing large amounts of data to functions
    - efficiently accessing data structures
    - building complicated data structures

    Use the address operator (&) to get the memory address of a variable
    Use the dereference operator (*) to get the value of the variable located at the address
    Use the dereference operator (*) to declare a pointer variable
    Example: int *pAge = &age;
    The above line declares a pointer variable called pAge that points to the memory address of the variable age
    The type of the pointer variable must match the type of the variable it is pointing to
*/

int main() {

    int age = 19;
    int *pAge = &age;  // Pointer variable that points to the memory address of the variable age

    double gpa = 3.8;
    double *pGpa = &gpa;  // Pointer variable that points to the memory address of the variable gpa

    std::string name = "Bob";
    std::string *pName = &name;  // Pointer variable that points to the memory address of the variable name

    std::cout << &age << std::endl;  // 0x61ff08
    std::cout << "-------------" << std::endl;

    std::cout << "pAge:" << std::endl;
    std::cout << pAge << std::endl;  // 0x61ff08, pointer variable
    std::cout << *pAge << std::endl;  // 19, dereference operator: get the value of the variable located at the address

    std::cout << "pGpa:" << std::endl;
    std::cout << pGpa << std::endl;  // 0x61ff00
    std::cout << *pGpa << std::endl;  // 3.8

    std::cout << "pName:" << std::endl;
    std::cout << pName << std::endl;  // 0x61fef0
    std::cout << *pName << std::endl;  // Bob

    return 0;
}