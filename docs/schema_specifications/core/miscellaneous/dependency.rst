##########
Dependency
##########

:Semantic name: https://openminds.om-i.org/types/Dependency

:Display as: Dependency


------------

------------

Properties
##########

:Required: `fulfilledBy <fulfilledBy_heading_>`_
:Optional: `failureImpact <failureImpact_heading_>`_

------------

.. _failureImpact_heading:

*************
failureImpact
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/failureImpact
   :value type: | linked object array \(1-N\) of type
                | `DependencyImpact <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/dependencyImpact.html>`_
   :instructions: Add the impacts that failure of this dependency would have.

`BACK TO TOP <Dependency_>`_

------------

.. _fulfilledBy_heading:

***********
fulfilledBy
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fulfilledBy
   :value type: | linked object of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/configuration.html>`_, `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_, `InterfaceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/interfaceVersion.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/softwareVersion.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Enter the resource that fulfils this dependency.

`BACK TO TOP <Dependency_>`_

------------

