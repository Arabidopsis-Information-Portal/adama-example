=====================================
An example of a microservice in Adama
=====================================

This repository includes a complete example for registering a service
in Adama, including documentation of parameters and provenance.

The easiest way to run this example is using `Docker`_:

- Install Docker following `these instructions`_ (available for Linux,
  Mac, and Windows).

- Install ``docker-compose`` following `these other instructions`_.

- Clone this repository and execute ``docker-compose``:

  .. code-block:: bash

     $ git clone https://github.com/waltermoreira/adama-example.git
     $ cd adama-example
     $ docker-compose build
     $ docker-compose up

Access the notebook at:

- Linux: http://localhost:8888

- Mac or Windows: ``http://$(boot2docker ip):8888``

The notebook can also be `displayed read-only`_ with no installation,
thanks to the `great work of Github team`_.


.. _Docker: http://docker.com
.. _these instructions: https://docs.docker.com/installation/#installation
.. _these other instructions: https://docs.docker.com/compose/install/#install-compose
.. _displayed read-only: https://github.com/waltermoreira/adama-example/blob/master/notebooks/Example.ipynb
.. _great work of Github team: https://github.com/blog/1995-github-jupyter-notebooks-3
