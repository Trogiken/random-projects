/*
 * File: main.cpp
 * --------------
 * This file contains the main program for the User Registration program.
 * The User Registration program allows users to register for an account
 * or login to an existing account.
 * This project demonstrates the use of classes, objects, exceptions, and file I/O.
 */

#include <iostream>
#include <string>
#include "register/register.h"

/*
    * Function: AskLoginorRegister
    * Usage: std::string loginOrRegister = AskLoginorRegister();
    * ----------------------------------------------------------
    * Asks the user if they would like to login or register.
    * Returns "login" or "register".
*/
std::string AskLoginorRegister() {
    std::string loginOrRegister = "";
    std::cout << "Would you like to login or register?" << std::endl;
    std::cout << "1. Login" << std::endl;
    std::cout << "2. Register" << std::endl;
    std::cout << "Enter 1 or 2: ";
    std::cin >> loginOrRegister;
    std::cout << std::endl;

    while (loginOrRegister != "1" && loginOrRegister != "2") {
        std::cout << "Invalid input. Please enter 1 or 2: ";
        std::cin >> loginOrRegister;
        std::cout << std::endl;
    }

    return loginOrRegister;
}

/*
    * Function: RegisterUser
    * Usage: Register user = RegisterUser();
    * ---------------------------------------
    * Asks the user for their username, password, email, and phone number.
    * Returns a Register object.
*/
Register RegisterUser() {
    std::string username;
    std::string password;
    std::string email;
    std::string phoneNumber;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << std::endl;

    std::cout << "Enter password: ";
    std::cin >> password;
    std::cout << std::endl;

    std::cout << "Enter email: ";
    std::cin >> email;
    std::cout << std::endl;

    std::cout << "Enter phone number: ";
    std::cin >> phoneNumber;
    std::cout << std::endl;

    try {
        return Register(username, password, email, phoneNumber);
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
        return Register();
    }
}

int main() {
   Register user;

    if (AskLoginorRegister() == "login") {
        // login
    } else {
        // register
        user = RegisterUser();
    }

    // if user object is default-constructed
    if (user.getUsername() == "") {
        std::cout << "User not registered" << std::endl;
    } else {
        std::cout << "Username: " << user.getUsername() << std::endl;
        std::cout << "Password: " << user.getPassword() << std::endl;
        std::cout << "Email: " << user.getEmail() << std::endl;
        std::cout << "Phone number: " << user.getPhoneNumber() << std::endl;
    }

    // If login, ask for username and password
    // If username and password match, say "Welcome, <username>"
    // If username and password don't match, say "Incorrect username or password"

    // If register, ask for username, password, and email
    
    // If username already exists, say "Username already exists"
    // If username doesn't exist, create a new user and say "User created"

    // Save user data to a file

    // If user wants to exit, say "Goodbye" and exit the program

    // keep window open
    std::cout.clear();
    std::cin.ignore();
    std::cin.get();
    return 0;
}