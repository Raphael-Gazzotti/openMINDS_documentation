###########
ServiceLink
###########

:Semantic name: https://openminds.om-i.org/types/ServiceLink

:Display as: Service link


------------

------------

Properties
##########

:Required: `dataLocation <dataLocation_heading_>`_, `openDataIn <openDataIn_heading_>`_, `service <service_heading_>`_
:Optional: `displayLabel <displayLabel_heading_>`_, `previewImage <previewImage_heading_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dataLocation
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/file.html>`_, `FileArchive <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/fileArchive.html>`_, `FileBundle <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/fileBundle.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/modelVersion.html>`_, `LivePaperResourceItem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/publications/livePaperResourceItem.html>`_ or `ParcellationEntityVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/SANDS/atlas/parcellationEntityVersion.html>`_
   :instructions: Add the location of the data that are linked to this specific service (e.g., stored as file (bundles) or registered as other entities such as atlas annotations).

`BACK TO TOP <ServiceLink_>`_

------------

.. _displayLabel_heading:

************
displayLabel
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/displayLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a display label for this service link.

`BACK TO TOP <ServiceLink_>`_

------------

.. _openDataIn_heading:

**********
openDataIn
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/openDataIn
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the internationalized resource identifier (IRI) to the linked data in the specified service.

`BACK TO TOP <ServiceLink_>`_

------------

.. _previewImage_heading:

************
previewImage
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/previewImage
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/file.html>`_
   :instructions: Add an image file to this service link that acts as a preview of its content or could function as an icon.

`BACK TO TOP <ServiceLink_>`_

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/service
   :value type: | linked object array \(1-N\) of type
                | `Interface <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/interface.html>`_, `InterfaceVersion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/products/interfaceVersion.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add all services in which the specified data can be opened by linking to each service’s interface (group of versions), specific interface version, or web resource.

`BACK TO TOP <ServiceLink_>`_

------------

