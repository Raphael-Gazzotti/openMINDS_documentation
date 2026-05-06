#################
ServiceDeployment
#################

:Semantic name: https://openminds.om-i.org/types/ServiceDeployment

:Display as: Service deployment


------------

------------

Properties
##########

:Required: `name <name_heading_>`_, `provides <provides_heading_>`_, `service <service_heading_>`_, `startTime <startTime_heading_>`_
:Optional: `dependsOn <dependsOn_heading_>`_, `deploymentType <deploymentType_heading_>`_, `endTime <endTime_heading_>`_, `uses <uses_heading_>`_

------------

.. _dependsOn_heading:

*********
dependsOn
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dependsOn
   :value type: | linked object array \(1-N\) of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModelVersion.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/modelVersion.html>`_, `SoftwareVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/softwareVersion.html>`_, `AnatomicalAtlasVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/anatomicalAtlasVersion.html>`_ or `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_
   :instructions: Add the software version and any other relevant research product version that was deployed.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _deploymentType_heading:

**************
deploymentType
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/deploymentType
   :value type: | linked object of type
                | `DeploymentEnvironmentType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deploymentEnvironmentType.html>`_
   :instructions: Enter the type of deployment environment, for example, 'production' or 'integration'.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _endTime_heading:

*******
endTime
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/endTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time at which this deployment ended, formatted according to ISO-8601.

`BACK TO TOP <ServiceDeployment_>`_

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
   :instructions: Enter a label for this service deployment.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _provides_heading:

********
provides
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/provides
   :value type: | embedded object array \(1-N\) of type
                | `DeployedInterface <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/deployedInterface.html>`_
   :instructions: Add the interfaces that have been deployed.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/service
   :value type: | linked object of type
                | `Service <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/service.html>`_
   :instructions: Add the service that has been deployed.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _startTime_heading:

*********
startTime
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startTime
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the date and time at which this deployment was started, formatted according to ISO-8601.

`BACK TO TOP <ServiceDeployment_>`_

------------

.. _uses_heading:

****
uses
****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/uses
   :value type: | linked object array \(1-N\) of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_, `DatasetVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/datasetVersion.html>`_, `MetaDataModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/metaDataModelVersion.html>`_, `ModelVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/modelVersion.html>`_, `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_, `AnatomicalAtlasVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/anatomicalAtlasVersion.html>`_ or `CommonCoordinateFrameworkVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/commonCoordinateFrameworkVersion.html>`_
   :instructions: Add the deployed interfaces and any other relevant research product versions that are used by this deployment.

`BACK TO TOP <ServiceDeployment_>`_

------------

