#include<iostream>
using namespace std;
string array1[0],array2[0],array3[0],array4[0],array5[0];

int total=0;

void enter() {
  int choice;
  cout<<"How many students do you want to enter: ";
  cin>>choice;
  total=total+choice;
  for(int i=0; i<choice; i++) {
    cout<<"\nEnter data of student: "<<i+1<<endl<<endl;
    cout<<"Enter name: ";
    cin>>array1[i];
    cout<<"Enter roll no.:  ";
    cin>>array2[i];
    cout<<"Enter course: ";
    cin>>array3[i];
    cout<<"Enter class: ";
    cin>>array4[i];
    cout<<"Enter contact: ";
    cin>>array5[i];
  }
}
void show() {
  for(int i=0; i<total; i++) {
    cout<<"Data of student: "<<i+1;<<endl<<endl;
    cout<<"Name: "array1[i]<<endl;
    cout<<"Roll no.: "array2[i]<<endl;
    cout<<"Course: "array3[i]<<endl;
    cout<<"Class: "array4[i]<<endl;
    cout<<"Contact: "array5[i]<<endl;
  }
}
void search() {
  
}
void update() {
  
}
void deleterecord() {
  
}

main()
{
  int value;
  while(true) 
  {
  cout<<"1. Enter data"<<endl;
  cout<<"2. Show data"<<endl;
  cout<<"3. Search data"<<endl;
  cout<<"4. Update data"<<endl;
  cout<<"5. Delete data"<<endl;
  cout<<"6. Exit"<<endl;
  cin>>value;
  switch(value)
  {
    case 1:
      enter();
      break;
    case 2:
      show();
      break;
    case 3:
      search()
      break;
    case 4:
      update();
      break;
    case 5;
      deleterecord();
      break;
    case 6;
      exit(0);
  }
  }
  }
}