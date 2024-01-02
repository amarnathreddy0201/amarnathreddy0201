#include <iostream>
#include <chrono>
int main(){
   std::chrono::time_point<std::chrono::system_clock> foo = std::chrono::system_clock::now(); 
   
   while(1){
       std::chrono::time_point<std::chrono::system_clock>now=std::chrono::system_clock::now(); 
       if(std::chrono::duration_cast<std::chrono::seconds>(now - foo).count()<5){
           
       }
       else{
           printf("GO A head");
       }
   }
printf("Done");
}
