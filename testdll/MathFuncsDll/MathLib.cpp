#include "MathLib.h"
#include <windows.h>
#include "MathFuncsLib.h"

void* InitMath() 
{
	return new MathFuncs::MyMathFuncs;
}

void Destory(void* mb)
{
	if (mb != NULL) 
		delete (MathFuncs::MyMathFuncs*)mb;
}

double Add_d(double a, double b)
{
	MathFuncs::MyMathFuncs* mathfunc = new MathFuncs::MyMathFuncs;
	double res = mathfunc->Add(a,b);
	return res;
}

double Subtract_d(double a, double b)
{
	MathFuncs::MyMathFuncs* mathfunc = new MathFuncs::MyMathFuncs;
	double res = mathfunc->Subtract(a, b);
	return res;
}

double Multiply_d(double a, double b)
{
	return 0.8;
}

double Divide_d(double a, double b)
{
	return 1.0;
}

char* Divide_s(char * a)
{	
	return a;
}


int test(outStruct *o){
	unsigned int i = 4;
	o->kw = (keywords*)malloc(sizeof(unsigned char) * 10 * i);
	strcpy_s(o->kw[0].words, "The First data");
	strcpy_s(o->kw[1].words, "The Second data");

	o->len = i;
	return 1;
}

int sumnum(MyStruct* vStruct)
{
	if (vStruct == 0)
	{
		printf("error args...");
		return 0;
	}

	vStruct->sum = vStruct->numA + vStruct->numB;
	//strcpy_s(vStruct->numStr, "11111111111");
	sprintf(vStruct->numStr, "%d+%d=%d", vStruct->numA, vStruct->numB, vStruct->sum);

	return 0;
}