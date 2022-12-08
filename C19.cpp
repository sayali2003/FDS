#include<iostream>
using namespace std;
struct Node
{
    string Name;
    string PRN;
    struct Node * ptr;
};

void printList(struct Node * x)
{
    int sr_no = 1;
    cout<<"\n"<<endl;
    cout<<"List of Pinnacle Club : "<<endl;
    while (x != NULL)
    {
        cout<<" "<<sr_no<<". "<<x-> Name<<"\t"<<x -> PRN<<endl;
        x = x -> ptr;
        sr_no++;
    }
    cout<<"There are total "<<(sr_no-1)<<" Members in Pinnacle Club ";
}

int main()
{
    struct Node * head = new Node();
    struct Node * last = new Node();
    cout<<"Enter President's Name : ";
    cin>>head -> Name;
    cout<<"Enter President's PRN : ";
    cin>>head -> PRN;
    cout<<"Enter Seceretary's Name : ";
    cin>>last -> Name;
    cout<<"Enter Seceretary's PRN : ";
    cin>>last -> PRN;
    head -> ptr = last;
    last -> ptr = NULL;
    
    struct Node * pntr;
    pntr = head;

    cout<<"1 - To Change President \n2 - To Change Seceretary \n3 - To Add a Member \n4 - To Delete a Member \n5 - To Exit Program "<<endl;
    int ch;
    int key = -1;
    while (key != 1)
    {  
        cout<<"Enter Your Choice : ";
        cin>>ch;      
        switch (ch)
        {
            case 1:
            {
                cout<<"Enter New President's Name : ";
                cin>>head -> Name;
                cout<<"Enter New President's PRN : ";
                cin>>head -> PRN;
                break;
            }
            case 2:
            {
                cout<<"Enter New Seceretary's Name : ";
                cin>>last -> Name;
                cout<<"Enter New Seceretary's PRN : ";
                cin>>last -> PRN;
                break;
            }
            case 3:
            {
                int new_mem;
                cout<<"Enter How many Members you wish to Register : ";
                cin>>new_mem;
                for (int i = 0; i<(new_mem); i++)
                {
                    struct Node * var = new Node();
                    pntr -> ptr = var;
                    var -> ptr = last;
                    pntr = pntr -> ptr;
                    cout<<"Enter New Member's Name : ";
                    cin>>var -> Name;
                    cout<<"Enter New Member's PRN : ";
                    cin>>var -> PRN;
                }
                break;
            }
            case 4:
            {
                string del_prn;
                cout<<"Enter PRN of the Member you wish to Delete : ";
                cin>>del_prn;
                struct Node * temp = head;
                while ((temp -> ptr) -> PRN != del_prn)
                {
                    temp = temp -> ptr;
                }
                temp -> ptr = temp -> ptr -> ptr;
                break;
            }
            case 5:
            {
                cout<<"You Choose to Exit ";
                key = 1;
                break;
            }
            default:
            {
                cout<<"You Entered Wrong Choice...!!!!"<<endl;
                key = 1;
                break;
            }
        }
    }
    printList(head);
}