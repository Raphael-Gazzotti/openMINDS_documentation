##################
ContentTypePattern
##################

:Semantic name: https://openminds.ebrains.eu/core/ContentTypePattern

:Display as: Content type pattern


------------

------------

Properties
##########

:Required: `contentType <contentType_heading_>`_, `regex <regex_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _contentType_heading:

***********
contentType
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contentType
   :value type: | linked object of type
                | `ContentType <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/contentType.html>`_
   :instructions: Enter the content type that can be defined by the given regular expression for file names/extensions.

`BACK TO TOP <ContentTypePattern_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this content type pattern.

`BACK TO TOP <ContentTypePattern_>`_

------------

.. _regex_heading:

*****
regex
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/regex
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a regular expression for the file names/extensions that defines the give content type.

`BACK TO TOP <ContentTypePattern_>`_

------------

