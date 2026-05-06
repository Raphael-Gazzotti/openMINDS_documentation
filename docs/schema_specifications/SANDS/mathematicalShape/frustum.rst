#######
Frustum
#######

:Semantic name: https://openminds.om-i.org/types/Frustum

:Display as: Frustum


------------

------------

Properties
##########

:Required: `baseDistance <baseDistance_heading_>`_, `majorBaseShape <majorBaseShape_heading_>`_, `minorBaseScale <minorBaseScale_heading_>`_
:Optional:

------------

.. _baseDistance_heading:

************
baseDistance
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/baseDistance
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the perpendicular distance between the centered major and minor base planes of this frustum.

`BACK TO TOP <Frustum_>`_

------------

.. _majorBaseShape_heading:

**************
majorBaseShape
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/majorBaseShape
   :value type: | embedded object of type
                | `Circle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/circle.html>`_, `CircularSector <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/circularSector.html>`_, `Ellipse <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/ellipse.html>`_, `EquilateralTriangle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/equilateralTriangle.html>`_, `IsoscelesTriangle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/isoscelesTriangle.html>`_, `Kite <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/kite.html>`_, `Parallelogram <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/parallelogram.html>`_, `Rectangle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/rectangle.html>`_, `RegularPolygon <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/regularPolygon.html>`_, `Rhombus <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/rhombus.html>`_, `RightTriangle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/rightTriangle.html>`_, `Square <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/square.html>`_, `Trapezoid <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/trapezoid.html>`_ or `Triangle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/mathematicalShape/triangle.html>`_
   :instructions: Enter the major two-dimensional base shape of this frustum.

`BACK TO TOP <Frustum_>`_

------------

.. _minorBaseScale_heading:

**************
minorBaseScale
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/minorBaseScale
   :value type: number
   :instructions: Enter the ratio of the smaller to the larger base size of this frustum.

`BACK TO TOP <Frustum_>`_

------------

