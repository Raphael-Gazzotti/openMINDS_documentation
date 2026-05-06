##############
UsageAgreement
##############

:Semantic name: https://openminds.om-i.org/types/UsageAgreement

:Display as: Usage agreement


------------

------------

Properties
##########

:Required: `authoringParty <authoringParty_heading_>`_, `fullName <fullName_heading_>`_, `jurisdiction <jurisdiction_heading_>`_, `modificationProfile <modificationProfile_heading_>`_, `shortName <shortName_heading_>`_, `template <template_heading_>`_
:Optional: `source <source_heading_>`_, `supportChannel <supportChannel_heading_>`_

------------

.. _authoringParty_heading:

**************
authoringParty
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/authoringParty
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all natural persons and legal entities (in display order) responsible for creating and establishing this usage agreement.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _fullName_heading:

********
fullName
********

Whole, non-abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fullName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the full name of this usage agreement.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _jurisdiction_heading:

************
jurisdiction
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/jurisdiction
   :value type: | linked object of type
                | `SovereignState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/sovereignState.html>`_ or `SupranationalBody <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/supranationalBody.html>`_
   :instructions: Enter the jurisdiction in which this usage agreement was issued.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _modificationProfile_heading:

*******************
modificationProfile
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/modificationProfile
   :value type: | linked object array \(1-N\) of type
                | `ModificationConsentRequirement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConsentRequirement.html>`_, `ModificationConstraint <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConstraint.html>`_, `ModificationForm <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationForm.html>`_ or `ModificationScope <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationScope.html>`_
   :instructions: Add all the types of modifications that are allowed under this usage agreement.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _shortName_heading:

*********
shortName
*********

Shortened or fully abbreviated name of something or somebody.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/shortName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a short name (or alias) for this usage agreement that could be used as a shortened display title (e.g., for web services with too little space to display the full name).

`BACK TO TOP <UsageAgreement_>`_

------------

.. _source_heading:

******
source
******

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/source
   :value type: | linked object array \(1-N\) of type
                | `License <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/license.html>`_ or `UsageAgreement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/usageAgreement.html>`_
   :instructions: Add all licenses or usage agreements that served as references in the creation of this usage agreement.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _supportChannel_heading:

**************
supportChannel
**************

Way of communication used to interact with users or customers.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/supportChannel
   :value type: | string array \(1-N\)
                | formatting: text/plain; singleline
   :instructions: Enter all channels through which users can obtain support and initiate negotiations regarding this usage agreement with the authoring party.

`BACK TO TOP <UsageAgreement_>`_

------------

.. _template_heading:

********
template
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/template
   :value type: | linked object of type
                | `WebResource <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the web resource that supplies the template for this usage agreement.

`BACK TO TOP <UsageAgreement_>`_

------------

