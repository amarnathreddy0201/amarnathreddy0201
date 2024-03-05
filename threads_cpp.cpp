// Online C++ compiler to run C++ program online
#include <iostream>
#include <thread>
#include <queue>

using namespace std;

queue<int> myQueue;


std::thread main1;
std::thread second ;
void add(){
    
    
    main1 = std::thread([&](){
        // main([&]()
        int i=0;
        while (true){
             myQueue.push(i);
             i++;
             std::cout << i << std::endl;
             if (i==100){
                 i=0;
                 break;
             }
        }
    });
    
    main1.join();
}

void subtract(){
    
    second = std::thread([&](){
        while(true){
            int element = myQueue.front();
            std::cout << element << std::endl;
            myQueue.pop();
        }
    });
    second.join();
}



int main() {
    // Write C++ code here
    std::cout << "Try programiz.pro"<< std::endl;
    add();
    subtract();
    
    
    

    return 0;
}
