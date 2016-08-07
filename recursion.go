package main 

import "fmt" 

func fib(n) {
	if (n == 0)
	  return 1
	if (n == 1)
	  return 1

	return fib(n-1) + fib(n-2)
}

func main() {
	fmt.Printf(fib(3))
}