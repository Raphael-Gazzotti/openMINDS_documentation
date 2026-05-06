###############
HardwareProduct
###############

:Semantic name: https://openminds.om-i.org/types/HardwareProduct

:Display as: Hardware product


------------

------------

Properties
##########

:Required: `contribution <contribution_heading_>`_, `name <name_heading_>`_, `scope <scope_heading_>`_, `type <type_heading_>`_
:Optional: `copyright <copyright_heading_>`_, `description <description_heading_>`_, `digitalIdentifier <digitalIdentifier_heading_>`_, `keyword <keyword_heading_>`_, `specification <specification_heading_>`_, `usageCondition <usageCondition_heading_>`_

------------

.. _contribution_heading:

************
contribution
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/contribution
   :value type: | linked object array \(1-N\) of type
                | `Organization <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/actors/person.html>`_
   :instructions: Add all relevant contributions (e.g., manufacturing, testing) for this hardware product.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _copyright_heading:

*********
copyright
*********

Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/copyright
   :value type: | embedded object of type
                | `Copyright <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/copyright.html>`_
   :instructions: Enter the copyright information of this hardware product.

`BACK TO TOP <HardwareProduct_>`_

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
   :instructions: Enter a short text describing this hardware product.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _digitalIdentifier_heading:

*****************
digitalIdentifier
*****************

Digital handle to identify objects or legal persons.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/digitalIdentifier
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Add the digital identifier for this hardware product.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _keyword_heading:

*******
keyword
*******

