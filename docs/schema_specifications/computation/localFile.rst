#########
LocalFile
#########

:Semantic name: https://openminds.om-i.org/types/LocalFile

:Display as: Local file

Structured information about a file that is not accessible via a URL.


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `path <path_heading_>`_
:Optional: `contentDescription <contentDescription_heading_>`_, `copyOf <copyOf_heading_>`_, `dataType <dataType_heading_>`_, `format <format_heading_>`_, `hash <hash_heading_>`_, `specialUsageRole <specialUsageRole_heading_>`_, `storageSize <storageSize_heading_>`_

------------

.. _contentDescription_heading:

******************
contentDescription
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contentDescription
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter a short content description for this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

.. _copyOf_heading:

******
copyOf
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/copyOf
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add the file of which this is a copy.

`BACK TO TOP <LocalFile_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataType
   :value type: | linked object array \(1-N\) of type
                | `DataType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/dataType.html>`_
   :instructions: Add all data types that are specifically represented in this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Add the content type of this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Add the hash that was generated for this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Enter the name of this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

.. _path_heading:

****
path
****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/path
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the file system path (absolute path or relative to the working directory) to this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Add the special usage role of this local file instance.

`BACK TO TOP <LocalFile_>`_

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
   :instructions: Enter the storage size of this local file instance.

`BACK TO TOP <LocalFile_>`_

------------

