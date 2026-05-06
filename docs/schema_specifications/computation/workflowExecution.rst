#################
WorkflowExecution
#################

:Semantic name: https://openminds.om-i.org/types/WorkflowExecution

:Display as: Workflow execution

Structured information about an execution of a computational workflow.


------------

------------

Properties
##########

:Required: `stage <stage_heading_>`_
:Optional: `configuration <configuration_heading_>`_, `recipe <recipe_heading_>`_, `startedBy <startedBy_heading_>`_

------------

.. _configuration_heading:

*************
configuration
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/configuration
   :value type: | linked object of type
                | `Configuration <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/configuration.html>`_ or `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add the configuration information for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _recipe_heading:

******
recipe
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/recipe
   :value type: | linked object of type
                | `WorkflowRecipeVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/workflowRecipeVersion.html>`_
   :instructions: Add the workflow recipe version used for this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _stage_heading:

*****
stage
*****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/stage
   :value type: | linked object array \(1-N\) of type
                | `DataAnalysis <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/dataAnalysis.html>`_, `DataCopy <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/dataCopy.html>`_, `GenericComputation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/genericComputation.html>`_, `ModelValidation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/modelValidation.html>`_, `Optimization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/optimization.html>`_, `Simulation <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/simulation.html>`_ or `Visualization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/visualization.html>`_
   :instructions: Add all stages that were performed in this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

.. _startedBy_heading:

*********
startedBy
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/startedBy
   :value type: | linked object of type
                | `SoftwareAgent <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/computation/softwareAgent.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/person.html>`_
   :instructions: Add the agent that started this workflow execution.

`BACK TO TOP <WorkflowExecution_>`_

------------

