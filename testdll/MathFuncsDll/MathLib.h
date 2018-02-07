#pragma once
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


#ifdef MATHFUNCSDLL_EXPORTS
#define MATHFUNCSDLL_API __declspec(dllexport) 
#else
#define MATHFUNCSDLL_API __declspec(dllimport) 
#endif

typedef struct
{
	char words[20];
}keywords;

typedef struct
{
	keywords *kw;
	unsigned int len;
}outStruct;

struct MyStruct
{
	int numA;
	int numB;
	int sum;
	char numStr[256];
};

extern "C" {
	MATHFUNCSDLL_API void* InitMath();
	MATHFUNCSDLL_API void Destory(void* mb);
	MATHFUNCSDLL_API double Add_d(double a, double b);
	MATHFUNCSDLL_API double Subtract_d(double a, double b);
	MATHFUNCSDLL_API double Multiply_d(double a, double b);
	MATHFUNCSDLL_API double Divide_d(double a, double b);
	MATHFUNCSDLL_API char* Divide_s(char* a);
	MATHFUNCSDLL_API int test(outStruct *o);
	MATHFUNCSDLL_API int sumnum(MyStruct *vStruct);
}
