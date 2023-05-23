
<img src="https://github.com/Elonsolmostafa1/Flood-Damage/assets/49917088/81cd2432-55ea-4c14-a7e6-bfdee864e85c" width="100%">

## Flood Damage Detection in Satellite Imagery

This project aims to develop an automated method for detecting post-flood damages in satellite imagery using machine learning and computer vision techniques. The solution enables the rapid and accurate identification of damaged areas, assisting emergency responders and disaster relief organizations in effectively allocating resources and planning response efforts.

### Project Overview
Floods are devastating natural disasters that require prompt and accurate assessment of the damage caused. Satellite imagery provides a powerful tool for post-flood damage assessment, but manual analysis is time-consuming and labor-intensive. This project addresses the need for an automated solution by leveraging machine learning and computer vision techniques.

### Key Tasks
The project consists of the following key tasks:

1. Preprocessing: All satellite images are resized to a consistent size to ensure uniformity in subsequent analysis steps.

2. Feature Extraction: Multiple feature extraction techniques are employed to capture different aspects of flood damage:

   - Local Binary Patterns (LBP): Captures local texture patterns.
   - Histogram of Oriented Gradients (HOG): Extracts gradient information for edge and shape characteristics.
   - Convolutional Neural Network (CNN) Features from ResNet: Utilizes transfer learning to extract high-level features.
   - Gray-Level Co-occurrence Matrix (GLCM) Features: Analyzes statistical properties of pixel intensities.

3. Classification: Five classifiers are employed to distinguish between damaged and undamaged areas:

   - Support Vector Machine (SVM)
   - k-Nearest Neighbors (KNN)
   - Random Forest
   - Naive Bayes
   - Logistic Regression


The classifiers are compared for each feature type to identify the most accurate model. Random Forest achieves the highest accuracy with CNN features (98%), LBP features (90%), and HOG features (83%). To maximize accuracy, LBP features are combined with CNN features.

4. Deep Learning Model: A Convolutional Neural Network (CNN) is implemented to classify flood damage. The model achieves an accuracy of 81.722%.


#### Why we choose transfer learning ?
transfer learning with models like ResNet can often be beneficial compared to training a deep learning model from scratch, especially when you have a limited amount of labeled data. Here are some reasons why transfer learning can be advantageous:

Feature Extraction: Pre-trained models like ResNet have learned powerful feature representations from large-scale datasets. By leveraging these pre-trained models, you can benefit from their ability to capture meaningful features, even if you have limited labeled data.

Reduced Training Time: Training a deep learning model from scratch can be computationally expensive and time-consuming, especially if you don't have access to a large amount of labeled data and computational resources. Transfer learning allows you to skip the initial training phase of the base model and focus on fine-tuning or training the top layers, which significantly reduces training time.

Generalization: Pre-trained models are trained on diverse datasets, enabling them to generalize well to new tasks and domains. The learned features tend to be robust and transferrable, which can improve the performance of your model on your specific task, even with a smaller dataset.

Avoiding Overfitting: Transfer learning helps mitigate the risk of overfitting, especially when the available labeled data is limited. The pre-trained model has already learned relevant features from a large dataset, which can prevent the model from memorizing the small labeled dataset, leading to better generalization.



5. Segmentation: For the segmentation task, K-means clustering with three clusters and Gaussian Mixture Model (GMM) are employed. K-means clustering is chosen as the preferred method.

### Results and Conclusion
Based on the evaluation of different classifiers and feature types, the combination of LBP and CNN features with Random Forest achieves the highest accuracy for flood damage detection. The project demonstrates the potential of machine learning and computer vision techniques in automating post-flood damage assessment.

The solution can significantly impact disaster response and recovery efforts by providing timely and accurate information to emergency responders and decision-makers. By promptly identifying damaged areas, resources can be allocated more effectively, leading to improved disaster management and ultimately better outcomes for the affected population.


### Segementaion Results using k-mean


![1](https://github.com/Elonsolmostafa1/Flood-Damage/assets/62807830/0baa69b5-219b-4589-920d-6b5168951cc5)
![2](https://github.com/Elonsolmostafa1/Flood-Damage/assets/62807830/7f147836-e248-4d4d-b228-cd39a038f22f)

![3](https://github.com/Elonsolmostafa1/Flood-Damage/assets/62807830/11f3aa9c-ffe1-443f-be76-a08ee3c66240)
