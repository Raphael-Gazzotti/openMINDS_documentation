###########
ServiceLink
###########

:Semantic name: https://openminds.ebrains.eu/core/ServiceLink

:Display as: Service link


------------

------------

Properties
##########

:Required: `dataLocation <dataLocation_heading_>`_, `openDataIn <openDataIn_heading_>`_, `service <service_heading_>`_
:Optional: `name <name_heading_>`_

------------

.. _dataLocation_heading:

************
dataLocation
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/dataLocation
   :value type: | linked object of type
                | `File <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add the file or file bundle with the data that are linked to the specified service.

`BACK TO TOP <ServiceLink_>`_

------------

.. _name_heading:

****
name
****

Word or phrase that constitutes the distinctive designation of a being or thing.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/name
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a name that should be used as preferred display label for this service link.

`BACK TO TOP <ServiceLink_>`_

------------

.. _openDataIn_heading:

**********
openDataIn
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/openDataIn
   :value type: | linked object of type
                | `URL <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/miscellaneous/URL.html>`_
   :instructions: Add the uniform resource locator (URL) to open the linked data in the specified service.

`BACK TO TOP <ServiceLink_>`_

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/service
   :value type: | linked object of type
                | Service \[TYPE_ERROR\]
   :instructions: Add the service in which the specified data can be opened.

`BACK TO TOP <ServiceLink_>`_

------------

