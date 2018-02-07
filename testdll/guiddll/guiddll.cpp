#include <stdio.h>

extern "C" _declspec(dllexport) int add(int a, int b)
{
	return a + b;
}