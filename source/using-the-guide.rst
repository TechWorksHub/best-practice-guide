.. header:: TechNES AI Best Practices Group: Using this guide

.. _Using this Guide:

Using this guide: The five questions
=================================

This guide will help you answer five questions step by step:

1. Should I use AI/ML?
2. How do I define my AI/ML project
3. How do I collect data?
4. How do I train my AI/ML application?
5. How do I deploy my AI/ML application?

Answering these questions will take you from conceptualizing your
AI application through to deploying it in the real world.

These five questions are broken into subsidiary questions, requirements, and tasks to
be completed.  We set out the question in the order they should be considered.
We strongly recommend you don't skip ahead, although from time to time you may
want to go back and review your answers to earlier questions.

These smaller questions, requirements and tasks for each of the five main questions
are recorded in a table, showing what the activity is, and where you should
record the documentary evidence of that activity being completed. Some of the
entries may be optional, depending on earlier answers.  Once all the required
subsidiary questions, requirements, and tasks are addressed, you will have your
answer to the main question, and can move on to the next of these five questions.

+----------------------------+--------------------------------------+----------+
| Question/Task/Requirement  | Evidence                             | Done     |
+============================+======================================+==========+
| Example requirement 1      | Example Risk Assessment.pdf,         | Yes      |
|                            | Example document.pdf                 |          |
+----------------------------+--------------------------------------+----------+
| Example requirement 2      | -                                    | -        |
+----------------------------+--------------------------------------+----------+
| ...                        | -                                    | -        |
+----------------------------+--------------------------------------+----------+

.. _Should I Use AI/ML?:

Question 1: Should I use AI/ML?
-------------------------------

Developing an AI application can present significant challenges. Collection of
data, testing and validation are challenges.
Many applications of AI will come with special requirements that can be a
challenge in themselves. To address this, the very first step in this guide is
to be able answer the following: should I use AI to solve my problem? We break
this problem down into two parts:

* What is the engineering case for using AI to solve the problem, over other
  approaches?
* Does the problem touch on any application or data areas that may effectively
  prohibit development?
  * What is the risk that the project falls into the :ref:`unacceptable AI Risk
    category<Unacceptable AI Risk>`?
  * What is the risk that the project makes use of :ref:`problematic data<Problematic Data Risk>`?

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

Question 2: How do I define my AI project?
------------------------------------------

In the previous step we worked on an engineering case for AI in our project. In
this step, we will take the first step in realizing our project by setting the
goals and bounds of the project. There are three steps to complete in this
section:

* Defining goals and metrics for success (KPIs)
* Defining limitations and boundaries on the project
* Completing a risk assessment of the project as a whole

+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Establish Goals and KPIs`                        | -        |          |
+--------------------------------------------------------+----------+----------+
| LIMITATIONS AND BOUNDARIES ON THE PROJECT?             | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Risk Assessment`                                 | -        |          |
+--------------------------------------------------------+----------+----------+

.. _How do I collect data for my AI/ML project?:

Question 3: How do I collect data for my AI/ML project?
-------------------------------------------------------

In the previous step, we defined the scope of our project. In this step, we move
on to the first part of the practical engineering of our AI project: collecting
the data. AI/ML applications are, at their core, data driven. At some level,
data will need to be collected, or at the very least, processed. It’s very
important to get this right, as the strength of the data will have a strong
impact on the efficacy of training and deploying our AI application. We set out
a number of steps for this section, but our primary challenges are:

* Making sure the data we’re is collecting useful, truthful, and effective
* Making sure we transform our raw data into a form that can effectively 
  utilized by AI/ML algorithms
* Making sure our infrastructure for collection, storage, and access is
  appropriate and robust


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

Question 4: How do I train my AI/ML application?
------------------------------------------------

In the previous step, we collected the data for our AI project. In this step,
we will make use of it by using it to train an AI algorithm of our choice to
meet the goals of our project. This is also the step where systematic problems
from decisions in earlier steps are likely to start manifesting in force. We
strongly suggest that readers don’t hesitate to revisit earlier decisions at
this stage if they prove to be unfruitful. Once again, we set out a number of
steps for this section, but our primary challenges are:

* Establishing which AI approach we’re going to use
* Engineering a pipeline to train our approach in the best possible way
* Building confidence that this training results in an AI algorithm that does
  all the things it should, and none of the things it shouldn’t


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

Question 5: How do I deploy my AI application?
----------------------------------------------

After training our AI application, we can finally deploy it and (hopefully)
achieve the goals set out in our previous steps. This step will likely represent
a welcome return to familiarity for the professional engineer, as the process
for deploying an AI application is fairly similar to that of deploying any other
software application. Our process will proceed broadly in three steps:

* Preparing our trained model for a live environment
* Engineering a process for deployment and model updating
* Setting up continuous monitoring for our model


+--------------------------------------------------------+----------+----------+
| Requirement                                            | Evidence | Complete |
+========================================================+==========+==========+
| :ref:`Deploying Your Model`                            | -        |          |
+--------------------------------------------------------+----------+----------+
| :ref:`Testing, Validation & Biases in Deployment`      | -        |          |
+--------------------------------------------------------+----------+----------+
