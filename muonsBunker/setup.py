from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

pyEcoMugModule = Pybind11Extension(
    'pyEcoMug',
    [str(file_name) for file_name in Path("src").glob("*.cc")],
    include_dirs=["include"],
    extra_compile_args=["-O3"]
)

setup(
    name="pyEcoMug",
    version=2.1,
    ext_modules=[pyEcoMugModule],
    cmdclass={"build_ext": build_ext},
)
