#############
Accessibility
#############

:Semantic name: https://openminds.om-i.org/types/Accessibility

:Display as: Accessibility


For this schema openMINDS provides a `library of instances <https://openminds-documentation.readthedocs.io/en/latest/instance_libraries/accessibilities.html>`_.

------------

------------

Properties
##########

:Required: `channel <channel_heading_>`_, `eligibility <eligibility_heading_>`_, `form <form_heading_>`_, `paymentModel <paymentModel_heading_>`_, `process <process_heading_>`_
:Optional:

------------

.. _channel_heading:

*******
channel
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/channel
   :value type: | linked object of type
                | `AccessChannel <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessChannel.html>`_
   :instructions: Add the relevant access channel indicating where access takes place (physical, virtual, or hybrid).

`BACK TO TOP <Accessibility_>`_

------------

.. _eligibility_heading:

***********
eligibility
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/eligibility
   :value type: | linked object of type
                | `AccessEligibilityType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessEligibilityType.html>`_
   :instructions: Add the relevant access eligibility type indicating who is allowed to access (open, controlled, or restricted).

`BACK TO TOP <Accessibility_>`_

------------

.. _form_heading:

****
form
****

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/form
   :value type: | linked object of type
                | `AccessForm <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessForm.html>`_
   :instructions: Add the relevant access form indicating whether the user interacts directly or through mediation.

`BACK TO TOP <Accessibility_>`_

------------

.. _paymentModel_heading:

************
paymentModel
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/paymentModel
   :value type: | linked object array \(1-N\) of type
                | `PaymentModelType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/paymentModelType.html>`_
   :instructions: Add all relevant payment model types indicating how access costs are determined. If no payment is requires, select zero-cost payment model.

`BACK TO TOP <Accessibility_>`_

------------

.. _process_heading:

*******
process
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/process
   :value type: | linked object of type
                | `AccessProcessType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/accessProcessType.html>`_
   :instructions: Add the relevant access process type indicating how access is granted (immediate, registered, authenticated, or authorized).

`BACK TO TOP <Accessibility_>`_

------------

