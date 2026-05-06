###################
ViewerSpecification
###################

:Semantic name: https://openminds.om-i.org/types/ViewerSpecification

:Display as: Viewer specification


------------

------------

Properties
##########

:Required: `anchorPoint <anchorPoint_heading_>`_
:Optional: `additionalRemarks <additionalRemarks_heading_>`_, `cameraPosition <cameraPosition_heading_>`_, `preferredDisplayColor <preferredDisplayColor_heading_>`_

------------

.. _additionalRemarks_heading:

*****************
additionalRemarks
*****************

Mention of what deserves additional attention or notice.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/additionalRemarks
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter any additional remarks concerning this viewer specification.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _anchorPoint_heading:

***********
anchorPoint
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/anchorPoint
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the coordinates of the anchor point that a viewer should use. Either state the anchor point of the annotation again or state another coordinate point.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _cameraPosition_heading:

**************
cameraPosition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/cameraPosition
   :value type: | embedded object of type
                | `CoordinatePoint <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/coordinatePoint.html>`_
   :instructions: Enter the camera position that a viewer should use.

`BACK TO TOP <ViewerSpecification_>`_

------------

.. _preferredDisplayColor_heading:

*********************
preferredDisplayColor
*********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/preferredDisplayColor
   :value type: | linked object of type
                | `Colormap <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/colormap.html>`_ or `SingleColor <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/SANDS/miscellaneous/singleColor.html>`_
   :instructions: Add the preferred color that a viewer should display.

`BACK TO TOP <ViewerSpecification_>`_

------------

