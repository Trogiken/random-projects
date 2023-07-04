#include <iostream>

int powerWithFor(int baseNum, int powNum) {
    // 2^3 = 2 * 2 * 2
    // Each time we loop, we multiply the result by the base number
    int result = 1;
    for (int i = 0; i < powNum; i++) {
        result = result * baseNum;
    }
    return result;
}

int main() {
    int nums[] = {1, 2, 5, 7, 9};
    for (int i = 0; i < 5; i++) {  // (initialization; condition; increment/decrement)
        std::cout << nums[i] << std::endl;
    }

    std::cout << "----------------" << std::endl;
    std::cout << powerWithFor(2, 3) << std::endl;

    return 0;
}