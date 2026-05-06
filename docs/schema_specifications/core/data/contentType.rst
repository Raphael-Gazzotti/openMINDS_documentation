###########
ContentType
###########

:Semantic name: https://openminds.om-i.org/types/ContentType

:Display as: Content type

Structured information on the content type of a file instance, bundle or repository.


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/v5.0/instance_libraries/contentTypes.html>`_.

------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `dataType <dataType_heading_>`_, `definingSource <definingSource_heading_>`_, `description <description_heading_>`_, `displayLabel <displayLabel_heading_>`_, `fileExtension <fileExtension_heading_>`_, `isBasedOn <isBasedOn_heading_>`_, `specification <specification_heading_>`_, `synonym <synonym_heading_>`_

------------

.. _dataType_heading:

********
dataType
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataType
   :value type: | linked object array \(1-N\) of type
                | `DataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dataType.html>`_
   :instructions: Add all data types that may be represented via this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _definingSource_heading:

**************
definingSource
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/definingSource
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifiers (IRIs) of sources that define or document this content type, preferably authoritative registries (e.g., IANA), or reference documentation (e.g., mimetype.io) if no registry entry exists.

`BACK TO TOP <ContentType_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of the content type specification. Leave blank if an official and public specification is linked under 'specification' for this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _displayLabel_heading:

************
displayLabel
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/displayLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a display label for this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _fileExtension_heading:

*************
fileExtension
*************

String of characters attached as suffix to the names of files of a particular format.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fileExtension
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all file extensions associated with this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _isBasedOn_heading:

*********
isBasedOn
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isBasedOn
   :value type: | linked object array \(1-N\) of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/contentType.html>`_
   :instructions: Add all content types this content type is based on.

`BACK TO TOP <ContentType_>`_

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
   :instructions: Enter the name of this content type following a IANA.org inspired convention.

`BACK TO TOP <ContentType_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specification
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the official specification of this content type. If no official and public specification is available, leave blank and enter the specification under 'description'.

`BACK TO TOP <ContentType_>`_

------------

.. _synonym_heading:

*******
synonym
*******

Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/synonym
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter any synonyms of this content type.

`BACK TO TOP <ContentType_>`_

------------

