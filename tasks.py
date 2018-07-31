from invoke import task
import pathlib

THIS_DIR = pathlib.Path(__file__).parent.resolve()
HTML_DIR = pathlib.Path(THIS_DIR, '.html')
REPO_DIR = pathlib.Path(THIS_DIR, '.dgrine.github.io')

@task
def publish(context):
    """
    Publishes the Markdown documentation to HTML.
    """
    with context.cd(str(THIS_DIR)):
        print("Running pdsite")
        context.run('pdsite build')

@task
def push(context, message = "Documentation updated."):
    """
    Pushes the documentation.
    """
    with context.cd(str(THIS_DIR)):
        if not HTML_DIR.exists():
            print("No documentation to be pushed.")
            return
        if not REPO_DIR.exists():
            print("Cloning dgrine.github.io")
            context.run('git clone https://github.com/dgrine/dgrine.github.io.git {}'.format(REPO_DIR))
        print("Cleaning {}".format(REPO_DIR))
        with context.cd(str(REPO_DIR)):
            context.run('rm -rf *')
            print("Copying {}".format(HTML_DIR))
            context.run('cp -r {}/* .'.format(HTML_DIR))
            print("Pushing changes")
            cmd = 'git add . && git commit -a -m \'{}\' && git push'.format(message)
            context.run(cmd)
