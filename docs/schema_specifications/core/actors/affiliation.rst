###########
Affiliation
###########

:Semantic name: https://openminds.om-i.org/types/Affiliation

:Display as: Affiliation

Structured information about a relationship between two entities, such as a person and their employer.


------------

------------

Properties
##########

:Required: `organization <organization_heading_>`_, `person <person_heading_>`_
:Optional:

------------

.. _organization_heading:

************
organization
************

Legally accountable, administrative and functional structure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/organization
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add all organizations (in display order) with which the specified individual is affiliated.

`BACK TO TOP <Affiliation_>`_

------------

.. _person_heading:

******
person
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/person
   :value type: | linked object of type
                | `Person <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the individual to whom this affiliation belongs.

`BACK TO TOP <Affiliation_>`_

------------

