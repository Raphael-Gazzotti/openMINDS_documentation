#######################
FileRepositoryStructure
#######################

:Semantic name: https://openminds.om-i.org/types/FileRepositoryStructure

:Display as: File repository structure


------------

------------

Properties
##########

:Required: `filePathPattern <filePathPattern_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _filePathPattern_heading:

***************
filePathPattern
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/filePathPattern
   :value type: | embedded object array \(1-N\) of type
                | `FilePathPattern <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/filePathPattern.html>`_
   :instructions: Add all file path patterns that define this file repository structure.

`BACK TO TOP <FileRepositoryStructure_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this file repository structure that may help you to find this instance more easily.

`BACK TO TOP <FileRepositoryStructure_>`_

------------

