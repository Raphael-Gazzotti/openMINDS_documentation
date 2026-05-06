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

:Required: `memberOf <memberOf_heading_>`_
:Optional: `endDate <endDate_heading_>`_, `startDate <startDate_heading_>`_

------------

.. _endDate_heading:

*******
endDate
*******

Date in the Gregorian calendar at which something terminates in time.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/endDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the end date of this affiliation, formatted as 'YYYY-MM-DD'. Leave blank if this affiliation is still current.

`BACK TO TOP <Affiliation_>`_

------------

.. _memberOf_heading:

********
memberOf
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/memberOf
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_ or `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the organization or consortium another party was or still is a member of.

`BACK TO TOP <Affiliation_>`_

------------

.. _startDate_heading:

*********
startDate
*********

Date in the Gregorian calendar at which something begins in time

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the start date of this affiliation, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <Affiliation_>`_

------------

