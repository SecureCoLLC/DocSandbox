import subprocess, os, sys

class Doxygen:
    def run(self, ):
        """Run the doxygen make command in the designated folder"""

        try:
            retcode = subprocess.call('cd .. && scripts/doxygen.sh', shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))
        except OSError as e:
            sys.stderr.write("doxygen execution failed: %s" % e)


    def generate(self, app):
        """Run the doxygen make commands if we're on the ReadTheDocs server"""

        read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

        if read_the_docs_build:
            run_doxygen()

def setup(app):
    doxygen = Doxygen()
    master_doc = '../doxygen/index'

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", doxygen.generate)
