#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

src = os.path.join("src", "euler_project", "EulerProject.h")
tests = os.path.join("tests", "euler_project_test", "euler_project_tests.cpp")
run = os.path.join("src", "euler_project_run", "EulerProjectRun.cpp")


class ProblemTemplate:
    def __init__(self, problem_index,
                 example_value, example_answer,
                 answer_value):
        self.problem_index = problem_index
        self.example_value = example_value
        self.example_answer = example_answer
        self.answer_value = answer_value
        self.insert_src()
        self.insert_tests()
        self.insert_run()

    @staticmethod
    def insert_lines(filename, string_to_add, line_match):
        # inserts string_to_add to last occurrence of line_match
        with open(filename, 'r') as f:
            lines = f.readlines()
        i_match = 0
        for i, line in enumerate(lines):
            if line[:-1] == line_match:
                i_match = i
        for line in reversed(string_to_add.split('\n')):
            lines.insert(i_match, line + '\n')
        with open(filename, 'w') as f:
            f.writelines(lines)

    def insert_src(self):
        src_string = ("    static long solve{0}(int n) {{\n"
                      "        return n;\n"
                      "    }}").format(self.problem_index)
        self.insert_lines(src, src_string, "};")

    def insert_tests(self):
        tests_string = """TEST(euler_project_{0}, test_rep){{
    EXPECT_EQ({1}, EulerProject::solve{0}({2}));
}}""".format(self.problem_index, self.example_answer, self.example_value)
        self.insert_lines(tests, tests_string, "// end of test file")

    def insert_run(self):
        run_string1 = """void run{0}(){{
    std::cout << "Question {0}\t" << std::endl;
    int l = {1};
    auto rep = EulerProject::solve{0}(l);
    std::cout << "\t" << rep << std::endl;
}}\n""".format(self.problem_index, self.answer_value)
        self.insert_lines(run, run_string1, "int main() {")
        run_string2 = """    run{}();""".format(self.problem_index)
        self.insert_lines(run, run_string2, "    return 0;")


def main():
    index = input("Enter Problem Index: ")
    example_value = input("Enter Example value: ")
    example_answer = input("Enter Example Answer: ")
    answer_value = input("Enter Answer value: ")
    ProblemTemplate(problem_index=index,
                    example_value=example_value,
                    example_answer=example_answer,
                    answer_value=answer_value)


if __name__ == "__main__":
    main()
