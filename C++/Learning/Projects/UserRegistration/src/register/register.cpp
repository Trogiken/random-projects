/*
 * File: registration.cpp
 * ----------------------
 * This file contains the implementation of the Register class.
 * The Register class provides functionality for user registration,
 * including setting and retrieving username, password, email, and
 * phone number, as well as performing basic validation on the
 * provided values.
 */

#include <iostream>
#include <string>
#include "register.h"

Register::Register() {
    this->username = "";
    this->password = "";
    this->email = "";
    this->phoneNumber = "";
}

Register::Register(std::string aUsername, std::string aPassword, std::string aEmail, std::string aPhoneNumber) {
    this->username = setUsername(aUsername);
    this->password = setPassword(aPassword);
    this->email = setEmail(aEmail);
    this->phoneNumber = setPhoneNumber(aPhoneNumber);
}

std::string Register::getUsername() {
    return this->username;
}

std::string Register::getPassword() {
    return this->password;
}

std::string Register::getEmail() {
    return this->email;
}

std::string Register::getPhoneNumber() {
    return this->phoneNumber;
}
// DEBUG this->username = aUsername does not work because object is not yet constructed, is there a better way
std::string Register::setUsername(std::string aUsername) {
    if (aUsername.length() < 5) {
        throw std::invalid_argument("Username must be at least 5 characters long");
    }
    username = aUsername;
    return username;
}

std::string Register::setPassword(std::string aPassword) {
    if (aPassword.length() < 8) {
        throw std::invalid_argument("Password must be at least 8 characters long");
    };
    password = aPassword;
    return password;
}

std::string Register::setEmail(std::string aEmail) {
    if (aEmail.find("@") == std::string::npos || aEmail.find(".") == std::string::npos) {
        throw std::invalid_argument("Invalid email");
    }
    email = aEmail;
    return email;
}

std::string Register::setPhoneNumber(std::string aPhoneNumber) {
    if (aPhoneNumber.length() != 10) {
        throw std::invalid_argument("Invalid phone number");
    }
    phoneNumber = aPhoneNumber;
    return phoneNumber;
}
