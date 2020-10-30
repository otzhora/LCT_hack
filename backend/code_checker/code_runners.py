import subprocess
import os


class BaseRunner:
    def __init__(self, file_path, tests_path=None, checker=False):
        self.file_path = file_path
        self.tests_path = tests_path
        self.checker = checker
        self.tests = [f"{tests_path}/{test}" for test in os.listdir(self.tests_path)]

    def run_code(self):
        raise NotImplemented


class PythonRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run_code(self):
        test_results = []
        for test in sorted(self.tests):
            student_result = subprocess.check_output(["python3", f"{self.file_path}/solution.py"],
                                                     cwd=test,
                                                     timeout=5,
                                                     stderr=subprocess.STDOUT)
            student_result = str(student_result, "utf-8")

            with open(f"{test}/correct.txt", 'r') as f:
                correct_result = f.readlines()

            test_results.append(student_result.strip() == "".join(correct_result).strip())

        return test_results


class CppRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compile_code(self):
        subprocess.run(["g++", f"{self.file_path}/solution.cpp", "-o", f"{self.file_path}/solution.o"])

    def run_code(self):
        test_results = []
        for test in sorted(self.tests):
            student_result = subprocess.check_output([f"{self.file_path}/solution.o"],
                                                     cwd=test,
                                                     timeout=5,
                                                     stderr=subprocess.STDOUT)
            student_result = str(student_result, "utf-8")

            with open(f"{test}/correct.txt", 'r') as f:
                correct_result = f.readlines()

            test_results.append(student_result.strip() == "".join(correct_result).strip())

        return test_results
