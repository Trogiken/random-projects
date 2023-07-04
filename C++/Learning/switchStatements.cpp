#include <iostream>

std::string getDayOfWeek(int dayNum) {
    std::string dayName;

    switch (dayNum) {
        case 0:
            dayName = "Sunday";
            break; // Breaks out of the switch statement, if not used it will execute the next case
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
        default:  // Like else in if statements
            dayName = "Invalid Day Number";
    }

    return dayName;
}

int main() {
    std::cout << getDayOfWeek(0) << std::endl;
    std::cout << getDayOfWeek(4) << std::endl;
    std::cout << getDayOfWeek(7) << std::endl;

    return 0;
}