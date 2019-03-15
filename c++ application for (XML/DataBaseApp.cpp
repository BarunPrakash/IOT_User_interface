// same problem using constructor / polymorphism
//Write C code here
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdint.h>
#include<limits.h>

using namespace std;
#define maxsize  2

/*
 *
 * using Class

*/




class empD
{
    private:
 unsigned int AccountNo;
 char strEmpName[16];
    protected:
 char valuableForLoan[16];
    public:
 unsigned int savingAccoutRs;
 empD()
 {
  AccountNo =4444;
  savingAccoutRs =0;

 }
 //~empD();
 void getDataIntoClass(void);
 void printEligibiltyMessageOnScreen(void)
 {

  printf("Acc:-%5d\n",AccountNo);
  printf("NAME:-%5s\n",strEmpName);
  printf("Rate:-%5s\n",valuableForLoan);


 }
 virtual void customerGrade(void) =0;

// function Deceleration

void AccesStructureObject(void);




};
void empD ::getDataIntoClass(void)
{

 cout<<"Enter Acc No"<<'\n';
 cin>>AccountNo;
 cout<<"Enter Name"<<'\n';
 cin>>strEmpName;
 cout<<"Enter SavingNo:-"<<'\n';
 cin>>savingAccoutRs;


}


class loanDep : public empD
{

   public:
   void checkValidtyOfFunc(void)
   {


  unsigned int tempVal=0;
  if(savingAccoutRs >30000)
  {
   tempVal= savingAccoutRs -10000;
   printf("Congratulation !! you are eligible for  loan:-%d\n",tempVal);

   strcpy(valuableForLoan ,"@3");

  }
  else
  {
   tempVal= savingAccoutRs -5000;
   printf("Congratulation !! you are eligible for  loan:-%d\n",tempVal);

   strcpy(valuableForLoan ,"@5");

  }
   }
   void customerGrade(void)
   {
    if(savingAccoutRs >60000)
    {
   cout<<"He is the premium  Customer!! Kindly  Ask for byke loan"<<endl;
    }
    else
    {
     cout<<"Thanks,we look forward for more assistance  "<<endl;
    }
   }


};


void AccesStructureObject(void)
{


 loanDep Lobj[2];
 empD *empPtr;
 empPtr =&Lobj[0];

 for(uint8_t  mov=0; mov<maxsize;mov++)
 {
  Lobj[mov].getDataIntoClass();

 }

 for(uint8_t  mov=0; mov<maxsize;mov++)
 {
  printf("----------------------------\n");

  Lobj[mov].checkValidtyOfFunc();
  Lobj[mov].printEligibiltyMessageOnScreen();

  printf("----------------------------\n");
 }
 printf("----------------------------\n");
 empPtr->customerGrade();
 printf("----------------------------\n");
}



int main()
{

 AccesStructureObject();





return 1;
}
