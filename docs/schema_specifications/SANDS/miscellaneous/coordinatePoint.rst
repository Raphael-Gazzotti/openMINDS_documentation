###############
CoordinatePoint
###############

:Semantic name: https://openminds.ebrains.eu/sands/CoordinatePoint

:Display as: Coordinate point


------------

------------

Properties
##########

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `coordinates <coordinates_heading_>`_
:Optional:

------------

.. _coordinateSpace_heading:

***************
coordinateSpace
***************

Two or three dimensional geometric setting.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinateSpace
   :value type: | linked object of type
                | `CommonCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/atlas/commonCoordinateSpace.html>`_ or `CustomCoordinateSpace <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/SANDS/non-atlas/customCoordinateSpace.html>`_
   :instructions: Add the coordinate space in which this coordinate point exists in.

`BACK TO TOP <CoordinatePoint_>`_

------------

.. _coordinates_heading:

***********
coordinates
***********

Pair or triplet of numbers defining a location in a given coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/coordinates
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v2.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Add two or three coordinates (2D: [x, y] or 3D: [x, y, z]) that define the exact location of this point in the stated coordinate space.

`BACK TO TOP <CoordinatePoint_>`_

------------

