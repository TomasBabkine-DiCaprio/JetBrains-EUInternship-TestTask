# JetBrains-EUInternship-TestTask
This is my submission for the JetBrains AI-Powered Code Assistance with GPT-3 and Codex Summer Internship test task. 
Students were asked to propose an algorithm to solve a problem and implement it in any language. I chose Python3.

# Problem statement
Given N hours to prepare for an exam, how can a programmer optimize their time given M topics to cover. A topic i requires Ti time to study, and has a certain number of questions Ki that could appear on the exam. The exam comprises of L questions chosen randomly with an equal probability. What is the best way to use the limited time to maximize the chances of getting the best possible grade?

# Problem solution
To maximize their chances of getting the best possible grade, the programmer should dedicate the most hours to the topics that have a higher probability of appearing on the exam and take the least amount of time to study. Let Ji be defined as the number of hours it take to study a question in i, we have Ji = Ti/ki. We then greedily study these questions until the sum of their time = N.

# Input
My program takes as input a .txt file with the following structure. The input starts with one line containing three positive integers, N, M & L separated by a space. Then follow M lines containing two integers Ti & Ki.

(This input format is similar to the one found on the [Kattis](https://open.kattis.com/) platform).

# Output
The output is printed on one line and contains values H1, ..., HM separated by a space, indicating how much time must be dedicated to studying topic i. The values are rounded to the 2nd decimal point.

# Performance
The algorithm runs in approximately O(n + nlogn) where n is the number of topics. Sorting the topics is the operation that takes the longest at O(nlogn)

# How to run this program
The program can be run from the command line with 
``` Bash
python3 script.py < '<path/to/input/file>'
```
For convenience, I have provided some sample input files in the SampleInputs directory.

# How to run tests
In the ```tests``` directory, run the following command:
``` Bash
python3 -m unittest discover
```
