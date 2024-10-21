.. header:: TechNES AI Best Practices Group: Using this guide

The 5 Questions
=================================

.. _Should I Use AI/ML?:

Should I use AI/ML?
-------------------

Developing an AI application can be challenging, particularly in the areas of
data collection, testing, and validation. As noted earlier, many applications of
AI have unique requirements that present their own problems. To address this,
the first step in this guide is to answer the key question: should I use AI to
solve my problem? We break this problem down into two parts:

* What is the engineering case for using AI to solve the problem, over other
  approaches? 
* Does the problem involve any application or data areas that may prohibit
  development?

  * What is the risk that the project falls into the unacceptable AI Risk
    category? 
  * What is the risk that the project makes use of problematic data?

+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Evaluate Engineering Case`                       | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Unacceptable AI Risk`                            | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Problematic Data Risk`                           | -        |          |
+--------------------------------------------------------+----------+----------+

.. _How do I define my AI project?:

How do I define my AI project?
------------------------------

In the previous step we developed an engineering case for using AI in our
project. In this step, we start to realize our project by setting the goals and
bounds of the project. There are three parts: 

* Defining goals and metrics for success
* Defining limitations and boundaries on the project
* Completing a risk assessment of the project as a whole

+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Establish Goals and KPIs`                        | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Risk Assessment`                                 | -        |          |
+--------------------------------------------------------+----------+----------+

.. _How do I collect data for my AI/ML project?:

How do I collect data for my AI/ML project?
-------------------------------------------

In the previous step, we defined the scope of our project. In this step, we move
on to the first practical engineering task: collecting the data. AI/ML
applications are fundamentally, data driven, so gathering or processing data is
essential. It’s very important to get this right,  as the quality of the data
will directly impact the success of training and deploying the AI application.
We set out a number of steps for this section, but our primary challenges are: 

* Making sure the data we collect is useful, truthful, and effective.
* Transforming our raw data into a form that can effectively utilized by AI/ML
  algorithms 
* Setting up a robust infrastructure for data collection, storage, and access.


+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Collecting your Data Set`                        | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Version Control, CI/CD for Data`                 | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Documentation`                                   | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Logging`                                         | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Data Exploration`                                | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Data Cleaning`                                   | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Validation and Testing`                          | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Data Storage and Access`                         | -        |          |
+--------------------------------------------------------+----------+----------+

.. _How do I train my AI/ML application?:

How do I train my AI/ML application?
------------------------------------

In the previous step, we collected the data for our AI project. In this step,
we will make use of it by using it to train an AI algorithm of our choice to
meet the goals of our project. This is also the step where systematic problems
from decisions in earlier steps are likely to start manifesting in force. We
strongly suggest that readers don’t hesitate to revisit earlier decisions at
this stage if they prove to be unfruitful. Once again, we set out a number of
steps for this section, but our primary challenges are:

* Deciding which AI approach to use
* Engineering a pipeline that optimizes the training
* Ensuring that the training results in an AI algorithm that performs as
  expected and avoids unintended behavior. 


+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Selecting an AI/ML Approach`                     | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Data Pre-processing`                             | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Creating a Training Pipeline`                    | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Testing, Validation & Biases in Training`        | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Version Control, CI/CD`                          | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Documentation and Logging`                       | -        |          |
+--------------------------------------------------------+----------+----------+

.. _How do I deploy my AI application?:

How do I deploy my AI application?
----------------------------------

After training our AI application, we can finally deploy it and (hopefully)
achieve the goals set out in our previous steps. For many professional engineers
his step will feel familiar , as the process for deploying an AI application is
similar to that of deploying any other software application. Our process has
three steps: 

* Preparing our trained the model for a live environment
* Engineering a process for deployment and model updating
* Setting up continuous monitoring to ensure the model performs as expected over
  time 


+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Deploying Your Model`                            | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Testing, Validation & Biases in Deployment`      | -        |          |
+--------------------------------------------------------+----------+----------+
