.. contents:: Table of Contents
    :class: sidebar
    :depth: 2

.. header:: TechNES AI Best Practices Group: 
    
    `Guidance for Electronic Systems Engineers`:strong:

AI/ML Overview and Trade-offs
=============================

Aims of this document:
----------------------
* Key considerations to be aware of in employing AI/ML in an embedded system
* Guidance towards application appropriate solutions given relevant trade-offs and system-level requirements
* Doesn’t appear to be anything like this online
* Who are the end users and how will they use it?
* Tim likes “cheat sheets”
* How affected by the type of users (Verification engineer, designer, …)
* Only industry or also academic (note specific to TechNeS, and aimed a professional engineers)
* Can we reuse academic courses
* How much more detail needed
* What prior experience assumed (general and AI specific)?
* Make it narrower, focus on applications, examples specific users
* Should I even use AI?
* Need decision steps, choice of algorithm is towards the end, may need to try several
* different collateral for stages as user gains expertise
* Start with good and bad examples of AI in use
* how to balance information overload: break into steps, separate guides for different problems

Candidate “Documentation” Technologies
======================================

Requirements
------------
* Must be good for collaborative work
* Must generate at least PDF, HTML, ideally help files
* Must be able to add mixed media (images/video)
* Needs version control
* Must be freely available to the group

Candidates
----------
* Restructured Text
* DocBook/DITA

Non-candidates
--------------
* Overleaf/LaTex - can’t generate structured HTML
* MS Word/OpenOffice/LibreOffice - can’t generate structured HTML
* Canva - proprietary

Top Level Decision steps
========================

Step 1:
    Train user in vocabulary to be able to address the problem accurately.  Enable conversation between engineering and marketing to refine product (may be highly disruptively).

Step 2:
    Can you relate your problem to an existing problem AI has already solved (data architecture and algorithm). Or do you need a new AI approach. Is it possible with AI? Or do you even need AI? We need to create the inverse table: what AI can do. Allow user to refine from general to specific AI choice

Step 3:
    Identify candidate solutions (data architecture and algorithm), cross-check features against table in this document. Do this hierarchically.  Identify any wider impact on the system by choice of AI.

Step 4:
    Identify AI engineering skills needed (training/buy-in)

End step:
    Engineer can implement their project

