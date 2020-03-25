import subprocess, os

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('pwd; cd .. && doxygen .doxygen-config; cd docs', shell=True)

