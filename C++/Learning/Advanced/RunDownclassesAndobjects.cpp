#include <iostream>

/*
    A class is a blueprint for creating objects
    An object is an instance of a class
    A class can contain:
    - attributes (variables)
    - methods (functions)
    - constructors
    - access modifiers (public, private, protected)

    Access modifiers:
    - public: accessible from anywhere
    - private: accessible only from within the class
    - protected: accessible from within the class and from classes derived from that class
        - a derived class is a class that inherits from another class

    Constructors:
    - a special method that is called when an object is created
    - the name of the constructor must be the same as the name of the class
    - they don't have a return type
    - they can have parameters
    - if you don't specify a constructor, C++ will automatically create one for you

    Destructors:
    - a special method that is called when an object is deleted
    - the name of the destructor must be the same as the name of the class, preceded by a tilde (~)
    - they don't have parameters
    - they don't have a return type

    Methods:
    - functions that belong to a class
    - they can be defined inside or outside the class
    - they can be defined in the class declaration or in the class definition

    Accessing attributes and methods:
    - use the dot operator (.) to access attributes and methods of an object
    - use the arrow operator (->) to access attributes and methods of a pointer to an object

    Vocabulary:
    Encapsulation: the process of combining data and functions into a single unit called class
    Abstraction: the process of hiding the implementation details from the user, only the functionality will be provided to the user
    Inheritance: the process of creating new classes from existing classes
    Polymorphism: the ability to perform a single action in different ways
*/


class Book {
    public:
        std::string title;
        std::string author;
        int pages = 0;  // default value

        // Constructor
        Book() {
            std::cout << "Creating object..." << std::endl;
        }

        // Destructor
        ~Book() {
            std::cout << "Deleting object..." << std::endl;
        }

        // Methods:
        bool isLongBook() {
            if (pages >= 500) {
                return true;
            }
            return false;
        }

        // Getters and setters
        void setPages(int pages) {
            if (pages >= 0) {
                this->pages = pages; // this->pages refers to the pages attribute of the object
            }
        }
        int getPages() {
            return this->pages;
        }

        // Constant attributes and methods
        const int MAX_PAGES = 1000;
        void printMaxPages() {
            std::cout << "Max pages: " << MAX_PAGES << std::endl;
        }

        // Example Friend functions
        // - a friend function can access private and protected members of a class
        // friend void printBookInfo(Book book);
        // friend class Library;
};

// Book with constructor
class BookConstructor {
    public:
        // can provide values
        std::string title;
        std::string author;
        int pages;  

        BookConstructor() {  // default constructor
            title = "no title";
            author = "no author";
            pages = 0;
        }

        BookConstructor(std::string title, std::string author, int pages) : title(title), author(author), pages(pages) {  // parameterized constructor, opt 1
        }
        // BookConstructor(std::string title, std::string author, int pages) {  // parameterized constructor, opt 2
        //     this->title = title;
        //     this->author = author;
        //     this->pages = pages;
        // }

};


int main() {
    // Book without constructor used
    Book book1;
    book1.title = "Harry Potter";
    book1.author = "JK Rowling";
    book1.pages = 500;

    Book book2;
    book2.title = "Lord of the Rings";
    book2.author = "Tolkien";

    std::cout << book1.title << std::endl;
    std::cout << book2.pages << std::endl;  // will print 0 because we didn't assign a value to it

    std::cout << book1.isLongBook() << std::endl;
    std::cout << book2.isLongBook() << std::endl;

    book1.setPages(1000);
    std::cout << book1.getPages() << std::endl;

    book1.printMaxPages();

    std:: cout << "--------------------" << std::endl;
    // Book with constructor used
    BookConstructor book3("The Hobbit", "Tolkien", 300); // using parameterized constructor
    std::cout << book3.title << std::endl;

    BookConstructor book4; // using default constructor
    std::cout << book4.title << std::endl;

    std:: cout << "--------------------" << std::endl;

    return 0;
}