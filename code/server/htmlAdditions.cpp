#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string html_addition(string html, string text) {

    size_t body_pos = html.find("<body>");

    // error handling if body tag is missing, returns original html
    if (body_pos == -1) {
        return html;
    }

    // insert the text after the opening body tag
    html.insert(body_pos + 6, text);

    return html;
}

int main() {
    string htmlAdditions;
    string htmlFile;

    cout << "Enter the HTML Doc to be updated: " << endl;
    cin >> htmlFile;

    ifstream input(htmlFile);

    if (!input) {
        cout << "Error Opening File";
        return 1;
    }

    //reading file contents
    string htmlContent((istreambuf_iterator<char>(input)), istreambuf_iterator<char>());

    cout << "Enter HTML body additions: " << endl;
    cin.ignore(); 
    getline(cin, htmlAdditions);

    string updatedHtml = html_addition(htmlContent, htmlAdditions);

    ofstream doc(htmlFile);
    doc << updatedHtml;
    doc.close();

    return 0;
}
