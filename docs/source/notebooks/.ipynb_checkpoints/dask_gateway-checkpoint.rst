Using Dask Gateway
==================

If you need extra compute resources the SMCE has the ability to spool up additional AWS EC2 worker nodes via Dask Gateway. 
Adding the nebari-dask package to your conda environment installs all of the necessary libraries for Dask Gateway to work.

Users do not have access to the is feature by default. Ask an admin to grant you access.

::
    
    from dask_gateway import Gateway
    from distributed import Client

::

    gateway = Gateway()

Select the Python environment, size of worker nodes, and set any environment variables. Currently there are two options for workers nodes:

* Small worker
    
    * 2 cores
    * 8GB Memory

* Medium worker
    
    * 4 cores
    * 16GB Memory

Each cluster can have several worker nodes. It is recommended to start with the small worker.

::

    options = gateway.cluster_options()
    options

.. image:: ../images/dask_gateway/cluster_options.jpg


Wait until the cluster is created. The cluster is spooling up additional AWS EC2 instances. This can take a few minutes.

Scale the cluster to your required size.

**If you are using the small worker for every two workers a new EC2 instance is started**

**If you are using the medium worker for every workers a new EC2 instance is started**

**There are only 10 worker nodes maximum for everyone, please use this responsibly**

The cluster can be managed via the provided link. Scaling can take time depending on the number of workers requested. 
Follow the link and navigate to the workers tab to see when the workers are available to use.

::

    cluster = gateway.new_cluster(options)
    cluster

.. image:: ../images/dask_gateway/dask_cluster.jpg

If you loose connection to your notebook **Do not start another cluster without checking to see if you previous cluster still exists**

The following code shows how to check for existing clusters and how to reconnect to them

**Starting a new cluster will start additional AWS compute resources**

::

    existing_clusters = gateway.list_clusters()
    existing_clusters

[]   

::

    cluster = cluster = gateway.connect(existing_clusters[0].name)
    cluster

.. image:: ../images/dask_gateway/dask_cluster.jpg

The final step is to assign the cluster as your Dask Client. Once this is done any time you call compute the cluster will be used rather than your local compute resources.

::

    client = Client(cluster)
    client

.. image:: ../images/dask_gateway/dask_client.jpg


After you are finished using the cluster make sure you shut everything down. It can take a few minutes to shut everything down.

::

    cluster.shutdown()