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
:Optional:

------------

.. _holder_heading:

******
holder
******

Legal person in possession of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/holder
   :value type: | linked object array \(1-N\) of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/actors/person.html>`_
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
   :instructions: Enter the year during which the copyright was first asserted and, optionally, later years during which updated versions were published.

`BACK TO TOP <Copyright_>`_

------------

