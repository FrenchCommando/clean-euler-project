# Clean Euler Project

project containing code to solve problems from Euler Project

https://projecteuler.net/



## Run

Run the python script `NextProblem.py` in the directory. It creates 3 chunks of code

- the source code in `src/euler_project/EulerProject.h`
- the runnable code in `src/euler_project_run/EulerProjectRun.cpp`
- the test code in `tests/euler_project_test/euler_project_tests.cpp`



## Structure

- the project is using cmake for C++, all the cmake code is already written
- I use the python script `NextProblem.py` to generate chunks of c++ code
- the main work of the problem should be written in the `solvexxx`  function in `src/euler_project/EulerProject.h`
- the test part is to check whether your code generates the correct value of the test (there is usually a test value in the description of the problem)

- the runnable code produces the result for the problem either in `stdout` or in a `output.txt` file. (depending on whether you comment the line `freopen("/path/to/EulerProject/output.txt", "w", stdout);`)
- also you can run `ProjectEulerCaptchaSolver/euler_project.py` from `ProjectEulerCaptchaSolver` to submit the solution directly from the `output.txt` file. You have to put your credentials in `project_euler_config.json`



## Comments

I am not affiliated to the Euler Project - feel free to send me any comments.