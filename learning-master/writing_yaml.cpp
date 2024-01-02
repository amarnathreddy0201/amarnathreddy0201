//Important links
//https://pypi.org/project/rapidyaml/0.1.0.post60/
//https://pypi.org/project/rapidyaml/0.1.0.post60/#creating-a-tree
#include <fstream>
#include <iostream>
#include <ryml_std.hpp>
#include <ryml.hpp>
int main() {

    //YAML::Node config;
    std::ofstream fout("testconfig.yaml");

    ryml::Tree tree;
    ryml::NodeRef r = tree.rootref();

    // Each container node must be explicitly set (either MAP or SEQ):
    r |= ryml::MAP;

    r["foo"] = "1"; // ryml works only with strings.
    // Note that the tree will be __pointing__ at the
    // strings "foo" and "1" used here. You need
    // to make sure they have at least the same
    // lifetime as the tree.

    // does not change the tree until s is written to.
    ryml::NodeRef s = r["seq"]; // here, s is not valid()
    s |= ryml::SEQ; // now s is valid()

    s.append_child() = "bar0"; // this child is now __pointing__ at "bar0"
    s.append_child() = "bar1";
    s.append_child() = "bar2";

    fout << tree;

    fout.close();
    std::cout << " configuration done" << std::endl;
}
