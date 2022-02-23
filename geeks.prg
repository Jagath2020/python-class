{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d42523a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "35\n"
     ]
    }
   ],
   "source": [
    "#addition of two numbers#method1\n",
    "a =20\n",
    "b =15\n",
    "sum = a+b\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d7d4b50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no1:5\n",
      "enter the no2:8\n",
      "13\n"
     ]
    }
   ],
   "source": [
    "#addition of two numbers#method2\n",
    "a =int(input(\"enter the no1:\"))#get nos from users\n",
    "b =int(input(\"enter the no2:\"))\n",
    "sum = a+b\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e3c36a74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "#maximum two numbers# method1\n",
    "a = 5\n",
    "b=9\n",
    "maximum =max(a,b)\n",
    "print(maximum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "da30692a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "def maximum(a, b):#method2 for max\n",
    "     \n",
    "    if a >= b:\n",
    "        return a\n",
    "    else:\n",
    "        return b\n",
    "print(max(10,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "82519009",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "#method3 for max\n",
    "a=3\n",
    "b=5\n",
    "print(a if a >= b else b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c5e52268",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of num is 5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#factorial prg#method1\n",
    "def factorial(n):\n",
    "    \n",
    "      return 1 if (n==1 or n==0) else n * factorial(n - 1);\n",
    "num = 5\n",
    "print(\"Factorial of num is\",num)\n",
    "factorial((num))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "572629a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of no is 7\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5040"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#method2\n",
    "def factorial(n):\n",
    "    if n < 0:\n",
    "        return 0\n",
    "    elif n == 0 or n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        fact = 1\n",
    "        while(n > 1):#n=5\n",
    "            fact *= n\n",
    "            n -= 1#decrement\n",
    "        return fact\n",
    "\n",
    "num =7 \n",
    "print(\"Factorial of no is\",num)\n",
    "factorial((num))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "afb88acf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of no is 5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):#recusive function\n",
    " \n",
    "    # single line to find factorial\n",
    "    return 1 if (n==1 or n==0) else n * factorial(n - 1)\n",
    "\n",
    "num = 5\n",
    "print (\"Factorial of no is\",num)\n",
    "print(factorial(num))\n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1d9d809f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of no is 5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "#method 4 \n",
    "import math\n",
    " \n",
    "def factorial(n):\n",
    "    return(math.factorial(n))#using inbuilt function\n",
    "\n",
    "num = 5\n",
    "print(\"Factorial of no is\", num)\n",
    "print(factorial(num))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e1ca1c59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The principal is 8\n",
      "The time period is 6\n",
      "The rate of interest is 8\n",
      "The Simple Interest is 3.84\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3.84"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " #find simple interest \n",
    "def simple_interest(p,t,r):\n",
    "    print('The principal is', p)\n",
    "    print('The time period is', t)\n",
    "    print('The rate of interest is',r)\n",
    "      \n",
    "    si = (p * t * r)/100#formula for si\n",
    "      \n",
    "    print('The Simple Interest is', si)\n",
    "    return si\n",
    "\n",
    "simple_interest(8, 6, 8)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "27c90dc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area is 78.550000\n"
     ]
    }
   ],
   "source": [
    "#area of the circle(pir2)\n",
    "def findArea(r):\n",
    "    PI = 3.142#constant\n",
    "    return PI * (r*r)\n",
    "\n",
    "print(\"Area is %.6f\" % findArea(5))#0.6f denotes 6 digits after decimal\n",
    "  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3ba724e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Compound interest is 6288.946267774416\n"
     ]
    }
   ],
   "source": [
    "#compound interest\n",
    "def compound_interest(principle, rate, time):\n",
    " \n",
    "    # Calculates compound interest\n",
    "    Amount = principle * (pow((1 + rate / 100), time))#A = P*(1 + R/100)power of t \n",
    "    CI = Amount - principle\n",
    "    print(\"Compound interest is\", CI)\n",
    " \n",
    "compound_interest(10000, 10.25, 5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "adcc9fd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The ASCII value of 'g' is 103\n"
     ]
    }
   ],
   "source": [
    "#ascii values#method1\n",
    "c = 'g'\n",
    "# print the ASCII value of assigned character in c\n",
    "print(\"The ASCII value of '\" + c + \"' is\", ord(c))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "55b1a132",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a String: python\n",
      "p \t 112\n",
      "y \t 121\n",
      "t \t 116\n",
      "h \t 104\n",
      "o \t 111\n",
      "n \t 110\n"
     ]
    }
   ],
   "source": [
    "#method2\n",
    "print(\"Enter a String: \", end=\"\")\n",
    "text = input()\n",
    "for char in text:\n",
    "    ascii = ord(char)\n",
    "    print(char, \"\\t\", ascii)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "85d78b05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "def squaresum(n) :\n",
    "  \n",
    "    # Iterate i from 1 \n",
    "    # and n finding \n",
    "    # square of i and\n",
    "    # add to sum.\n",
    "    sm = 0\n",
    "    for i in range(1, n+1) :\n",
    "        sm = sm + (i * i)\n",
    "    return sm\n",
    "print(squaresum(4))\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e6e5430e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30.0\n"
     ]
    }
   ],
   "source": [
    "#method2\n",
    "def squaresum(n):\n",
    "    return (n * (n + 1) / 2) * (2 * n + 1) / 3#using formula\n",
    "  \n",
    "n = 4\n",
    "print(squaresum(n));\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "84831142",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "225\n"
     ]
    }
   ],
   "source": [
    "#sum of cube numbers#method 1 direct\n",
    "\n",
    "def cubessum(n):\n",
    "    sum = 0\n",
    "    for i in range(1, n+1):\n",
    "        sum +=i*i*i\n",
    "          \n",
    "    return sum\n",
    "print(cubessum(5))\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "46433815",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1296\n"
     ]
    }
   ],
   "source": [
    "def sumOfSeries(n):#method2 using formula\n",
    "    x = (n * (n + 1)  / 2)\n",
    "    return (int)(x * x)#formula((n*n+1)/2 )power of 2\n",
    "n = 8\n",
    "print(sumOfSeries(n))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ab27af32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "# Python Program to find position of n\\'th multiple\n",
    "# of a number k in Fibonacci Series\n",
    " \n",
    "def findPosition(k, n):\n",
    "    f1 = 0\n",
    "    f2 = 1\n",
    "    i =2;\n",
    "    while i!=0:\n",
    "        f3 = f1 + f2;\n",
    "        f1 = f2;\n",
    "        f2 = f3;\n",
    " \n",
    "        if f2%k == 0:\n",
    "            return n*i\n",
    " \n",
    "        i+=1\n",
    "         \n",
    "    return\n",
    " \n",
    " \n",
    "# Multiple no.\n",
    "n = 5\n",
    "# Number of whose multiple we are finding\n",
    "k = 4\n",
    " \n",
    "print( findPosition(k,n))\n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3070b7cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d518733c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f6382ef",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a25251f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "096937c8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8b98bd9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
