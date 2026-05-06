####
File
####

:Semantic name: https://openminds.om-i.org/types/File

:Display as: File

Structured information on a file instance that is accessible via a URL.


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `name <name_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `dataType <dataType_heading_>`_, `fileRepository <fileRepository_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `isPartOf <isPartOf_heading_>`_, `specialUsageRole <specialUsageRole_heading_>`_, `storageSize <storageSize_heading_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to this file instance.

`BACK TO TOP <File_>`_

------------

.. _contentDescription_heading:

******************
contentDescription
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contentDescription
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter a short content description for this file instance.

`BACK TO TOP <File_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataType
   :value type: | linked object array \(1-N\) of type
                | `DataType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/dataType.html>`_
   :instructions: Add all data types that are specifically represented in this file instance.

`BACK TO TOP <File_>`_

------------

.. _fileRepository_heading:

**************
fileRepository
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fileRepository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the overarching repository to which this file instance belongs.

`BACK TO TOP <File_>`_

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
   :instructions: Add the content type of this file instance.

`BACK TO TOP <File_>`_

------------

.. _hash_heading:

****
hash
****

Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/hash
   :value type: | embedded object array \(1-N\) of type
                | `Hash <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/hash.html>`_
   :instructions: Add all hashes that were generated for this file instance.

`BACK TO TOP <File_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `FileBundle <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all file bundles in which this file instance is grouped into.

`BACK TO TOP <File_>`_

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
   :instructions: Enter the name of this file instance.

`BACK TO TOP <File_>`_

------------

.. _specialUsageRole_heading:

****************
specialUsageRole
****************

Particular function of something when it is used.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specialUsageRole
   :value type: | linked object of type
                | `FileUsageRole <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/fileUsageRole.html>`_
   :instructions: Add the special usage role of this file instance.

`BACK TO TOP <File_>`_

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
   :instructions: Enter the storage size of this file instance.

`BACK TO TOP <File_>`_

------------

