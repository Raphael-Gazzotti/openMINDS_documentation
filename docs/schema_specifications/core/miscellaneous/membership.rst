##########
Membership
##########

:Semantic name: https://openminds.om-i.org/types/Membership

:Display as: Membership


------------

------------

Properties
##########

:Required: `member <member_heading_>`_
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
   :instructions: Enter the end date of this membership, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <Membership_>`_

------------

.. _member_heading:

******
member
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/member
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the actor associated with this membership.

`BACK TO TOP <Membership_>`_

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
   :instructions: Enter the start date of this membership, formatted as 'YYYY-MM-DD'.

`BACK TO TOP <Membership_>`_

------------

