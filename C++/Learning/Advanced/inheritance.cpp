#include <iostream>

class Chef {
    public:
        void makeChicken() {
            std::cout << "The chef makes chicken." << std::endl;
        }
        void makeSalad() {
            std::cout << "The chef makes salad." << std::endl;
        }
        void makeSpecialDish() {
            std::cout << "The chef makes bbq ribs." << std::endl;
        }
};

class ItalianChef : public Chef {   // ItalianChef inherits from Chef
    public:
        void makePasta() {
            std::cout << "The chef makes pasta." << std::endl;
        }
        void makeSpecialDish() {    // overrides the makeSpecialDish method from Chef
            std::cout << "The chef makes chicken parm." << std::endl;
        }
};

int main() {
    Chef chef;
    chef.makeChicken();
    chef.makeSpecialDish();

    std::cout << "--------------------" << std::endl;

    ItalianChef italianChef;
    italianChef.makeChicken();
    italianChef.makePasta();
    italianChef.makeSpecialDish();

    return 0;
}