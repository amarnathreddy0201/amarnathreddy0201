 std::string file_name = "amar.csv";
    // open for output in append mode (create a new file only if the file does not exist)
    std::ofstream file1;
    file1= std::ofstream(file_name, std::ios::app);
    file1 << "a" << "," << "b" << "\n";
    int i = 0;
    while (20 > i) {
        //if (20 > i) {
            file1 << i << "," << i+1 << "\n";
            i += 1;
        
    }
