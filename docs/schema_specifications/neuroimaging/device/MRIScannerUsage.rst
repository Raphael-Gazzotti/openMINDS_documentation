###############
MRIScannerUsage
###############

:Semantic name: https://openminds.om-i.org/types/MRIScannerUsage

:Display as: Mriscanner usage


------------

------------

Properties
##########

:Required: `device <device_heading_>`_, `echoTime <echoTime_heading_>`_, `repetitionTime <repetitionTime_heading_>`_, `sliceTiming <sliceTiming_heading_>`_
:Optional: `MRIWeighting <MRIWeighting_heading_>`_, `MTPulseShape <MTPulseShape_heading_>`_, `accelerationFactor <accelerationFactor_heading_>`_, `diffusionEncodingParameters <diffusionEncodingParameters_heading_>`_, `dwellTime <dwellTime_heading_>`_, `fatSuppressionTechnique <fatSuppressionTechnique_heading_>`_, `fieldOfView <fieldOfView_heading_>`_, `flipAngle <flipAngle_heading_>`_, `gradientCorrection <gradientCorrection_heading_>`_, `inversionTime <inversionTime_heading_>`_, `lookupLabel <lookupLabel_heading_>`_, `matrixSize <matrixSize_heading_>`_, `metadataLocation <metadataLocation_heading_>`_, `numberOfDiscardedVolumes <numberOfDiscardedVolumes_heading_>`_, `numberOfExcitations <numberOfExcitations_heading_>`_, `numberOfSlices <numberOfSlices_heading_>`_, `parallelAcquisitionTechnique <parallelAcquisitionTechnique_heading_>`_, `phaseEncodingDirection <phaseEncodingDirection_heading_>`_, `receiverBandwidth <receiverBandwidth_heading_>`_, `sliceAngulation <sliceAngulation_heading_>`_, `sliceGap <sliceGap_heading_>`_, `sliceOrientation <sliceOrientation_heading_>`_, `sliceThickness <sliceThickness_heading_>`_, `spatialEncoding <spatialEncoding_heading_>`_, `spoilingTechnique <spoilingTechnique_heading_>`_, `totalReadOutTime <totalReadOutTime_heading_>`_, `transmitterBandwidth <transmitterBandwidth_heading_>`_, `usedCoils <usedCoils_heading_>`_, `usedSpecimen <usedSpecimen_heading_>`_, `voxelSize <voxelSize_heading_>`_

------------

.. _MRIWeighting_heading:

************
MRIWeighting
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/MRIWeighting
   :value type: | linked object of type
                | `MRIWeighting <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIWeighting.html>`_
   :instructions: Add the magnetic resonance imaging weighting type describing the dominant source of image contrast. This designation reflects the contrast determined by repetition time, echo time, and inversion time and can be identified from the sequence protocol.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _MTPulseShape_heading:

************
MTPulseShape
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/MTPulseShape
   :value type: | linked object of type
                | `PulseShape <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/pulseShape.html>`_
   :instructions: Add the shape of the magnetization transfer (MT) radiofrequency (RF) pulse waveform used in this acquisition. This information is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _accelerationFactor_heading:

******************
accelerationFactor
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/accelerationFactor
   :value type: integer
   :instructions: Enter the acceleration factor (R), defined as the ratio of fully sampled to reduced k-space acquisition, with R ≥ 1 and R = 1 indicating no acceleration. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _diffusionEncodingParameters_heading:

