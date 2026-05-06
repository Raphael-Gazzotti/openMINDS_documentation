###############
FilePathPattern
###############

:Semantic name: https://openminds.ebrains.eu/core/FilePathPattern

:Display as: File path pattern


------------

------------

Properties
##########

:Required: `groupingType <groupingType_heading_>`_, `regex <regex_heading_>`_
:Optional:

------------

.. _groupingType_heading:

************
groupingType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/groupingType
   :value type: | linked object of type
                | `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/fileBundleGrouping.html>`_
   :instructions: Add the type of grouping that is defined by the given file path pattern.

`BACK TO TOP <FilePathPattern_>`_

------------

.. _regex_heading:

*****
regex
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/regex
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the regular expression that defines this file path pattern.

`BACK TO TOP <FilePathPattern_>`_

------------