Overview: How Algorithms Learn
===============================

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| How AI Algorithms learn | Description                                                                                                                                                                       |
+=========================+==============+====================================================================================================================================================================+
| Supervised              | The model is trained on ‘labelled’ data, where known correct outputs are labelled alongside the input data to enable future classification or predictions, sepcialized variants   |
|                         |   * Semi-supervised: Not all the data is labelled or reliable, so need to mix with unsupervised techniques to pre-process the data                                                |
|                         |   * Self-Supervised: Applying a pre-trained (pretext) supervised learning model to an unsupervised learning problem to address a specific problem                                 |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unsupervised            | The model is presented with unlabeled data and so has to exploit inherent qualities in the input data, such as clustering or density / distribution to ‘learn’ how to process it. |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reinforcement           | Technically a class of supervised learning, but usually categorized separately. The model operates without training but in an environment where it’s decision outputs (based on   |
|                         | given input data) will elicit reward signals (positive and negative feedback). It must thereby optimise it’s internal model of likely success from a given current state.         |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Neural Network Algorithm Families
=================================

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AI Algorithm Families   | Description                                                                                                                                                                       |
+=========================+==============+====================================================================================================================================================================+
| Feed Forward Neural     | A collection of layered, interconnected nodes which sum weighted inputs and applies an activation (mathematical) function to derive output. Input data travels in one direction   |
| Networks                | only and exits through output nodes. Before use FFN’s are trained using a training dataset and thus use a supervised learning approach.                                           |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Recurrent Neural        | By feeding intermediate layer outputs back to the inputs, better prediction of outcomes is achieved. In this way, some information the network possessed in the previous time-    |
| Networks                | step is remembered by a memory function.                                                                                                                                          |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unsupervised Neural     | The network does not receive a prior training dataset and, instead, is presented with unlabeled data. The network therefore has to exploit inherent qualities in the input data   |
| Networks                | to ‘learn’ how to process it. Typically ‘training’ occurs ‘on the job’ e.g. using competitive rather than error-correction learning.                                              |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Graph Neural            |                                                                                                                                                                                   |
| Networks                |                                                                                                                                                                                   |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spiking Neural          |                                                                                                                                                                                   |
| Networks                |                                                                                                                                                                                   |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Non-Neural Network Algorithm Families
=====================================

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AI Algorithm Families   | Description                                                                                                                                                                       |
+=========================+==============+====================================================================================================================================================================+
| Linear and related      | * Linear Regression                                                                                                                                                               |
|                         | * Spline Interpolation                                                                                                                                                            |
|                         | * Support Vector Machine (SVM)                                                                                                                                                    | 
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tree Based Methods      | * Decision trees                                                                                                                                                                  |
|                         | * Random Forests                                                                                                                                                                  |
|                         | * Boosted/Bagged trees                                                                                                                                                            | 
|                         | * Gradient Boosted trees                                                                                                                                                          | 
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nearest Neighbor        | * K-nearest neighbor                                                                                                                                                              |
|                         | * k-means                                                                                                                                                                         |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Statistical             | * Naieve Bayes                                                                                                                                                                    |
|                         | * T-test/F-test                                                                                                                                                                   |
|                         | * Markov Chain Monte Carlo                                                                                                                                                        |
|                         |     - Simulated Annealing                                                                                                                                                         |
|                         |     - Dynamic Causal Modelling                                                                                                                                                    |
|                         | * Full Bayesian Methods                                                                                                                                                           |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Symbolic                | * Inductive Logic Programming                                                                                                                                                     |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bio-Inspired            | * Genetic Algorithms/Genetic Programming                                                                                                                                          |
|                         | * Any Colony Optimization                                                                                                                                                         |
|                         | * Particle Swarm Optimization                                                                                                                                                     |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Mathematical Models
=====================================
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Algorithm               | Description                                      | Type            | Learning     | Benefits                                         | Application                                      |
+=========================+==================================================+=================+==============+==================================================+==================================================+
| Linear Regression       | Line-fit algorithm, according to: y=ax+b.        | Regression      | Supervised   | Efficient for linear relationships e.g. trends   | Drug-dosage relationships                        |
|                         |                                                  |                 |              | or forecasts                                     |                                                  |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Logistic Regression     | Discrete outcomes from linear data.              | Classification  | Supervised   | Efficient for linear relationships when the data | Medical data, Credit scoring,                    |
|                         |                                                  |                 |              | set is linearly separable                        | Language processing                              |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Decision Tree           | Data set is split recursively into a tree        | Classification  | Supervised   | Fast and efficient to run. Easy to understand    | Data mining, Planning, Fault diagnosis           |       
|                         |                                                  |                 |              | and interpret. Can handle any type of data       |                                                  |
|                         | comprising decision nodes and outcome leaves.    | (or Regression) |              |                                                  |                                                  |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Support Vector Machine  | SVM algorithms classify data in n                | Classification  | Supervised   | Handles high dimensional data, separating things | Face detection, Handwriting recognition,         |
|                         | (no of features)-dimensional space.              | (or Regression) |              | into (typically two) groups with more separation | Image classification                             |
|                         |                                                  |                 |              | than other algorithms by projecting the data     |                                                  |
|                         |                                                  |                 |              | into a more easily separable space.              |                                                  |
|                         |                                                  |                 |              |                                                  |                                                  |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Naieve Bayes            | Simple classification algorithm using            | Classification  | Supervised   | Requires less training data than other           | Face recognition, Weather prediction,            |
|                         | conditional probability of an event based on     |                 |              | algorithms and handles both continuous and       | Medical diagnosis, News classification, Spam     |
|                         | prior events.                                    |                 |              | discrete data. Highly scalable with the number   | email detection based on word frequency vs real  |
|                         |                                                  |                 |              | of predictors and data points. Fast runtime      | email.                                           |
|                         |                                                  |                 |              | enables real-time predictions.                   |                                                  |
|                         |                                                  |                 |              |                                                  |                                                  |
|                         |                                                  |                 |              |                                                  |                                                  |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| K-nearest Neighbor      | Classification based on prior classification of  | Classification  | Supervised   | Simple to implement and effective for data with  | Text mining, Finance, Medical, Facial            |    
|                         | the majority of (K) nearest neighbors with a     |                 |              | low dimensionality. There is no training period  | recognition, Recommendation systems (e.g. music  |    
|                         | distance function. (Becomes computationally      |                 |              | (data is stored only for use later) which makes  | based on age, genre, country)                    |
|                         | expensive as dataset and dimensionality scale).  |                 |              | KNN faster than other (trained) algorithms.      |                                                  |
|                         |                                                  |                 |              | Furthermore, new training data can be added      |                                                  |   
|                         |                                                  |                 |              | seamlessly.                                      |                                                  |                       
|                         |                                                  | (or Regression) |              |                                                  |                                                  |
|                         |                                                  |                 |              |                                                  |                                                  |
|                         |                                                  |                 |              |                                                  |                                                  |
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| K-Means                 | Classifies data into K clusters through          | Classification  | Unsupervised | Simple to implement and results are easy to      | Image segmentation, Image compression, Biological|
|                         | recursive clustering of data with similar        |                 |              | interpret. Handles large datasets well and       | data, Fraud detection, Transport data analysis   | 
|                         | features.                                        |                 |              | guarantees convergence. Easily adapts to changes |                                                  |       
|                         |                                                  |                 |              | in data.                                         |                                                  |   
|                         |                                                  | (or Regression) |              |                                                  |                                                  | 
|                         |                                                  |                 |              |                                                  |                                                  | 
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+
| Random Forest           | Average across multiple decision trees           | Classification  | Supervised   | Reliable predictions that can be understood      | Finance risk, Medical trends, Stock trading,     |
|                         | trained on various subsets of the data.          |                 |              | easily. Handles large datasets efficiently.      | E-commerce                                       |
|                         |                                                  |                 |              | More accurate than a single decision tree.       |                                                  |   
|                         |                                                  | (or Regression) |              |                                                  |                                                  | 
+-------------------------+--------------------------------------------------+-----------------+--------------+--------------------------------------------------+--------------------------------------------------+

