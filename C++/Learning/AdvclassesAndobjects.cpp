#include <iostream>


class student {
    public:
        std::string name;
        std::string major;
        double gpa;

        student(std::string aName, std::string aMajor, double aGpa) {
            name = aName;
            major = aMajor;
            gpa = aGpa;
        }

        bool hasHonors() {
            if (gpa >= 3.5) { // this->gpa also works and is more explicit
                return true;
            }
            return false;
        }
};


class Movie {
    private:
        std::string rating;
    public:
        std::string title;
        std::string director;

        Movie(std::string Title, std::string Director, std::string Rating) 
            : title(Title), director(Director) { // using initializer list
            setRating(Rating);

            // will also work
            // this->title = Title;
            // this->director = Director;
            // this->setRating(Rating);
        };

        // setRating method using getter and setter
        std::string setRating(std::string Rating) {
            if (Rating == "G" || Rating == "PG" || Rating == "PG-13" || Rating == "R" || Rating == "E") {
                this->rating = Rating;
            } else {
                this->rating = "NR";
            }
            return this->rating;
        }

        std::string getRating() {
            return this->rating;
        }
};


int main() {
    student student1("Jim", "Business", 2.4);
    student student2("Pam", "Art", 3.6);

    std::cout << student1.hasHonors() << std::endl;
    std::cout << student2.hasHonors() << std::endl;

    Movie avengers("The Avengers", "Joss Whedon", "PG-13");
    std::cout << avengers.getRating() << std::endl;

    return 0;
}