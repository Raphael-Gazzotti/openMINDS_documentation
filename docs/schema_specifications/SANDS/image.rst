#####
Image
#####

:Semantic name: https://openminds.ebrains.eu/sands/Image

:Display as: Image

Structured information on an image.


------------

------------

Properties
##########

:Required: `coordinateSpace <coordinateSpace_heading_>`_, `definedIn <definedIn_heading_>`_, `voxelSize <voxelSize_heading_>`_
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
                | `CoordinateSpace <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/SANDS/coordinateSpace.html>`_
   :instructions: Add the coordinate space this image exists in.

`BACK TO TOP <Image_>`_

------------

.. _definedIn_heading:

*********
definedIn
*********

Reference to a file instance in which something is stored.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/definedIn
   :value type: | linked object of type
                | FileInstance \[TYPE_ERROR\]
   :instructions: Add the file in which this image is stored in.

`BACK TO TOP <Image_>`_

------------

.. _voxelSize_heading:

*********
voxelSize
*********

Extent of the discrete elements comprising a three-dimensional entity.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/voxelSize
   :value type: | embedded object array \(2-3\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Add two or three values with units defined that describe the size of one pixel (2D: [x, y]) or voxel (3D: [x, y, z]) in the physical space.

`BACK TO TOP <Image_>`_

------------

