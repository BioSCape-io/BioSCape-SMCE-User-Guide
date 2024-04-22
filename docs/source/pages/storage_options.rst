===============
Storage Options
===============

Users currently have the following storage options:

Home Directory
--------------

    Appears as `/` in the file browser; full path is `/home/<username>`.
    This is regular file-system storage. It is private to your user, but is **limited in terms of space (10GB),
    so use this sparingly**. It is persistent across sessions,
    but we recommend making sure all important files are backed up.



EFS
---

    Appears as `shared` in the file browser (relative to the home directory); full path is `/home/<username>/shared`.
    The shared storage is split up based on the user groups you are apart of. I recommend using the `user` directory.
    the shared storage is regular file-system storage. I strongly recommended that you create user and/or sub-project-specific
    subdirectories here to keep things organized. This is technically unlimited,
    but is on a pay-for-what-you-use model, so please use responsibly. 
    It is more expensive and, usually, somewhat less performant than S3.


.. _s3_buckets:

S3 buckets
----------

    There are two s3 buckets that are part of the BioSCape SMCE


    * bioscape-data

            This is where the BioSCape data lives. It is read-only

    * bioscape-smce-user-bucket

        This is an S3 bucket set up for users to use as another storage option. It is a good place for storing things like larger data products. 
        s3 buckets do not behave like a regular file system and are not designed for constant reads and writes. 

