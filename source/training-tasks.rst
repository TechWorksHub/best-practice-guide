How do I train my AI/ML application: Task List
==============================================

.. _How do I train my AI/ML application? Task List:

:ref:`How do I train my AI/ML application?`
-------------------------------------------

.. _Selecting an AI/ML Approach:

:ref:`Selecting an AI/ML Approach<How do I train my AI/ML application?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

There is not a set way of picking an AI algorithm to use in every case. In the
appendix we list how some common algorithms match up to the problems we
describe below, but this should not be taken prescriptively. The most practical
suggestion in most cases is to use these as suggestions for as a starting point,
and iterate. What others are doing with similar problems is another good
starting point. 

We break up the problems you need to think about when selecting an algorithm
into three parts. The first are practical considerations:

* What computational resources do you have available?
* How much data do you have, and how are you going to get it to the computer
  that you are using to train?
* How many resources (time, money, etc.) are you willing to spend on training?

A lot of the decisions in this area boil down to scaling. Almost any algorithm
can be deployed at some scale. The key question is what is the best algorithm
that I can deploy for my scale of data and available resources? It is important
to remember as part of this that not all algorithms scale equally - either with
amount of data or dimensionality. 


The second set of considerations are use case based. Especially, what, if any,
special requirements do you have for your end system? For example:

* Do the outcomes need to be explained in a human understandable way?
* Do I need to be able to enforce certain behavior in my model?
* Do I need to be able to explain or understand uncertainty in my model?

A lot of the above are common requirements that significantly limit the
available choices of algorithms.


Our third and final category are technical considerations:

* How do prospective approaches match up with the underlying assumptions of each
  algorithm?
* Is the complexity of my prospective algorithm appropriate for the problem I’m
  solving
* How do limitations of my data affect my choice?

It is important to remember with these points that all AI models are just
models, and will never reflect reality in full detail. Nor do we necessarily
want them to - as we see in the appendix on Bias and Variance, often a
purposely simpler model can produce better results than a more complex one,
especially when data or training is limited. Limitations on training data can be
important too. Some AI algorithms cannot deal with data that has missing parts,
for example. This must either be addressed, or a different approach used. 

To complete this section you must:

* Select an AI approach (or approaches) to use in subsequent steps

.. _Data Pre-processing:

:ref:`Data Pre-processing<How do I train my AI/ML application?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This step has a lot of overlap with our previous Collecting Data subsection on
Data Cleaning. Our focus here is slightly different, with us instead looking at
maximizing the efficacy of our training process, rather than specifically
focusing on fixing deficiencies in the data. 


**Missing data.** Depending on your choice of AI Algorithm, missing data may
have suddenly become extremely important. If this is the case, revisit the Data
Collection section, Data Cleaning subsection in the issue. 

**Scaling and Transforming data.** For many models, the training process can be
improved by scaling or transforming the data. For example, scaling all values to
be on the same scale. 

There are a range of reasons you might want to do this. A common example is two
features being on different scales. If we have one feature that takes on values
in the range 0-1, and another that takes on values in the range 0-100, some
types of analysis may cause us to weigh one more heavily than the other. 


Which technique will be applied will depend on your analysis and goals. Some
common techniques would be:

* Removing the average from a set of numbers
* Transforming all values to the same scale
* Scaling all values to a normal distribution

**Dimensionality Reduction.** Sometimes our datasets include a large number of
features. This can be a blessing because it gives us more information to
integrate into our analysis, but it can also cause difficulties:

* It increases computational cost of training
* It can cause overfitting, especially if the extra features are not useful
* Multiple weak features are often a less useful explanation than one or two
  strong ones

A way of dealing with this is to reduce the dimensionality of the data. There
are two very broad ways of approaching this:

* We can select the most useful features from our existing set of features
* We can aggregate our current features to create a new set of features with
  beneficial features

The advantage of the first is that we can perform dimensionality reduction with
the existing features to select the best ones. The advantage of the second is
that, although our constructed dimensions lose interpretability, the process by
which we create them typically makes them very strong at explaining our data. 

To complete this step you must:

* Create a pre-processing procedure for your data


.. _Creating a Training Pipeline:

:ref:`Creating a Training Pipeline<How do I train my AI/ML application?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this step you must create an automated process to ingest the data collected,
cleaned and preprocessed, and use it to train a model.
 

For small projects, this may be a very simple script consisting of a few lines
of code collecting the data and running the training function. For larger
projects, larger datasets, or non-standard tools this may be significantly
harder. 


**Hardware Acceleration.** Many machine workloads can be significantly sped up
using hardware that shifts computationally intensive parts of the training
process to specialized processing units. These technologies generally work by
improving matrix arithmetic. It is not always necessary or desirable to do this,
but it can be very beneficial for some workloads. Neural Networks are one
example where hardware acceleration has been very successful.


Though there are special processors available for this, modern graphics cards
also do this type of processing, are often competitive on cost-per-processing
power basis, and have additional uses (e.g. as graphics processors).

**Storage Mediums.** This is an excellent opportunity to revisit the Collecting
Data section, under the subsection of Data Storage and Access. The discussion on
different data storage mediums is extremely relevant to training. 

**Large Datasets & Resource Intensive Projects.** Larger projects may end up in
a situation in which the dataset is not stored on one machine, and/or
computation must be spread across multiple distributed units. Future iterations
of this guide will cover this issue, currently we suggest that readers seek
expert advice on this complex topic.

To complete this step:

* Create a training pipeline


.. _Testing, Validation & Biases in Training:

:ref:`Testing, Validation & Biases in Training<How do I train my AI/ML application?>`
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Testing how the model performs through its training process is extremely
important. For models of small scale, it is a vital diagnostic tool. For models
of a large scale, it allows us to identify problems early, before too many
resources are committed to them. 

**Training Error.** It’s important to split your dataset into at least 2 parts -
a training dataset and a testing dataset. Most (e.g. 90%) of your data will be
in the training dataset, and this will be what you use to do your training.
Entirely separately from this 


**Parameters and Hyperparameters.** As important as always. We are essentially
testing for extremely similar things as the testing and validation for the data
collection, but the downstream versions.


**Bias.** If there are specific biases of concern in your dataset, you should
check these during training. This should be done by creating a test of bias, and
periodically running it during the training process. 


To complete this step:

* Create an automated testing process


.. _Version Control, CI/CD:

:ref:`Version Control, CI/CD<How do I train my AI/ML application?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A large part of this is discussed in the previous section under “collecting
data”. The extra considerations for the training process are that we must now
firmly keep track of two, nested versionings. We need to keep track of not just
the version of the code that was used to train a model, but the version of any
data used to train the model too. 


Large trained models may not be suitable for normal version control and may
require similar techniques (though at a comparatively smaller scale) to data
version control.

To complete this step:

* Include your training process within your version control


.. _Documentation and Logging:

:ref:`Documentation and Logging<How do I train my AI/ML application?>`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

There is significant overlap between this section and the Documentation and
Logging section of the Collecting Data section. 

One thing to clearly document in the training process is any hyperparameters
associated with the algorithm you are using. These will have a significant
effect on the training process. For example, learning rate in a neural network,
or the parameters of the kernel in a Support Vector Machine. In addition to
these, it is important to keep track of and document all decisions you are
making in your training pipeline. Qualities like the batch size of training in a
neural network might not be a hyperparameter in a certain narrow sense, but can
make almost as much difference to the outcome of training. 


Logging remains important. it is important to keep track of how training
progressed even in failed testing cases and how well your model is training
throughout the process. 

To complete this step:

* Create documentation and a logging process