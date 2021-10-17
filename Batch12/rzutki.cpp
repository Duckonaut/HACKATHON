#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

struct more_than_key
{
    inline bool operator() (const tuple<string, int>& struct1, const tuple<string, int>& struct2)
    {
        return (get<1>(struct1) > get<1>(struct2));
    }
};

int main()
{
    int n = 0;
    cin >> n;
    vector<tuple<string, int> > table;
    int temp = 0;
    int sum = 0;
    string tempname;
    for (int i = 0; i < n; ++i)
    {
        sum = 0;
        cin >> tempname;
        for (int i = 0; i < 5; ++i)
        {
            cin >> temp;
            sum += temp;
        }
        tuple<string, int> thing(tempname, sum);
        table.push_back(thing);
    }

    sort(table.begin(), table.end(), more_than_key());

    int prev_score = 0;
    int cur_score = 0;
    int iteration = 1;
    int place = 1;
    for (auto element : table)
    {
        cur_score = get<1>(element);
        if (cur_score != prev_score)
        {
            place = iteration;
        }
        cout << place << " " << get<0>(element) << " " << cur_score << endl;

        ++iteration;
        prev_score = cur_score;
    }

    // waiting for input so the console doesnt close immediately
    cin >> n;
    return 0;
}