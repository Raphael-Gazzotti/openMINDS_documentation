########
Location
########

:Semantic name: https://openminds.om-i.org/types/Location

:Display as: Location


------------

------------

Properties
##########

:Required: `country <country_heading_>`_
:Optional: `address <address_heading_>`_, `geoCoordinates <geoCoordinates_heading_>`_

------------

.. _address_heading:

*******
address
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/address
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the address of the location, in the format [Street address], City, [Region/State], [Postal code]. The minimum requested information is City.

`BACK TO TOP <Location_>`_

------------

.. _country_heading:

*******
country
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/country
   :value type: | linked object of type
                | `SovereignState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/sovereignState.html>`_
   :instructions: Enter the country in which the location is found.

`BACK TO TOP <Location_>`_

------------

.. _geoCoordinates_heading:

**************
geoCoordinates
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/geoCoordinates
   :value type: | embedded object of type
                | `GeoCoordinates <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/geoCoordinates.html>`_
   :instructions: Enter the geographic coordinates of the location.

`BACK TO TOP <Location_>`_

------------

