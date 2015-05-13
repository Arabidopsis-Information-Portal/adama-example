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


.. _Docker: http://docker.com
.. _these instructions: https://docs.docker.com/installation/#installation
.. _these other instructions: https://docs.docker.com/compose/install/#install-compose
