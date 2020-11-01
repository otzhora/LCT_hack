import tempfile
import subprocess


class CodeManager:
    def __init__(self, git_path, runner, *runner_args, **runner_kwargs):
        self.git_path = git_path
        self.runner = runner(*runner_args, **runner_kwargs)

    def run_code(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            subprocess.run(["git", "clone", self.git_path, tmp_dir])
            try:
                setup_res = self.runner.setup(tmp_dir)
            except subprocess.CalledProcessError:
                setup_res = "Setup error"

            try:
                checks_res = self.runner.checks(tmp_dir)
            except subprocess.CalledProcessError as e:
                checks_res = e.output

            try:
                run_res = self.runner.run_code(tmp_dir)
            except subprocess.CalledProcessError as e:
                run_res = e.output

        return {
            "setup": setup_res,
            "checks": checks_res,
            "run": run_res
        }


class CodeRunner:
    def __init__(self, setup_script, checks_script, run_script):
        self.setup_script = setup_script
        self.checks_script = checks_script
        self.run_script = run_script

    def setup(self, tmp_dir):
        return subprocess.check_output(["sh", str(self.setup_script)], cwd=tmp_dir, timeout=350)

    def checks(self, tmp_dir):
        return subprocess.check_output(["sh", str(self.checks_script)], cwd=tmp_dir, timeout=350)

    def run_code(self, tmp_dir):
        return subprocess.check_output(["sh", str(self.run_script)], cwd=tmp_dir, timeout=350)
