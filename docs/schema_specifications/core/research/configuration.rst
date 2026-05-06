#############
Configuration
#############

:Semantic name: https://openminds.om-i.org/types/Configuration

:Display as: Configuration

Structured information about the properties or parameters of an entity or process.


------------

------------

Properties
##########

:Required: `configuration <configuration_heading_>`_, `format <format_heading_>`_
:Optional: `lookupLabel <lookupLabel_heading_>`_

------------

.. _configuration_heading:

*************
configuration
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/configuration
   :value type: | string
                | formatting: text/plain; multiline
   :instructions: Enter the configuration in a simple text based format (e.g., JSON or YAML).

`BACK TO TOP <Configuration_>`_

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
   :instructions: Add the content type of this configuration.

`BACK TO TOP <Configuration_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this configuration that may help you to find this instance more easily.

`BACK TO TOP <Configuration_>`_

------------

