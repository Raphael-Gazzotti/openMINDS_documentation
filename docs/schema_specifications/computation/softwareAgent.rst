#############
SoftwareAgent
#############

:Semantic name: https://openminds.om-i.org/types/SoftwareAgent

:Display as: Software agent

Structured information about a piece of software or web service that can perform a task autonomously.


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `software <software_heading_>`_
:Optional: `environment <environment_heading_>`_

------------

.. _environment_heading:

***********
environment
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/environment
   :value type: | linked object of type
                | `Environment <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/computation/environment.html>`_
   :instructions: Add the computational environment in which this software agent was running.

`BACK TO TOP <SoftwareAgent_>`_

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
   :instructions: Enter a descriptive name for this software agent.

`BACK TO TOP <SoftwareAgent_>`_

------------

.. _software_heading:

********
software
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/software
   :value type: | linked object of type
                | `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/products/softwareVersion.html>`_
   :instructions: Add the software version that is being run as this software agent.

`BACK TO TOP <SoftwareAgent_>`_

------------

