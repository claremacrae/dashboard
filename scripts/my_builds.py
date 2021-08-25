from scripts.ClareRepos import ClareRepos
from scripts.CppApprovalTests import CppApprovalTests
from scripts.PythonApprovalTests import PythonApprovalTests
from scripts.TestFrameworkRepos import TestFrameworkRepos
from scripts.implementation.all_repos import AllRepos


def add_all_repos(builds: AllRepos) -> None:
    CppApprovalTests.add_all_repos(builds)
    PythonApprovalTests.add_all_repos(builds)
    ClareRepos.add_all_my_repos(builds)
    TestFrameworkRepos.add_all_repos(builds)


