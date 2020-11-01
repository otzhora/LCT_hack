import subprocess
import os


def check_same(student_result, correct_result):
    return "".join(student_result).strip() == "".join(correct_result).strip()


class BaseRunner:
    def __init__(self, file_path, tests_path=None, post=False, hooks: set = None):
        self.launch_command = []
        self.file_path = file_path
        self.tests_path = tests_path
        self.post = post
        self.tests = [f"{tests_path}/{test}" for test in os.listdir(self.tests_path)]
        if hooks is None:
            self.hooks = set()
        else:
            self.hooks = hooks

    def run_code(self):
        test_results = []
        style_result = None

        if "pre_run" in self.hooks:
            self.pre_run()

        if "style" in self.hooks:
            style_result = self.check_style()

        for test in sorted(self.tests):
            success = False
            try:
                with open(f"{test}/input.txt", "r") as f:
                    student_in = "".join(f.readlines())
                student_result = subprocess.check_output(self.launch_command,
                                                         cwd=test,
                                                         timeout=5,
                                                         stderr=subprocess.STDOUT,
                                                         input=student_in.encode("utf-8"))
                student_result = str(student_result, "utf-8")
                success = True
            except subprocess.TimeoutExpired:
                student_result = "Time limit exceeded"
            except subprocess.CalledProcessError as e:
                student_result = e.output

            check_result = False
            if success:
                with open(f"{test}/correct.txt", 'r') as f:
                    correct_result = f.readlines()

                check_result = check_same(student_result, correct_result)

            test_results.append({"student_output": student_result,
                                 "style_result": style_result,
                                 "check": check_result})

        return test_results

    def pre_run(self):
        raise NotImplemented

    def check_style(self):
        raise NotImplemented


class PythonRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launch_command = ["python3", f"{self.file_path}/solution.py"]

    def check_style(self):
        try:
            return subprocess.check_output(["flake8", f"{self.file_path}/solution.py"],
                                           timeout=5,
                                           stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return e.output


class CppRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launch_command = [f"{self.file_path}/solution.o"]
        self.hooks.add("pre_run")

    def compile_code(self):
        subprocess.run(["g++", f"{self.file_path}/solution.cpp", "-o", f"{self.file_path}/solution.o"])

    def pre_run(self):
        self.compile_code()


class JsRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launch_command = ["node", f"{self.file_path}/solution.js"]


class RubyRunner(BaseRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launch_command = ["ruby", f"{self.file_path}/solution.rb"]


class HaskellRunner(BaseRunner):
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launch_command = [f"{self.file_path}/solution"]
        self.hooks.add("pre_run")

    def compile_code(self):
        subprocess.run(["ghc", f"{self.file_path}/solution.hs"])

    def pre_run(self):
        self.compile_code()


Languages = {
    "Python": PythonRunner,
    "Cpp": CppRunner,
    "JS": JsRunner,
    "Ruby": RubyRunner
}
