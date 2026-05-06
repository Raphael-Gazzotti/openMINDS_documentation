#################
GenericIdentifier
#################

:Semantic name: https://openminds.om-i.org/types/GenericIdentifier

:Display as: Generic identifier


------------

------------

Properties
##########

:Required: `emitter <emitter_heading_>`_, `identifier <identifier_heading_>`_
:Optional: `type <type_heading_>`_

------------

.. _emitter_heading:

*******
emitter
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/emitter
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/actors/organization.html>`_
   :instructions: Add the organization that governs and/or emits the identifier.

`BACK TO TOP <GenericIdentifier_>`_

------------

.. _identifier_heading:

**********
identifier
**********

Term or code used to identify something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/identifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a persistent, unique identifier emitted by an organization.

`BACK TO TOP <GenericIdentifier_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the type of identifier, e.g. 'PubMed ID'.

`BACK TO TOP <GenericIdentifier_>`_

------------

