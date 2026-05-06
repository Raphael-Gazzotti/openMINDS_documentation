###################
LaunchConfiguration
###################

:Semantic name: https://openminds.om-i.org/types/LaunchConfiguration

:Display as: Launch configuration

Structured information about the launch of a computational process.


------------

------------

Properties
##########

:Required: `executable <executable_heading_>`_
:Optional: `argument <argument_heading_>`_, `description <description_heading_>`_, `environmentVariable <environmentVariable_heading_>`_, `name <name_heading_>`_

------------

.. _argument_heading:

********
argument
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/argument
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all command line arguments for this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

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
   :instructions: Enter a short text describing this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

.. _environmentVariable_heading:

*******************
environmentVariable
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/environmentVariable
   :value type: | linked object of type
                | `PropertyValueList <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/research/propertyValueList.html>`_
   :instructions: Add any environment variables defined by this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

.. _executable_heading:

**********
executable
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/executable
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the path to the command-line executable.

`BACK TO TOP <LaunchConfiguration_>`_

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
   :instructions: Enter a descriptive name for this launch configuration.

`BACK TO TOP <LaunchConfiguration_>`_

------------

