//MathFuncsLib.h
namespace MathFuncs
{
	// This class is exported from the MathFuncsDll.dll
	class MyMathFuncs
	{
	public:
		// Returns a + b
		double Add(double a, double b);

		// Returns a - b
		double Subtract(double a, double b);

		// Returns a * b
		double Multiply(double a, double b);

		// Returns a / b
		// Throws const std::invalid_argument& if b is 0
		double Divide(double a, double b);
	};
}