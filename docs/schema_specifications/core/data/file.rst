####
File
####

:Semantic name: https://openminds.ebrains.eu/core/File

:Display as: File

Structured information on a file instance that is accessible via a URL.


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `content <content_heading_>`_, `descendedFrom <descendedFrom_heading_>`_, `fileRepository <fileRepository_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `specialUsageRole <specialUsageRole_heading_>`_, `storageSize <storageSize_heading_>`_

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
   :instructions: Enter the internationalized resource identifier of this single file.

`BACK TO TOP <File_>`_

------------

.. _content_heading:

*******
content
*******

Something that is contained.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/content
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short content description for this file instance.

`BACK TO TOP <File_>`_

------------

.. _descendedFrom_heading:

*************
descendedFrom
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/descendedFrom
   :value type: | linked object array \(1-N\) of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/behavioralTask.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all entities that played a role in the production of this single file.

`BACK TO TOP <File_>`_

------------

.. _fileRepository_heading:

**************
fileRepository
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fileRepository
   :value type: | linked object of type
                | `FileRepository <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the over all repository to which this single file belongs.

`BACK TO TOP <File_>`_

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
   :instructions: Add the content type of this file instance.

`BACK TO TOP <File_>`_

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
   :instructions: Add the hash that was generated for this file instance.

`BACK TO TOP <File_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object array \(1-N\) of type
                | `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add one or several bundles in which this single file can be grouped.

`BACK TO TOP <File_>`_

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
   :instructions: Enter the name of this single file.

`BACK TO TOP <File_>`_

------------

.. _specialUsageRole_heading:

****************
specialUsageRole
****************

Particular function of something when it is used.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specialUsageRole
   :value type: | linked object of type
                | `FileUsageRole <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/fileUsageRole.html>`_
   :instructions: Add a special usage role for this single file.

`BACK TO TOP <File_>`_

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
   :instructions: Enter the storage size this file instance allocates.

`BACK TO TOP <File_>`_

------------

