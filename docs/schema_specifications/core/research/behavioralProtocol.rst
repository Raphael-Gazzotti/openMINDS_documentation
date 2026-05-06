##################
BehavioralProtocol
##################

:Semantic name: https://openminds.om-i.org/types/BehavioralProtocol

:Display as: Behavioral protocol

Structured information about a protocol used in an experiment studying human or animal behavior.


------------

------------

Properties
##########

:Required: `description <description_heading_>`_, `name <name_heading_>`_
:Optional: `describedIn <describedIn_heading_>`_, `internalIdentifier <internalIdentifier_heading_>`_, `stimulation <stimulation_heading_>`_, `stimulusType <stimulusType_heading_>`_

------------

.. _describedIn_heading:

***********
describedIn
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/describedIn
   :value type: | linked object array \(1-N\) of type
                | `DOI <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/digitalIdentifier/DOI.html>`_, `File <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/data/file.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add all sources in which this behavioral protocol is described in detail.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _description_heading:

***********
description
***********

Longer statement or account giving the characteristics of someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/description
   :value type: | string
                | formatting: text/markdown; multiline
   :instructions: Enter a description of this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _internalIdentifier_heading:

******************
internalIdentifier
******************

Term or code that identifies someone or something within a particular product.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/internalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

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
   :instructions: Enter a descriptive name for this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _stimulation_heading:

***********
stimulation
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/stimulation
   :value type: | linked object array \(1-N\) of type
                | `StimulationApproach <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/stimulationApproach.html>`_ or `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/stimulationTechnique.html>`_
   :instructions: Add all stimulation approaches and/or techniques used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

.. _stimulusType_heading:

************
stimulusType
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/stimulusType
   :value type: | linked object array \(1-N\) of type
                | `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/tactileStimulusType.html>`_ or `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/v4.0/schema_specifications/controlledTerms/visualStimulusType.html>`_
   :instructions: Add all stimulus types used within this behavioral protocol.

`BACK TO TOP <BehavioralProtocol_>`_

------------

