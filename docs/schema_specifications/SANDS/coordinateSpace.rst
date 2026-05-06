###############
CoordinateSpace
###############

:Semantic name: https://openminds.ebrains.eu/sands/CoordinateSpace

:Display as: Coordinate space

Structured information on a coordinate space.


------------

------------

Properties
##########

:Required: `anatomicalAxesOrientation <anatomicalAxesOrientation_heading_>`_, `axesOrigin <axesOrigin_heading_>`_, `fullName <fullName_heading_>`_, `nativeUnit <nativeUnit_heading_>`_, `releaseDate <releaseDate_heading_>`_, `shortName <shortName_heading_>`_, `versionIdentifier <versionIdentifier_heading_>`_
:Optional: `defaultImage <defaultImage_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `homepage <homepage_heading_>`_, `ontologyIdentifier <ontologyIdentifier_heading_>`_

------------

.. _anatomicalAxesOrientation_heading:

*************************
anatomicalAxesOrientation
*************************

Relation between reference planes used in anatomy and mathematics.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/anatomicalAxesOrientation
   :value type: | linked object of type
                | `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_
   :instructions: Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ).

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _axesOrigin_heading:

**********
axesOrigin
**********

Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/axesOrigin
   :value type: | linked object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the origin of the coordinate system (central point where axes intersect; 2D: [x, y] or 3D:[x, y, z]).

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _defaultImage_heading:

************
defaultImage
************

Two or three dimensional image that particluarly represents a specific coordinate space.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/defaultImage
   :value type: | linked object array \(1-N\) of type
                | `Image <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/image.html>`_
   :instructions: Add one or several images used as visual representation of this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/digitalIdentifier
   :value type: | linked object of type
                | DigitalIdentifier \[TYPE_ERROR\]
   :instructions: Add the globally unique and persistent digital identifier of this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive full name for this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _homepage_heading:

********
homepage
********

Main website of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/homepage
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the homepage of this brain atlas.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _nativeUnit_heading:

**********
nativeUnit
**********

Determinate quantity used in the original measurement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/nativeUnit
   :value type: | linked object of type
                | `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_
   :instructions: Add the native unit that is used for this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _ontologyIdentifier_heading:

******************
ontologyIdentifier
******************

Term or code used to identify something or someone registered within a particular ontology.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/ontologyIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (IRI) of the related ontological term matching this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _releaseDate_heading:

***********
releaseDate
***********

Fixed date on which a product is due to become or was made available for the general public to see or buy

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/releaseDate
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date of first publication of this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a descriptive short name for this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

.. _versionIdentifier_heading:

*****************
versionIdentifier
*****************

Term or code used to identify the version of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/versionIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the version identifier of this coordinate space.

`BACK TO TOP <CoordinateSpace_>`_

------------

