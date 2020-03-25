import subprocess, os, sys

sys.path.append( "ext/breathe/")
extensions = ['sphinx.ext.pngmath', 'sphinx.ext.todo', 'breathe' ]
breathe_projects = { "sandbox": "doxygen/xml/" }
breathe_default_project = "sandbox"

# master_doc = '../doxygen/index'

class Doxygen:
    def run(self, ):
        """Run the doxygen make command in the designated folder"""

        try:
            retcode = subprocess.call('pwd && cd .. && scripts/doxygen.sh', shell=True)
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

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", doxygen.generate)
