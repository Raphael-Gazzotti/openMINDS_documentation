##############
FileRepository
##############

:Semantic name: https://openminds.ebrains.eu/core/FileRepository

:Display as: File repository

Structured information on a file repository.


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `hostedBy <hostedBy_heading_>`_, `name <name_heading_>`_
:Optional: `contentTypePattern <contentTypePattern_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `repositoryType <repositoryType_heading_>`_, `storageSize <storageSize_heading_>`_, `structurePattern <structurePattern_heading_>`_

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _contentTypePattern_heading:

******************
contentTypePattern
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentTypePattern
   :value type: | embedded object array \(1-N\) of type
                | `ContentTypePattern <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/contentTypePattern.html>`_
   :instructions: Add all content type patterns that would identify matching content types for files within this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/contentType.html>`_
   :instructions: If file instances and bundles within the repository are organized and formatted according to a formal data structure use the appropriate contentType. Leave blank otherwise.

`BACK TO TOP <FileRepository_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hash
   :value type: | embedded object of type
                | `Hash <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/hash.html>`_
   :instructions: Add the hash that was generated for this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _hostedBy_heading:

********
hostedBy
********

Reference to an organization that provides facilities and services for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/hostedBy
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the host of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _repositoryType_heading:

**************
repositoryType
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/repositoryType
   :value type: | linked object of type
                | FileRepositoryType \[TYPE_ERROR\]
   :instructions: Add the type of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _storageSize_heading:

***********
storageSize
***********

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the storage size this file repository allocates.

`BACK TO TOP <FileRepository_>`_

------------

.. _structurePattern_heading:

****************
structurePattern
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/structurePattern
   :value type: | linked object of type
                | `FileRepositoryStructure <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileRepositoryStructure.html>`_
   :instructions: Add a file repository structure which identifies the file path patterns used in this file repository.

`BACK TO TOP <FileRepository_>`_

------------

