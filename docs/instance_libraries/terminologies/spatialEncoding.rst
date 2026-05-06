######################################
Terminologies: SpatialEncoding library
######################################

Related schema specification: `SpatialEncoding <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/controlledTerms/spatialEncoding.html>`_

------------

------------

one-dimensionalFrequencyEncoding
--------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalFrequencyEncoding
   :@type: https://openminds.om-i.org/types/SpatialEncoding
   :definition: A spatial encoding method in which position along a single dimension is represented by differences in signal frequency.
   :description: In one-dimensional frequency encoding, spatial location is mapped directly to frequency components of the detected signal. A spatially varying field or gradient establishes a linear relationship between position and frequency. Signals from different locations are separated through spectral analysis. Reconstruction is performed by converting frequency information into spatial coordinates. This method is widely used in line-scan imaging, spectroscopy, and single-axis readout systems.
   :name: one-dimensional frequency encoding

`BACK TO TOP <Terminologies: SpatialEncoding library_>`_

------------

one-dimensionalPhaseEncoding
----------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/spatialEncoding/one-dimensionalPhaseEncoding
   :@type: https://openminds.om-i.org/types/SpatialEncoding
   :definition: A spatial encoding method in which position along a single dimension is represented by controlled phase shifts of the signal.
   :description: In one-dimensional phase encoding, spatial position is encoded through accumulated phase differences. A preparatory gradient or modulation step introduces position-dependent phase offsets. These phase shifts are sampled over repeated measurements. Spatial information is recovered through Fourier or phase-sensitive reconstruction. This method is commonly used when frequency-based encoding is impractical or insufficient.
   :name: one-dimensional phase encoding

`BACK TO TOP <Terminologies: SpatialEncoding library_>`_

------------

three-dimensionalFrequency-phase-phaseEncoding
----------------------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/spatialEncoding/three-dimensionalFrequency-phase-phaseEncoding
   :@type: https://openminds.om-i.org/types/SpatialEncoding
   :definition: A spatial encoding method in which position in three dimensions is represented using frequency encoding along one axis and phase encoding along two orthogonal axes.
   :description: In three-dimensional frequency-phase-phase encoding, spatial information is distributed across one frequency-encoded and two phase-encoded dimensions. A readout gradient provides frequency discrimination along one axis. Two independent phase-encoding steps encode the remaining spatial directions. Repeated acquisitions sample the three-dimensional encoding space. Reconstruction produces volumetric spatial representations from the combined frequency and phase data.
   :name: three-dimensional frequency-phase-phase encoding

`BACK TO TOP <Terminologies: SpatialEncoding library_>`_

------------

two-dimensionalFrequency-phaseEncoding
--------------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/spatialEncoding/two-dimensionalFrequency-phaseEncoding
   :@type: https://openminds.om-i.org/types/SpatialEncoding
   :definition: A spatial encoding method in which position in two dimensions is represented using frequency encoding along one axis and phase encoding along a second axis.
   :description: In two-dimensional frequency-phase encoding, one spatial direction is mapped to signal frequency and the other to signal phase. A readout gradient establishes frequency encoding, while stepped gradients impose phase encoding. Multiple acquisitions are combined to sample the two-dimensional encoding space. Reconstruction converts frequency and phase information into planar spatial coordinates. This approach is widely used in two-dimensional imaging and mapping applications.
   :name: two-dimensional frequency-phase encoding

`BACK TO TOP <Terminologies: SpatialEncoding library_>`_

------------

