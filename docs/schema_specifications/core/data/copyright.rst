#########
Copyright
#########

:Semantic name: https://openminds.om-i.org/types/Copyright

:Display as: Copyright

Structured information on the copyright.


------------

------------

Properties
##########

:Required: `holder <holder_heading_>`_, `year <year_heading_>`_
:Optional: `customUsageClause <customUsageClause_heading_>`_

------------

.. _customUsageClause_heading:

*****************
customUsageClause
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/customUsageClause
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a statement describing the usage rights, such as 'All rights reserved.'.

`BACK TO TOP <Copyright_>`_

------------

.. _holder_heading:

******
holder
******

Legal person in possession of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/holder
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all parties that hold this copyright.

`BACK TO TOP <Copyright_>`_

------------

.. _year_heading:

****
year
****

Cycle in the Gregorian calendar specified by a number and comprised of 365 or 366 days divided into 12 months beginning with January and ending with December.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/year
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter the year when the copyright was first asserted, and optionally any subsequent years when the copyright holder and/or the rights-reservation clause was updated.

`BACK TO TOP <Copyright_>`_

------------

