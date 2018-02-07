// MyExecRefsDll.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	double a = 7;
	int b = 99;

	cout << "a+b=" << Add_d(a, b) << endl;
	cout << "a-b=" << Subtract_d(a, b) << endl;
	cout << "a*b=" << Multiply_d(a, b) << endl;
	cout << "a/b=" << Divide_d(a, b) << endl;

	try
	{
		cout << "a/0=" << Divide_d(a, 0) << endl;
	}
	catch (const invalid_argument &e)
	{
		cout << "Caught execption:" << e.what() << endl;
	}
	
	cout << "size char:" << sizeof(unsigned char) << endl;
	cout << "total:" << sizeof(unsigned char) * 10 * 4 << endl;

	outStruct o;
	test(&o);
	cout << "size:" << sizeof(o) << "\nlen:"<< strlen(o.kw[0].words) << endl;
	cout << "kws[0]" << o.kw[0].words << endl;
	cout << "kws[1]" << o.kw[1].words << endl;
	cout << "kws[2]" << o.kw[2].words << endl;
	cout << "kw->len" << o.len << endl;

	int k;
	cin >> k;
	return 0;
}

