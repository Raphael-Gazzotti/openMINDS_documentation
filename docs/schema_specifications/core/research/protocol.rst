########
Protocol
########

:Semantic name: https://openminds.ebrains.eu/core/Protocol

:Display as: Protocol

Structured information on a research project.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_, `technique <technique_heading_>`_
:Optional: `studyOption <studyOption_heading_>`_

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
   :instructions: Enter a description of this protocol.

`BACK TO TOP <Protocol_>`_

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
   :instructions: Enter a descriptive name for this protocol.

`BACK TO TOP <Protocol_>`_

------------

.. _studyOption_heading:

***********
studyOption
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/studyOption
   :value type: | linked object array \(1-N\) of type
                | undefined
   :instructions: Add all study options this protocol offers.

`BACK TO TOP <Protocol_>`_

------------

.. _technique_heading:

*********
technique
*********

Method of accomplishing a desired aim.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/technique
   :value type: | linked object array \(1-N\) of type
                | `Technique <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/technique.html>`_
   :instructions: Add all techniques that were used in this protocol.

`BACK TO TOP <Protocol_>`_

------------

