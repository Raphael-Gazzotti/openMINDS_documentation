###########
FileArchive
###########

:Semantic name: https://openminds.om-i.org/types/FileArchive

:Display as: File archive


------------

------------

Properties
##########

:Required: `IRI <IRI_heading_>`_, `format <format_heading_>`_
:Optional: `sourceData <sourceData_heading_>`_

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
   :instructions: Enter the internationalized resource identifier (IRI) to this file archive.

`BACK TO TOP <FileArchive_>`_

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
   :instructions: Add the content type of this file archive.

`BACK TO TOP <FileArchive_>`_

------------

.. _sourceData_heading:

**********
sourceData
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sourceData
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add the data that were ingested and modified to create this file archive.

`BACK TO TOP <FileArchive_>`_

------------

