# A basic Flask quickstart 
*With support for serving easy APIs and static content*

[![Build Status](https://travis-ci.org/dtchanpura/flask-base.svg)](https://travis-ci.org/dtchanpura/flask-base)

To deploy a clone of this application using the [`rhc` command line tool](http://rubygems.org/gems/rhc):

    rhc app create flask python-2.7 --from-code=https://github.com/ryanj/flask-base.git
    
Or [link to a web-based clone+deploy](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Fryanj%2Fflask-base.git) on [OpenShift Online](http://OpenShift.com) or on [your own OpenShift cloud](http://openshift.github.io): 

    https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Fryanj%2Fflask-base.git

## Local server
Start a local webserver by running:

```bash
python app.py
```

## License
This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to CC0 (http://creativecommons.org/publicdomain/zero/1.0/)
