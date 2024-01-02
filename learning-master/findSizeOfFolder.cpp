#include <iostream>
#define _SILENCE_EXPERIMENTAL_FILESYSTEM_DEPRECATION_WARNING 1;
#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;


unsigned long long int get_directory_size(const fs::path& directory) {
    if (!fs::exists(directory)) return 0;

    if (fs::is_directory(directory)) {
        unsigned long long int ret_size = 0;
        fs::directory_iterator m_dir_itr(directory);

        for (m_dir_itr = fs::begin(m_dir_itr); m_dir_itr != fs::end(m_dir_itr); ++m_dir_itr) {
            fs::directory_entry m_dir_entry = *m_dir_itr;
            if (fs::is_regular_file(m_dir_entry.path())) {
                ret_size += fs::file_size(m_dir_entry.path());
            }
            else if (fs::is_directory(m_dir_entry.path())) {
                ret_size += get_directory_size(m_dir_entry.path());
            }
        }

        return ret_size;
    }
    else if (fs::is_regular_file(directory)) {
        return fs::file_size(directory);
    }

    return 0;
}

int main(){
  auto folder_size = get_directory_size("C:/fwdcheckerboardandyaml/poco_client");
  printf("Size of 'C:/Folder' is %d\n", folder_size);
  return 0;
}