Feed Forward Neural Networks
=====================================

+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| ANN                     | Description                                                                                                               |          Application                          |
+=========================+===========================================================================================================================+===============================================+
| Feed Forward Neural     | Collection of interconnected nodes, arranged in layers. The basic unit is the Perceptron (or Threshold Logic Unit) - a    | Data Compression, Pattern Recognition, Machine|       
| Network                 | single node which sums weighted inputs and applies an activation function to derive the output. In larger networks with   | diagnostics, Image / Speech / Handwriting     |      
|                         | multiple nodes, input data travels in one direction, passing through a number of input nodes and exiting through output   | Recognition                                   |              
|                         | nodes. In a multilayer network (three or more successive layers), each node is connected to all nodes in the next layer.  |                                               |  
|                         | The output is a function (activation function) of the sum of all inputs multiplied by their respective weights. During    |                                               |  
|                         | training (Supervised Learning), the weights are calculated through backpropagation.                                       |                                               |      
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Convolutional Neural    | A form of FFN Inspired by the animal visual cortex. The CNN is a 3D arrangement of neurons, employing convolutional       | Video recognition, semantic parsing and       |      
| Network                 | processing rather than multiplication in its hidden layers. Each neuron in the first (convolutional) layer only           | paraphrase detection.                         |                      
|                         | processes information from a small part of the input field. The network understands images in parts and computes these    |                                               |      
|                         | operations multiple times to process the full image. Nodes are connected only locally to nearby neighbors unlike an FFN.  |                                               |          
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Radial Basis Function   | A three-layer FFN where the hidden layer uses a non-linear RBF activation function. Classification is performed by        | System modelling & control, time series       |  
| Neural Network          | measuring the input’s similarity to previously trained data points.                                                       | prediction, image classification              |  
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Recurrent Neural Networks
=====================================

