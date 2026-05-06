############
ParameterSet
############

:Semantic name: https://openminds.ebrains.eu/core/ParameterSet

:Display as: Parameter set

Structured information on a used parameter set.


------------

------------

Properties
##########

:Required: `context <context_heading_>`_, `parameter <parameter_heading_>`_, `relevantFor <relevantFor_heading_>`_
:Optional:

------------

.. _context_heading:

*******
context
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/context
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the common context for the parameters grouped in this set.

`BACK TO TOP <ParameterSet_>`_

------------

.. _parameter_heading:

*********
parameter
*********

Digital or physical property determining a particular function, characteristic or behavior of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/parameter
   :value type: | embedded object array \(1-N\) of type
                | `NumericalParameter <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/numericalParameter.html>`_ or `StringParameter <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/stringParameter.html>`_
   :instructions: Add all numerical and string parameters that belong to this parameter set.

`BACK TO TOP <ParameterSet_>`_

------------

.. _relevantFor_heading:

***********
relevantFor
***********

Reference to what or whom something or someone bears significance.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/relevantFor
   :value type: | linked object of type
                | `BehavioralTask <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/research/behavioralTask.html>`_ or `Technique <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/controlledTerms/technique.html>`_
   :instructions: Add the technique or behavioral task where this set of parameters is used in.

`BACK TO TOP <ParameterSet_>`_

------------

