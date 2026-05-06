###########
ContentType
###########

:Semantic name: https://openminds.ebrains.eu/core/ContentType

:Display as: Content type

Structured information on the content type of a file instance, bundle or repository.


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `description <description_heading_>`_, `fileExtension <fileExtension_heading_>`_, `relatedMediaType <relatedMediaType_heading_>`_, `specification <specification_heading_>`_, `synonym <synonym_heading_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of the content type specification. May be left blank if a public specification can be linked in 'specification'.

`BACK TO TOP <ContentType_>`_

------------

.. _fileExtension_heading:

*************
fileExtension
*************

String of characters attached as suffix to the names of files of a particular format.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fileExtension
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter one or several file extensions associated with this content type.

`BACK TO TOP <ContentType_>`_

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
   :instructions: Enter the name (iana-inspired convention) of this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _relatedMediaType_heading:

****************
relatedMediaType
****************

Reference to an official two-part identifier for file formats and format contents.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relatedMediaType
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the iternationalized resource identifier (IRI) of the official registered media type (e.g. on IANA.org) matching this content type.

`BACK TO TOP <ContentType_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/specification
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the iternationalized resource identifier (IRI) of the official specification of this content type. Leave blank and use 'description' to provide some specification if an official specification is not available.

`BACK TO TOP <ContentType_>`_

------------

.. _synonym_heading:

*******
synonym
*******

Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/synonym
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter one or several synonyms of this content type.

`BACK TO TOP <ContentType_>`_

------------

