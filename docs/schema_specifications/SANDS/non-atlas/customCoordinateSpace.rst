#####################
CustomCoordinateSpace
#####################

:Semantic name: https://openminds.om-i.org/types/CustomCoordinateSpace

:Display as: Custom coordinate space


------------

------------

Properties
##########

:Required: `anatomicalAxesOrientation <anatomicalAxesOrientation_heading_>`_, `axesOrigin <axesOrigin_heading_>`_, `name <name_heading_>`_, `nativeUnit <nativeUnit_heading_>`_
:Optional: `defaultImage <defaultImage_heading_>`_

------------

.. _anatomicalAxesOrientation_heading:

*************************
anatomicalAxesOrientation
*************************

Relation between reference planes used in anatomy and mathematics.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anatomicalAxesOrientation
   :value type: | linked object of type
                | `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_
   :instructions: Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this custom coordinate space.

`BACK TO TOP <CustomCoordinateSpace_>`_

------------

.. _axesOrigin_heading:

**********
axesOrigin
**********

Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/axesOrigin
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the origin (central point where all axes intersect) of this custom coordinate space for two-dimensional spaces as [x, y] or for three-dimensional space as [x, y, z].

`BACK TO TOP <CustomCoordinateSpace_>`_

------------

.. _defaultImage_heading:

************
defaultImage
************

Two or three dimensional image that particluarly represents a specific coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/defaultImage
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_
   :instructions: Add all image files used as visual representation of this custom coordinate space.

`BACK TO TOP <CustomCoordinateSpace_>`_

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
   :instructions: Enter a descriptive name for this custom coordinate space.

`BACK TO TOP <CustomCoordinateSpace_>`_

------------

.. _nativeUnit_heading:

**********
nativeUnit
**********

Determinate quantity used in the original measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/nativeUnit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the native unit that is used for this custom coordinate space.

`BACK TO TOP <CustomCoordinateSpace_>`_

------------

