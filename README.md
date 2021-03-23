# fth-rbms
This project implements Restricted Boltzmann Machines (RBMs) using TensorFlow. Our implementation includes momentum, weight decay, L2 regularization, and CD-k contrastive divergence. We provide support for GPU (CUDA) calculations.

In addition, we provide an example file applying our model to the Movielens dataset (see ml_1m). The example trains an RBM, uses the trained model to extract features from the movie reviews, and finally uses a Tensorflow based logistic regression for genre classification. It achieves 91.8% classification accuracy (this is obviously not a cutting-edge model).
