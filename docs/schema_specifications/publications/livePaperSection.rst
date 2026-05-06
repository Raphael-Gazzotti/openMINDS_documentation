################
LivePaperSection
################

:Semantic name: https://openminds.om-i.org/types/LivePaperSection

:Display as: Live paper section


------------

------------

Properties
##########

:Required: `isPartOf <isPartOf_heading_>`_, `name <name_heading_>`_, `order <order_heading_>`_, `type <type_heading_>`_
:Optional: `description <description_heading_>`_

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
   :instructions: Enter a description of this live paper section.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/isPartOf
   :value type: | linked object of type
                | `LivePaperVersion <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/publications/livePaperVersion.html>`_
   :instructions: Add the live paper version this live paper section is part of.

`BACK TO TOP <LivePaperSection_>`_

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
   :instructions: Enter the name (or title) of this live paper section.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _order_heading:

*****
order
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/order
   :value type: integer
   :instructions: Enter an integer that is used to sort this live paper section in ascending order with other live paper sections of the overarching live paper version.

`BACK TO TOP <LivePaperSection_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Add the type of this live paper section (e.g., 'custom', 'generic', 'models', 'morphology', or 'traces').

`BACK TO TOP <LivePaperSection_>`_

------------

