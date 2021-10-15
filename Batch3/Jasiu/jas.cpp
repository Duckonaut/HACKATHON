#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;

float count_area(vector<vector<int>> points, int corners)
{
    float area = 0.0;
    for (int i = 0; i < corners - 1; i++)
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1];
    area += points[corners-1][0] * points[0][1] - points[0][0] * points[corners-1][1];
    area = abs(area) / 2.0;
    return area;
}

int main() {
    cout << "Enter amount of corners (no less than 3):";
    int corners;
    cin >> corners;
    if(corners < 3)
    {
        cout << "Incorrect amount of corners." << endl;
        return 0;
    }
    vector<vector<int>> points;
    bool unique_flag = true;       // check if all points are unique
    for(int i = 0; i < corners; i++)
    {
        vector<int> coords;
        int x, y;
        cin >> x >> y;
        coords.push_back(x);
        coords.push_back(y);
        if (std::find(points.begin(), points.end(), coords) != points.end())
        {
            unique_flag = false;
        }
        points.push_back(coords);
    }
    float area;
    area = count_area(points, corners);
    if (area == 0 || !unique_flag)
    {
        cout << "BLAD" << endl;
        return 0;
    }
    cout << area;
}
