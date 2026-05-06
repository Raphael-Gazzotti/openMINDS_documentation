###########
Affiliation
###########

:Semantic name: https://openminds.ebrains.eu/core/Affiliation

:Display as: Affiliation

Structured information about a relationship between two entities, such as a person and their employer.


------------

------------

Properties
##########

:Required: `organization <organization_heading_>`_
:Optional: `endDate <endDate_heading_>`_, `startDate <startDate_heading_>`_

------------

.. _endDate_heading:

*******
endDate
*******

Date in the Gregorian calendar at which something terminates in time.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/endDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the end date of this affiliation. Leave blank if the affiliation is still current.

`BACK TO TOP <Affiliation_>`_

------------

.. _organization_heading:

************
organization
************

Legally accountable, administrative and functional structure.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/organization
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add organization to which a person is or was affiliated.

`BACK TO TOP <Affiliation_>`_

------------

.. _startDate_heading:

*********
startDate
*********

Date in the Gregorian calendar at which something begins in time

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/startDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the start date of this affiliation.

`BACK TO TOP <Affiliation_>`_

------------