Significant word or concept that are representative of something or someone.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/keyword
   :value type: | linked object array \(1-N\) of type
                | `AccessChannel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessChannel.html>`_, `AccessEligibilityType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessEligibilityType.html>`_, `AccessForm <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessForm.html>`_, `AccessProcessType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/accessProcessType.html>`_, `ActionStatusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/actionStatusType.html>`_, `AgeCategory <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/ageCategory.html>`_, `AgeReference <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/ageReference.html>`_, `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/analysisTechnique.html>`_, `AnatomicalAxesOrientation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalAxesOrientation.html>`_, `AnatomicalCavity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalCavity.html>`_, `AnatomicalIdentificationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalIdentificationType.html>`_, `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/anatomicalPlane.html>`_, `AnnotationCriteriaType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/annotationCriteriaType.html>`_, `AnnotationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/annotationType.html>`_, `AtlasType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/atlasType.html>`_, `AuditoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/auditoryStimulusType.html>`_, `BiologicalOrder <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalOrder.html>`_, `BiologicalProcess <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalProcess.html>`_, `BiologicalSex <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/biologicalSex.html>`_, `BreedingType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/breedingType.html>`_, `CellCultureType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cellCultureType.html>`_, `CellType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cellType.html>`_, `ChemicalMixtureType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/chemicalMixtureType.html>`_, `Colormap <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/colormap.html>`_, `CommunicationInterfaceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/communicationInterfaceType.html>`_, `CommunicationProtocol <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/communicationProtocol.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/contributionType.html>`_, `CranialWindowConstructionType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cranialWindowConstructionType.html>`_, `CranialWindowReinforcementType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/cranialWindowReinforcementType.html>`_, `CriteriaQualityType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/criteriaQualityType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dataType.html>`_, `DependencyImpact <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dependencyImpact.html>`_, `DeploymentEnvironmentType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deploymentEnvironmentType.html>`_, `DeviceMountingType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deviceMountingType.html>`_, `DeviceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deviceType.html>`_, `DifferenceMeasure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/differenceMeasure.html>`_, `Disease <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/disease.html>`_, `DiseaseModel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/diseaseModel.html>`_, `EducationalLevel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/educationalLevel.html>`_, `ElectricalStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/electricalStimulusType.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/experimentalApproach.html>`_, `ExternalBodyRegion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/externalBodyRegion.html>`_, `FileBundleGrouping <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileBundleGrouping.html>`_, `FileRepositoryType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileRepositoryType.html>`_, `FileUsageRole <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/fileUsageRole.html>`_, `GeneticStrainType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/geneticStrainType.html>`_, `GustatoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/gustatoryStimulusType.html>`_, `Handedness <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/handedness.html>`_, `Language <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/language.html>`_, `Laterality <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/laterality.html>`_, `LearningResourceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/learningResourceType.html>`_, `MRIFatSuppressionTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIFatSuppressionTechnique.html>`_, `MRIParallelAcquisitionTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIParallelAcquisitionTechnique.html>`_, `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIPulseSequence.html>`_, `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_, `MRIWeighting <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIWeighting.html>`_, `MeasuredQuantity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/measuredQuantity.html>`_, `MeasuredSignalType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/measuredSignalType.html>`_, `MetaDataModelType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/metaDataModelType.html>`_, `ModelAbstractionLevel <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modelAbstractionLevel.html>`_, `ModelScope <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modelScope.html>`_, `ModificationConsentRequirement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConsentRequirement.html>`_, `ModificationConstraint <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationConstraint.html>`_, `ModificationForm <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationForm.html>`_, `ModificationScope <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/modificationScope.html>`_, `MolecularEntity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/molecularEntity.html>`_, `MuscularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/muscularStructure.html>`_, `NervousSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/nervousSystemStructure.html>`_, `OlfactoryStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/olfactoryStimulusType.html>`_, `OperatingDevice <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operatingDevice.html>`_, `OperatingSystem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operatingSystem.html>`_, `OperationalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operationalApproach.html>`_, `OpticalStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/opticalStimulusType.html>`_, `Organ <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organ.html>`_, `OrganSystemStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organSystemStructure.html>`_, `OrganismSubstance <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSubstance.html>`_, `OrganismSystem <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organismSystem.html>`_, `OrganizationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/organizationType.html>`_, `PatchClampVariation <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/patchClampVariation.html>`_, `PaymentModelType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/paymentModelType.html>`_, `PreparationType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/preparationType.html>`_, `ProgrammingLanguage <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/programmingLanguage.html>`_, `ProjectType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/projectType.html>`_, `PublicationStatus <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/publicationStatus.html>`_, `PulseShape <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/pulseShape.html>`_, `QualitativeOverlap <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/qualitativeOverlap.html>`_, `SemanticDataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/semanticDataType.html>`_, `SetupType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/setupType.html>`_, `SignalDirectionality <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/signalDirectionality.html>`_, `SkeletalStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/skeletalStructure.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareFeature.html>`_, `SovereignState <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/sovereignState.html>`_, `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/spatialEncoding.html>`_, `Species <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/species.html>`_, `StimulationApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/stimulationApproach.html>`_, `StimulationTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/stimulationTechnique.html>`_, `SubcellularEntity <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/subcellularEntity.html>`_, `SubjectAttribute <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/subjectAttribute.html>`_, `SupranationalBody <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/supranationalBody.html>`_, `TactileStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tactileStimulusType.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/technique.html>`_, `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/termSuggestion.html>`_, `Terminology <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/terminology.html>`_, `TissueSampleAttribute <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueSampleAttribute.html>`_, `TissueSampleType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueSampleType.html>`_, `TissueStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/tissueStructure.html>`_, `TypeOfUncertainty <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/typeOfUncertainty.html>`_, `UnitOfMeasurement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/unitOfMeasurement.html>`_, `VascularStructure <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/vascularStructure.html>`_, `VisualStimulusType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/visualStimulusType.html>`_ or `WeightType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/weightType.html>`_
   :instructions: Add all relevant keywords to this hardware product, either by adding controlled terms or by suggesting new terms.

`BACK TO TOP <HardwareProduct_>`_

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
   :instructions: Enter the model name for this hardware product defined by the manufacturer. In case of versioned models, the version identifier should be included in the name.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _scope_heading:

*****
scope
*****

Extent of something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/scope
   :value type: | linked object array \(1-N\) of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/analysisTechnique.html>`_, `ContributionType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/contributionType.html>`_, `DataType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/dataType.html>`_, `ExperimentalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/experimentalApproach.html>`_, `OperationalApproach <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/operationalApproach.html>`_, `SoftwareApplicationCategory <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareApplicationCategory.html>`_, `SoftwareFeature <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/softwareFeature.html>`_, `Technique <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/technique.html>`_ or `TermSuggestion <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/termSuggestion.html>`_
   :instructions: Add terms that describe what this hardware product does.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _specification_heading:

*************
specification
*************

Detailed and precise presentation of, or proposal for something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/specification
   :value type: | linked object of type
                | `PropertyValueList <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/research/propertyValueList.html>`_
   :instructions: Add the specification(s) of this hardware product as property value list.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/type
   :value type: | linked object of type
                | `DeviceType <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/deviceType.html>`_
   :instructions: Add the type of this hardware product.

`BACK TO TOP <HardwareProduct_>`_

------------

.. _usageCondition_heading:

**************
usageCondition
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usageCondition
   :value type: | linked object array \(1-N\) of type
                | `License <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/license.html>`_ or `UsageAgreement <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/core/data/usageAgreement.html>`_
   :instructions: Add all licenses and available usage agreements applicable to this hardware product.

`BACK TO TOP <HardwareProduct_>`_

------------

