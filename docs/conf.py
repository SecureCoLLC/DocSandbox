import subprocess, os

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('pwd; pushd .. && doxygen .doxygen-config; popd', shell=True)

