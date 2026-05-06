###############
CoordinatePoint
###############

:Semantic name: https://openminds.om-i.org/types/CoordinatePoint

:Display as: Coordinate point


------------

------------

Properties
##########

:Required: `coordinateFramework <coordinateFramework_heading_>`_, `coordinates <coordinates_heading_>`_
:Optional:

------------

.. _coordinateFramework_heading:

*******************
coordinateFramework
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/coordinateFramework
   :value type: | linked object of type
                | `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_ or `CustomCoordinateFramework <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/non-atlas/customCoordinateFramework.html>`_
   :instructions: Add the coordinate framework in which this coordinate point exists in.

`BACK TO TOP <CoordinatePoint_>`_

------------

.. _coordinates_heading:

***********
coordinates
***********

Pair or triplet of numbers defining a location in a given coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/coordinates
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the coordinates of this point within the stated coordinate space for two-dimensonal spaces as [x, y] or for three-dimensional space as [x, y, z].

`BACK TO TOP <CoordinatePoint_>`_

------------

