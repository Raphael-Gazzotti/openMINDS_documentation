##########
Periodical
##########

:Semantic name: https://openminds.om-i.org/types/Periodical

:Display as: Periodical


------------

------------

Properties
##########

:Required: `name <name_heading_>`_
:Optional: `abbreviation <abbreviation_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_

------------

.. _abbreviation_heading:

************
abbreviation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/abbreviation
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the official (or most commonly used) abbreviation of the periodical (e.g., J. Physiol).

`BACK TO TOP <Periodical_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | linked object of type
                | `ISSN <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/digitalIdentifier/ISSN.html>`_
   :instructions: Add the globally unique and persistent digital identifier of this periodical.

`BACK TO TOP <Periodical_>`_

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
   :instructions: Enter the name (or title) of this periodical (e.g., Journal of Physiology).

`BACK TO TOP <Periodical_>`_

------------

