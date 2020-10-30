import os


class CodeConverter:
    def __init__(self, path_for_students_solutions):
        self.path_for_student_solutions = path_for_students_solutions
        self.lang_exts = {
            "Python": "py",
            "Cpp": "cpp"
        }

        if not os.path.isdir(self.path_for_student_solutions):
            try:
                os.mkdir(self.path_for_student_solutions)
            except OSError:
                print("Creation of the directory %s failed" % self.path_for_student_solutions)
            else:
                print("Successfully created the directory %s " % self.path_for_student_solutions)

    def create_folder_for_user(self, username):
        path = f"{self.path_for_student_solutions}/{username}"
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)

    def create_folder_for_task(self, username, task):
        self.create_folder_for_user(username)
        path = f"{self.path_for_student_solutions}/{username}/{task}"
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)

    def text_to_code(self, username, task, text, lang):
        self.create_folder_for_task(username, task)
        path = f"{self.path_for_student_solutions}/{username}/{task}/solution.{self.lang_exts[lang]}"

        with open(path, "w") as f:
            f.write(text)

    def get_code_path(self, username, task):
        self.create_folder_for_task(username, task)
        return f"{self.path_for_student_solutions}/{username}/{task}"
