#######
Funding
#######

:Semantic name: https://openminds.ebrains.eu/core/Funding

:Display as: Funding

Structured information on used funding.


------------

------------

Properties
##########

:Required: `funder <funder_heading_>`_
:Optional: `acknowledgement <acknowledgement_heading_>`_, `awardNumber <awardNumber_heading_>`_, `awardTitle <awardTitle_heading_>`_

------------

.. _acknowledgement_heading:

***************
acknowledgement
***************

Official declaration or avowal of appreciation of an act or achievement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/acknowledgement
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the acknowledgement that should be used with this funding.

`BACK TO TOP <Funding_>`_

------------

.. _awardNumber_heading:

***********
awardNumber
***********

Machine-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/awardNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the associated award number of this funding.

`BACK TO TOP <Funding_>`_

------------

.. _awardTitle_heading:

**********
awardTitle
**********

Human-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/awardTitle
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the award title of this funding.

`BACK TO TOP <Funding_>`_

------------

.. _funder_heading:

******
funder
******

Legal person that provides money for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funder
   :value type: | linked object of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v1.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add the organization that provided this funding.

`BACK TO TOP <Funding_>`_

------------