+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| ANN                     | Description                                                                                                               |          Application                          |
+=========================+===========================================================================================================================+===============================================+
| Recurrent Neural        | Layer outputs fed back to the inputs help in predicting outcomes. The first layer is typically a feed forward neural      | Handwriting / Speech recognition, Language    |
| Network                 | network followed by a recurrent layer where some information it had in the previous time-step is remembered by a memory   | modelling & translation, Text summarization,  |
|                         | function.                                                                                                                 | Image tagging                                 |
|                         |                                                                                                                           |                                               |
|                         |                                                                                                                           |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Long short-term memory  | A more sophisticated RNN which uses memory gates to regulate information flow through the network so as to improve        | Unsegmented connected handwriting recognition,| 
| (LSTM)                  | training by avoiding loss of small gradient data during backpropagation.                                                  | speech recognition, robot control, video games|
|                         |                                                                                                                           |                                               |
|                         |                                                                                                                           |                                               |
|                         |                                                                                                                           |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Sequence to Sequence    | Two Recurrent Neural Networks working simultaneously. One RNN is configured as an encoder, processing the input data and  | Machine translation, Speech recognition, Text |
| (Seq2Seq)               | the second as a decoder which derives the output based on the encoder’s final internal state.                             | summarization, Conversational models /        |
|                         |                                                                                                                           | Chat-bots, Video captioning                   |
|                         |                                                                                                                           |                                               |
|                         |                                                                                                                           |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Attention network       | Attention networks mimic cognitive attention by enhancing some parts of the input data while diminishing other parts;     | Reasoning, Complex language processing.       |
|                         | i.e. to focus attention on a small but important part of the data. Learning which part of the data is more important      | Multi-sensory data processing                 |
|                         | than others depends on the context and is trained by the gradient descent algorithm.                                      | (sound, images, video, and text)              |
|                         |                                                                                                                           |                                               |
|                         |                                                                                                                           |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Recurrent Neural Networks
=====================================

+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| ANN                     | Description                                                                                                               |          Application                          |
+=========================+===========================================================================================================================+===============================================+
| Self-Organizing Map /   | Unsupervised technique producing a 1 or 2-D representation of a higher dimensional dataset such that similar observations | Visualizing data in large datasets, Project   |
| Kohonen Net             | are clustered to aid onward analysis. The network is trained using competitive rather than error-correction learning so   | prioritization, Seismic or Failure mode       |
|                         | that nodes ‘move’ within the dataspace to generate a map of the reference data. During iterative training, node weights   | analysis, Artwork creation                    |
|                         | change in order to ‘cluster’ the neurons together to reduce the distance between neuron and input. The map can then       |                                               |
|                         | classify observations for the input space by finding the node with the closest weight vector to the input space vector.   |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Generative adversarial  | Two neural networks compete in a zero-sum game. The generator network learns to generate new data with the same           | Image-to-Image / Text-to-Image Translation,   |
| network (GAN)           | statistics as the training set in an unsupervised way, as it is indirectly trained by the discriminator (the second       | Semantic image manipulation and creation,     |
|                         | neural network) which can tell how realistic a given input is while it is itself being updated dynamically. GANs are      | Photo editing / blending, Face aging, Video   |
|                         | also useful for semi-supervised, fully supervised and reinforcement learning.                                             | prediction, Super-resolution                  |
|                         |                                                                                                                           |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Autoencoder             | An autoencoder is a Feed Forward Neural Network which learns an efficient representation (encoding) for a set of          | Dimensionality reduction, Information         |
|                         | unlabeled data , through unsupervised learning. The autoencoder consists of two main parts: an encoder that maps the      | retrieval, Anomaly detection Feature          |
|                         | input into the code, and a decoder that maps the code to a reconstruction of the input. The encoding is refined by        | extraction, Image denoising and compression,  |
|                         | attempting to regenerate the input from the encoding whilst minimizing the difference between input and output. The       | Image search, Image generation                |
|                         | network therefore generates new data rather than predicting target values and is thus unsupervised.                       |                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+