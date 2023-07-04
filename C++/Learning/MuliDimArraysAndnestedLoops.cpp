#include <iostream>

int main() {
    int numberGrid[3][2] {  // 3 arrays with 2 elements each (3 rows, 2 columns)
            {1, 2},
            {3, 4},
            {5, 6}
        };
    
    std::cout << numberGrid[0][1] << std::endl;  // 2, from row 0 get element at index 1

    // J and I are convention for nested loops
    for (int i = 0; i < 3; i++) {  // 3 rows
        for (int j = 0; j < 2; j++) {  // 2 columns
            std::cout << numberGrid[i][j] << std::endl;  // Every loop we print the element at the current row and column
        }
    }

    return 0;
    }