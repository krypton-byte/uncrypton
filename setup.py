from distutils.core import setup
setup(
  name = 'uncrypton',         # How you named your package folder (MyLib)
  packages = ['uncrypton'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'unmarshaling for python',   # Give a short description about your library
  author = 'Krypton:~#',                   # Type in your name
  author_email = 'galaxyvplus6434@gmail.com',      # Type in your E-Mail
  url = 'https://papaclash.com',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/uncrypton.tar.gz',    # I explain this later on
  keywords = ['decode', 'unmarshaling', 'unmarsh'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
