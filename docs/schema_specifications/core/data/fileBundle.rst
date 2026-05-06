##########
FileBundle
##########

:Semantic name: https://openminds.ebrains.eu/core/FileBundle

:Display as: File bundle

Structured information on a bundle of file instances.


------------

------------

Properties
##########

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_
:Optional: `content <content_heading_>`_, `descendedFrom <descendedFrom_heading_>`_, `format <format_heading_>`_, `groupedBy <groupedBy_heading_>`_, `hash <hash_heading_>`_, `patternOfFilenames <patternOfFilenames_heading_>`_, `storageSize <storageSize_heading_>`_

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
   :instructions: Enter a short content description for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _descendedFrom_heading:

*************
descendedFrom
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/descendedFrom
   :value type: | linked object array \(1-N\) of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/behavioralTask.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_, `SubjectGroupState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectGroupState.html>`_, `SubjectState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/subjectState.html>`_, `TissueSampleCollectionState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleCollectionState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add all entities that played a role in the production of this file bundle (must be true for all grouped files).

`BACK TO TOP <FileBundle_>`_

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
   :instructions: If file instances within this bundle are organized and formatted according to a formal data structure use the appropriate contentType. Leave blank otherwise.

`BACK TO TOP <FileBundle_>`_

------------

.. _groupedBy_heading:

*********
groupedBy
*********

Reference to the aspect used to group something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupedBy
   :value type: | linked object of type
                | `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/fileBundleGrouping.html>`_
   :instructions: Add the concept which was used to group file instances into this file bundle.

`BACK TO TOP <FileBundle_>`_

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
   :instructions: Add the hash that was generated for this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_ or `FileRepository <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileRepository.html>`_
   :instructions: Add the file bundle or file repository this file bundle is a part of.

`BACK TO TOP <FileBundle_>`_

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
   :instructions: Enter the name of this file bundle.

`BACK TO TOP <FileBundle_>`_

------------

.. _patternOfFilenames_heading:

******************
patternOfFilenames
******************

Reliable sample / structure of characters valid for all names in a particular collection of files.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/patternOfFilenames
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a regular expression (syntax: ECMA 262) which is valid for all filenames of the file instances that should be grouped into this file bundle.

`BACK TO TOP <FileBundle_>`_

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
   :instructions: Enter the storage size this file bundle allocates.

`BACK TO TOP <FileBundle_>`_

------------