***************************
diffusionEncodingParameters
***************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/diffusionEncodingParameters
   :value type: | linked object array \(2-2\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_
   :instructions: Add two diffusion encoding files: a b-value file specifying the diffusion weighting for each acquired volume and a b-vector file specifying the corresponding three-dimensional diffusion gradient directions. Ensure that both files are correctly ordered, that b-vectors are normalized, and that they are aligned with the image volumes.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _dwellTime_heading:

*********
dwellTime
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/dwellTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the dwell time, defined as the time interval between successive data samples during signal readout, which determines the receiver bandwidth and frequency resolution. This value is typically set automatically by the sequence and can be retrieved from the sequence protocol or DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _echoTime_heading:

********
echoTime
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/echoTime
   :value type: | embedded object array \(1-N\) of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the echo time (TE), defined as the interval between the center of the excitation pulse and the center of the measured echo, expressed in milliseconds. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _fatSuppressionTechnique_heading:

***********************
fatSuppressionTechnique
***********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fatSuppressionTechnique
   :value type: | linked object of type
                | `MRIFatSuppressionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIFatSuppressionTechnique.html>`_
   :instructions: Add the fat suppression technique used for this acquisition (for example, fat saturation, SPAIR, STIR, or Dixon); if no fat suppression was applied, leave this field null. This information is typically specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _fieldOfView_heading:

***********
fieldOfView
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/fieldOfView
   :value type: | linked object of type
                | undefined
   :instructions: Add the field of view of this image.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _flipAngle_heading:

*********
flipAngle
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/flipAngle
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the flip angle, defined as the angle by which the net magnetization is rotated by the radiofrequency excitation pulse, expressed in degrees. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _gradientCorrection_heading:

******************
gradientCorrection
******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/gradientCorrection
   :value type: | linked object of type
                | `AnalysisTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/analysisTechnique.html>`_
   :instructions: Add the gradient correction method applied during image reconstruction. This information is typically defined by the scanner system and can be retrieved from the reconstruction settings or DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _inversionTime_heading:

*************
inversionTime
*************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/inversionTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the inversion time (TI), defined as the interval between the inversion pulse and the excitation pulse, expressed in milliseconds. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _lookupLabel_heading:

***********
lookupLabel
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/lookupLabel
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter a lookup label for this device usage that may help you to find this instance more easily.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _matrixSize_heading:

**********
matrixSize
**********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/matrixSize
   :value type: integer array \(2-3\)
   :instructions: Enter the matrix size as the number of samples in the frequency and phase encoding directions for two-dimensional acquisitions (frequency × phase), or in the frequency, phase, and partition encoding directions for three-dimensional acquisitions (frequency × phase × partitions). This information is defined by the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _metadataLocation_heading:

****************
metadataLocation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/metadataLocation
   :value type: | linked object array \(1-N\) of type
                | `File <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/file.html>`_ or `FileBundle <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/data/fileBundle.html>`_
   :instructions: Add all files or file bundles containing additional information about the usage of this device.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _numberOfDiscardedVolumes_heading:

************************
numberOfDiscardedVolumes
************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfDiscardedVolumes
   :value type: integer
   :instructions: Enter the number of initial volumes automatically discarded by the scanner before saving data, typically to allow signal stabilization at the beginning of the acquisition. This value is defined by the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _numberOfExcitations_heading:

*******************
numberOfExcitations
*******************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfExcitations
   :value type: integer
   :instructions: Enter the number of excitations (NEX), defined as the number of times each k-space line is acquired and averaged to improve signal-to-noise ratio; if no averaging was performed, set this value to 1. This value is specified in the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _numberOfSlices_heading:

**************
numberOfSlices
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/numberOfSlices
   :value type: integer
   :instructions: Enter the number of slices corresponding to the total number of two-dimensional image slices acquired in this scan. This value is defined by the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _parallelAcquisitionTechnique_heading:

****************************
parallelAcquisitionTechnique
****************************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/parallelAcquisitionTechnique
   :value type: | linked object of type
                | `MRIParallelAcquisitionTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRIParallelAcquisitionTechnique.html>`_
   :instructions: Add the parallel acquisition technique used for this scan (for example, SENSE or GRAPPA). This information is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _phaseEncodingDirection_heading:

**********************
phaseEncodingDirection
**********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/phaseEncodingDirection
   :value type: integer array \(3-3\)
   :instructions: Enter the phase encoding direction as a signed unit vector in the scanner or image coordinate system (for example, [±1, 0, 0], [0, ±1, 0], or [0, 0, ±1]), where the nonzero component indicates the encoding axis and the sign specifies the polarity of k-space traversal.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _receiverBandwidth_heading:

*****************
receiverBandwidth
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/receiverBandwidth
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the receiver bandwidth, defined as the range of frequencies sampled per pixel during signal acquisition, expressed in hertz per pixel. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _repetitionTime_heading:

**************
repetitionTime
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/repetitionTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the repetition time (TR), defined as the interval between successive excitation pulses, expressed in milliseconds. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _sliceAngulation_heading:

***************
sliceAngulation
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceAngulation
   :value type: number array \(3-3\)
   :instructions: Enter the slice plane orientation as a three-element unit normal vector [nx, ny, nz] in scanner coordinates, where each component is a dimensionless floating-point value between -1 and +1 and the vector has unit length (nx² + ny² + nz² = 1). For non-oblique acquisitions, the vector aligns with a principal axis (for example, [0, 0, 1]), and for oblique acquisitions, the components are fractional.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _sliceGap_heading:

********
sliceGap
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceGap
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the slice gap, defined as the distance between adjacent slices, expressed in millimeters and excluding the slice thickness; if slice spacing is uniform, provide a single value, and if it varies across the volume, provide the corresponding range. This information is specified in the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _sliceOrientation_heading:

****************
sliceOrientation
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceOrientation
   :value type: | linked object of type
                | `AnatomicalPlane <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/anatomicalPlane.html>`_
   :instructions: Add the primary slice plane, defined relative to the scanner coordinate system, where axial corresponds to planes perpendicular to the scanner z-axis, sagittal to planes perpendicular to the x-axis, and coronal to planes perpendicular to the y-axis. This classification is independent of subject orientation and may therefore differ from anatomical planes when the subject is positioned non-standardly in the scanner.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _sliceThickness_heading:

**************
sliceThickness
**************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceThickness
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_ or `QuantitativeValueRange <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueRange.html>`_
   :instructions: Enter the slice thickness, defined as the physical thickness of each acquired slice, expressed in millimeters; if uniform, provide a single value, and if variable, provide the corresponding range. This value is specified in the acquisition protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _sliceTiming_heading:

***********
sliceTiming
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/sliceTiming
   :value type: | embedded object of type
                | `QuantitativeValueArray <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueArray.html>`_
   :instructions: Enter the slice timing, defined as the acquisition time of each slice within a volume relative to the start of the volume acquisition. This information is determined by the sequence timing and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _spatialEncoding_heading:

***************
spatialEncoding
***************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/spatialEncoding
   :value type: | linked object of type
                | `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/spatialEncoding.html>`_
   :instructions: Add the spatial encoding scheme used to acquire the data, specifying how frequency, phase, and partition encoding were applied (for example, frequency–phase encoding for two-dimensional acquisitions or frequency–phase–phase encoding for three-dimensional acquisitions). This information is defined in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _spoilingTechnique_heading:

*****************
spoilingTechnique
*****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/spoilingTechnique
   :value type: | linked object of type
                | `MRISpoilingTechnique <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/MRISpoilingTechnique.html>`_
   :instructions: Add the spoiling technique used in this acquisition, specifying the method applied to eliminate residual transverse magnetization (for example, radiofrequency spoiling or gradient spoiling). This information is defined in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _totalReadOutTime_heading:

****************
totalReadOutTime
****************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/totalReadOutTime
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the total readout time (TRT), defined as the time interval between acquisition of the first and last k-space lines in the phase-encoding direction during a single readout, expressed in milliseconds. This value is typically computed automatically and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _transmitterBandwidth_heading:

********************
transmitterBandwidth
********************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/transmitterBandwidth
   :value type: | embedded object of type
                | `QuantitativeValue <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValue.html>`_
   :instructions: Enter the transmitter bandwidth, defined as the frequency range excited by the radiofrequency pulse per pixel, expressed in hertz per pixel. This value is specified in the sequence protocol and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _usedCoils_heading:

*********
usedCoils
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedCoils
   :value type: | linked object array \(2-N\) of type
                | `DeviceType <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/deviceType.html>`_ or `MRICoilUsage <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/neuroimaging/device/MRICoilUsage.html>`_
   :instructions: Add all coils used for this acquisition, including built-in and external transmit, receive, and gradient-related coils, corresponding to the relevant DICOM coil attributes. Preferably provide structured coil descriptions; if unavailable, specify at least the device type.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _usedSpecimen_heading:

************
usedSpecimen
************

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/usedSpecimen
   :value type: | linked object of type
                | `SubjectState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/subjectState.html>`_ or `TissueSampleState <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/research/tissueSampleState.html>`_
   :instructions: Add the state of the tissue sample or subject that this device was used on.

`BACK TO TOP <MRIScannerUsage_>`_

------------

.. _voxelSize_heading:

*********
voxelSize
*********

Extent of the discrete elements comprising a three-dimensional entity.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/voxelSize
   :value type: | embedded object of type
                | `QuantitativeValueArray <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/quantitativeValueArray.html>`_
   :instructions: Enter the voxel size as the physical dimensions of a single image voxel in the x, y, and z directions, expressed in millimeters. This value is typically derived from the field of view, matrix size, and slice thickness and can be retrieved from the DICOM header.

`BACK TO TOP <MRIScannerUsage_>`_

------------

