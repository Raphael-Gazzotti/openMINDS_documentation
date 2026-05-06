##############
FileRepository
##############

:Semantic name: https://openminds.om-i.org/types/FileRepository

:Display as: File repository

Structured information on a file repository.


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `hostedBy <hostedBy_heading_>`_, `name <name_heading_>`_
:Optional: `contentTypePattern <contentTypePattern_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `storageSize <storageSize_heading_>`_, `structurePattern <structurePattern_heading_>`_, `type <type_heading_>`_

------------

.. _IRI_heading:

***
IRI
***

Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/IRI
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _contentTypePattern_heading:

******************
contentTypePattern
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contentTypePattern
   :value type: | linked object array \(1-N\) of type
                | `ContentTypePattern <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/contentTypePattern.html>`_
   :instructions: Add all content type patterns that identify matching content types for files within this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _format_heading:

******
format
******

Method of digitally organizing and structuring data or information.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/format
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/contentType.html>`_
   :instructions: If the files and file bundles within this repository are organised and formatted according to a formal data structure, add the content type of this formal data structure. Leave blank if no formal data structure has been applied.

`BACK TO TOP <FileRepository_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hash
   :value type: | embedded object of type
                | `Hash <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/hash.html>`_
   :instructions: Add the hash that was generated for this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _hostedBy_heading:

********
hostedBy
********

Reference to an organization that provides facilities and services for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hostedBy
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the host organization of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the name of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _storageSize_heading:

***********
storageSize
***********

Quantitative value defining how much disk space is used by an object on a computer system.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/storageSize
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the storage size of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _structurePattern_heading:

****************
structurePattern
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/structurePattern
   :value type: | linked object of type
                | `FileRepositoryStructure <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileRepositoryStructure.html>`_
   :instructions: Add the file repository structure that identifies the file path patterns used in this file repository.

`BACK TO TOP <FileRepository_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/fileRepositoryType.html>`_
   :instructions: Add the type of this file repository.

`BACK TO TOP <FileRepository_>`_

------------

