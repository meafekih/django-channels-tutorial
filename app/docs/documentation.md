Using your own package¶
Since we moved the polls directory out of the project, it’s no longer working. We’ll now fix this by installing our new django-polls package.

Installing as a user library

The following steps install django-polls as a user library. Per-user installs have a lot of advantages over installing the package system-wide, such as being usable on systems where you don’t have administrator access as well as preventing the package from affecting system services and other users of the machine.

Note that per-user installations can still affect the behavior of system tools that run as that user, so using a virtual environment is a more robust solution (see below).

To install the package, use pip (you already installed it, right?):

python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
With luck, your Django project should now work correctly again. Run the server again to confirm this.

To uninstall the package, use pip:

python -m pip uninstall django-polls
Publishing your app¶
Now that we’ve packaged and tested django-polls, it’s ready to share with the world! If this wasn’t just an example, you could now:

Email the package to a friend.
Upload the package on your website.
Post the package on a public repository, such as the Python Package Index (PyPI). packaging.python.org has a good tutorial for doing this.
Installing Python packages with a virtual environment¶
Earlier, we installed the polls app as a user library. This has some disadvantages:

Modifying the user libraries can affect other Python software on your system.
You won’t be able to run multiple versions of this package (or others with the same name).
Typically, these situations only arise once you’re maintaining several Django projects. When they do, the best solution is to use venv. This tool allows you to maintain multiple isolated Python environments, each with its own copy of the libraries and package namespace.