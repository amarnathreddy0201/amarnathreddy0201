#include<opencv2/opencv.hpp>//OpenCV header to use VideoCapture class//
#include<iostream>
#include <string>
using namespace std;
using namespace cv;
int main() {
    Mat myImage,image1;//Declaring a matrix to load the frames//
    namedWindow("Video Player");//Declaring the video to show the video//
    VideoCapture cap(0);//Declaring an object to capture stream of frames from third camera//
    VideoCapture cap1(2);
    //if (!cap.isOpened() !cap1.) { //This section prompt an error message if no video stream is found//
    //    cout << "No video stream detected" << endl;
    //    system("pause");
    //    return-1;
    //}
    int i = 0;
    while (cap.isOpened() && cap1.isOpened()) { //Taking an everlasting loop to show the video//
        cap >> myImage;
        cap1 >> image1;
        if (!myImage.empty() && !image1.empty()) {
            imshow("Video Player", myImage);//Showing the video//
            imshow("Video ", image1);
            char c = (char)waitKey(1);//Allowing 1 milliseconds frame processing time and initiating break condition//
            if (c == 27) { //If 'Esc' is entered Save the images//
                // File Location ----> C:/Amar/black_c++/left
                cv::imwrite("C:/Amar/black_c++/left/image"+std::to_string(i)+".png", myImage);
                cv::imwrite("C:/Amar/black_c++/right/image" + std::to_string(i) + ".png", image1);
                i += 1;
            }
        }
       
    }
    cap.release();//Releasing the buffer memory//
    cap1.release();
    return 0;
}
