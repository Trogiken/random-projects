#ifndef REGISTRATION_H
#define REGISTRATION_H

#include <string>

class Register {
    private:
        std::string username;
        std::string password;
        std::string email;
        std::string phoneNumber;

    public:
        Register();
        Register(std::string aUsername, std::string aPassword, std::string aEmail, std::string aPhoneNumber);
        
        std::string getUsername();
        std::string getPassword();
        std::string getEmail();
        std::string getPhoneNumber();

    private:
        std::string setUsername(std::string username);
        std::string setPassword(std::string password);
        std::string setEmail(std::string email);
        std::string setPhoneNumber(std::string phoneNumber);
};

#endif  // REGISTRATION_H
