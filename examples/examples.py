from rules import Rule as R
from rules.combinators import and_,or_
from rules.strategies import *
from operator import add

#
def divisible_by(m):
    return lambda n: n%m ==0

def value(val):
    return lambda n: val

def always(n):
    return True


def fizzbuzz1(end):
    for i in range(1,end+1):
        yield FirstMatching()\
            (
                R( and_( divisible_by(3), divisible_by(5) ), value("FizzBuzz")),
                R(  divisible_by(3), value("Fizz")),
                R(  divisible_by(5), value("Buzz")),
                R(  always , str)
            )(i)
        
def fizzbuzz2(end):
    for i in range(1,end+1):
        yield DefaultWithExceptions(default=str )\
            (
                R(  divisible_by(3), value("Fizz")),
                R(  divisible_by(5), value("Buzz")),
                R( and_( divisible_by(3), divisible_by(5) ), value("FizzBuzz")),            
            )(i)

def fizzbuzz3(end):
    for i in range(1,end+1):
        yield DefaultWithExceptions(default=str )\
            (
                Accumulate(lambda x,y: x+y, init="")\
                (
                    R(  divisible_by(3), value("Fizz")),
                    R(  divisible_by(5), value("Buzz")),
                )
            )(i)

def fizzbuzz4(end):
    for i in range(1,end+1):
        yield DefaultWithExceptions(default=str )\
            (
                R( or_( divisible_by(3), divisible_by(5) ) ,Accumulate(add, init="")\
                                                            (
                                                                R(  divisible_by(3), value("Fizz")),
                                                                R(  divisible_by(5), value("Buzz")),
                                                            ) )
            )(i)

def main():
    for element1,element2 in zip(fizzbuzz1(100),fizzbuzz3(100)):
        assert(element1 == element2)

if __name__ == "__main__":
    main()







