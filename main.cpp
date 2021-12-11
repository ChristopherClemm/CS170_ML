#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_set>
#include <iterator>
#include <limits>
#include <math.h>
//github was not allowing me to push changes incrementally always pop "fatal: the remote hung up unexpectedly "
//can show local changes with git commits if  requested

using namespace std;
vector<vector<double>> readinFile();
void forward();
void printCurrSet(unordered_set<int>);
double accuracy(vector<vector<double>>, unordered_set<int>, int);
void backward();
int main() {

  //cout << "Hello" << endl;
  cout<< "forawrd(1) or backwards(2)" << endl;
  int resp;
  cin >> resp;
  if (resp == 1)
  {
    forward();
  }
  else
  {
    backward();
  }
  //forward();
  //backward();
  return 0;
}

void backward()
{
  //
  unordered_set<int> mySet;
  double bestOverallAcc = 0.0;
  unordered_set<int> bestSet;
  vector<vector<double>>data = readinFile();
  //cout << "size = "<< data[0].size() << endl;
  //load up set with all features
  for( int i = 1; i < data[0].size(); i++)
  {
    mySet.insert(i);
  }
//loop through the amount of features
  for(int i = 1; i < data[0].size(); i++)
  {
    cout << "On the level: " << i << " of the search tree" << endl;
    int feature_to_remove_this_level = 0;
    double best_acc_so_far = 0.0;
    //loop through remaining features
    for(int j = 1; j < data[0].size(); j++)
    {
      if (mySet.count(j))
      {
        cout << "Considering taking out " << j << " feature "<< endl;
        //get accuracy by removing a feature temporarily
        double acc = accuracy(data, mySet, -j);
        //cout << "acc at this level: " << acc << endl;
        //compare acc to the best acc so far
        if( acc > best_acc_so_far)
        {
          best_acc_so_far = acc;
          feature_to_remove_this_level = j;
        }

      }

    }
    cout << "Accuracy = " << best_acc_so_far << endl;
    //remove the feature
    mySet.erase(feature_to_remove_this_level);
    cout << "On level " << i << " I took out " << feature_to_remove_this_level << " to the current set " << endl;
    printCurrSet(mySet);
    //if it is so far the best then update
    if(best_acc_so_far > bestOverallAcc)
    {
      bestSet = mySet;
      bestOverallAcc = best_acc_so_far;
    }

  }
  cout << "The best accuracy was " << bestOverallAcc << endl;
  cout << "The best set was ";
  printCurrSet(bestSet);

}
void forward()
{
  unordered_set<int> mySet;
  double bestOverallAcc = 0.0;
  unordered_set<int> bestSet;
  vector<vector<double>>data = readinFile();
  cout << "size = "<< data[0].size() << endl;
  //loop through all features
  for(int i = 1; i < data[0].size(); i++)
  {
    cout << "On the level: " << i << " of the search tree" << endl;
    int feature_to_add_this_level = 0;
    double best_acc_so_far = 0.0;
    //loop through remaining features
    for(int j = 1; j < data[0].size(); j++)
    {
      if (!mySet.count(j))
      {
        cout << "Considering adding " << j << " feature "<< endl;
        //get acc when feature temporarily added
        double acc = accuracy(data, mySet, j);
        if( acc > best_acc_so_far)
        {
          best_acc_so_far = acc;
          feature_to_add_this_level = j;
        }

      }

    }
    //insert the best feature found to curr set
    cout << "Accuracy = " << best_acc_so_far << endl;
    mySet.insert(feature_to_add_this_level);
    cout << "On level " << i << " I added " << feature_to_add_this_level << " to the current set " << endl;
    printCurrSet(mySet);
    //if it is the best acc rating then update
    if(best_acc_so_far > bestOverallAcc)
    {
      bestSet = mySet;
      bestOverallAcc = best_acc_so_far;
    }

  }
  cout << "The best accuracy was " << bestOverallAcc << endl;
  cout << "The best set was ";
  printCurrSet(bestSet);
}
//function for printing set
void printCurrSet(unordered_set<int> mySet)
{
  unordered_set<int> :: iterator itr;
  for( itr = mySet.begin(); itr != mySet.end(); itr++)
  {
    cout << *itr << " ";
  }
  cout << endl;
}
//reading in the file
vector<vector<double>> readinFile(){
  ifstream inFile;
  double value;
  string filename = "Ver_2_CS170_Fall_2021_small_data__99.txt";
  inFile.open(filename);
  //cout << "hiii";
  vector<vector<double>>data;
  string tempString = "";
  while(getline(inFile,tempString))
  {
    vector<double> tempStore;
    istringstream iss(tempString);
    for(double t; iss>> t;)
    {
      tempStore.push_back(t);
    }
    data.push_back(tempStore);

  }
  cout << data[0][0] << endl;
  //cout <<"here";
  return data;
}


double accuracy(vector<vector<double>> myData, unordered_set<int> mySet, int feature_to_add)
{
  double correct_class = 0.0;
  //if feature_to_add is negative we want to remove it from the set
  // else we want to add it to the set
  if( feature_to_add < 0)
  {

    mySet.erase(-feature_to_add);
    //cout << "erasing" <<  endl;

  }
  else
  {

    mySet.insert(feature_to_add);
  }
  //printCurrSet(mySet);
  //loop thorugh all instances
  for(int i = 0; i < myData.size(); i++)
  {
    vector<double> object_to_classify = myData[i];
    double nn_dist = numeric_limits<double>::max();
    int nn_loc = myData.size()+1;
    double smallestSum = numeric_limits<double>::max();
    //loop through to compare current instance to all other instances
    for(int j = 0; j < myData.size(); j++)
    {
      if (i != j)
      {
        double sum = 0;
        unordered_set<int> :: iterator itr;
        //gets the distance to each point
        for( itr = mySet.begin(); itr != mySet.end(); itr++)
        {
          double sub_exp = (object_to_classify[*itr] - myData[j][*itr])*(object_to_classify[*itr] - myData[j][*itr]);
          sum += sub_exp;
          //opitmizing code
          if(sum > smallestSum)
          {
            break;
          }

        }

        double dist = sqrt(sum);
        //if its the closest point then update the closest point variables
        if (dist < nn_dist)
        {
          smallestSum = sum;
          nn_dist = dist;
          nn_loc = j;
        }
      }
    }
    //if guess is correct then we add 1 to the correct_class variable
    if(object_to_classify[0] == myData[nn_loc][0])
    {
      correct_class += 1.0;
    }
  }
  //this returns the number correct over the total number of instances
  return correct_class/myData.size();//acc
}
