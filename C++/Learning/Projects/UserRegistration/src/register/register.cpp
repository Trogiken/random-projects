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

Register::Register(std::string aUsername, std::string aPassword, std::string aEmail, std::string aPhoneNumber)
    : username(setUsername(aUsername)), password(setPassword(aPassword)), email(setEmail(aEmail)), phoneNumber(setPhoneNumber(aPhoneNumber)) {}

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

std::string Register::setUsername(std::string username) {
    if (username.length() < 5) {
        throw std::invalid_argument("Username must be at least 5 characters long");
    }
    this->username = username;
    return this->username;
}

std::string Register::setPassword(std::string password) {
    if (password.length() < 8) {
        throw std::invalid_argument("Password must be at least 8 characters long");
    }
    this->password = password;
    return this->password;
}

std::string Register::setEmail(std::string email) {
    if (email.find("@") == std::string::npos || email.find(".") == std::string::npos) {
        throw std::invalid_argument("Invalid email");
    }
    this->email = email;
    return this->email;
}

std::string Register::setPhoneNumber(std::string phoneNumber) {
    if (phoneNumber.length() != 10) {
        throw std::invalid_argument("Invalid phone number");
    }
    this->phoneNumber = phoneNumber;
    return this->phoneNumber;
}
