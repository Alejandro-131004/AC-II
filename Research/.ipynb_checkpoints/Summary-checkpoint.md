## A Dataset and Taxonomy for Urban Sound Research

1. ### Introduction and Motivation

    - Urban sound classification is crucial for urban informatics and multimedia retrieval.

    - Two main barriers in this field:
        - Lack of a common taxonomy.
        - Scarcity of large, annotated datasets.

2. ### Urban Sound Taxonomy

    - **Requirements for an Urban Sound Taxonomy:**

        - **Integration of Previous Research:** Based on subsets of prior urban acoustic research, grouping sounds into four main categories: human, nature, mechanical, and music.

        - **Detailed Classification:** Emphasis on specific, low-level sounds (e.g., “car horn,” “engine”) rather than broad categories to enhance clarity and utility.

        - **Focus on Urban Noise Pollution:** Centers on high-complaint sounds from NYC’s 311 data (370,000+ complaints), including frequently disruptive sounds like construction, traffic noise, loud music, and animal noises (e.g., dog barks).

    - The authors propose a taxonomy to classify urban sounds into four high-level groups:
        - Human
        - Nature 
        - Mechanical 
        - Music.


3. ### UrbanSound Dataset

    - UrbanSound contains 27 hours of audio, with 18.5 hours labeled across 10 classes:
        - Classes include: 
            - air conditioner
            - car horn 
            - children playing 
            - dog bark 
            - drilling
            - etc.

        -  All of the classes, with the exception of **"children playing"** and **"gun shots"** (they were added for variety), were selected due to the high frequency in which they appear in **urban noise complaints**.

    - Dataset collected from Freesound, and recordings annotated for sound occurrence and salience.

    - UrbanSound8K subset created for training purposes:
        - Includes 8732 labeled audio slices (8.75 hours) segmented to a maximum of 4 seconds.

        - Distribution of labeled occurrences and slices visualized.

4. ### Classification Experiments

    - Conducted baseline classification using various algorithms (SVM, RandomForest, etc.).

    ### Feature Extraction for Sound Classification

    #### Feature Choice - MFCCs

    - **Mel-Frequency Cepstral Coefficients (MFCCs)** were selected as the main feature due to their success in environmental sound classification.
    
    - MFCCs capture the frequency content and are widely used as a competitive baseline for sound classification.

    #### Feature Extraction Process

    - **Frame-Based Analysis**: Audio slices are analyzed per frame, with each frame windowed at **23.2 ms** and a 50% overlap between frames.

    - **Frequency Bands**: Computed across **40 Mel bands** from 0 to 22050 Hz.

    - **Coefficients**: The first **25 MFCC coefficients** are extracted for each frame to summarize the sound’s spectral properties.

    #### Summary Statistics for Each Slice

    - Extracted MFCC values are summarized per slice using **minimum, maximum, median, mean, variance, skewness, kurtosis**, and the **mean and variance of the first and second derivatives**.

    - This results in a **225-dimensional feature vector** per audio slice, capturing comprehensive details of the sound.

    #### Tool Used

    - The **Essentia audio analysis library** was employed for MFCC extraction, enabling efficient processing of the audio dataset.

    ### Experimental Setup

    #### Software and Tools

    - Experiments were conducted using **Weka**, a data mining software suite.

    - Every experiment was run with **10-fold cross-validation** to ensure reliable performance metrics.

    ####  Feature Selection

    - Within each fold, **correlation-based attribute selection** was used to reduce the risk of overfitting and improve generalization on the training data.

    #### Classifier Parameters

    - Default parameter settings were used for each classification algorithm, as the main focus was to understand dataset characteristics rather than optimizing model accuracy.

    #### Fold Creation

    - To avoid artificially inflated accuracy, slices from the same original recording were kept within the same fold.

    - This approach ensured no data leakage between training and testing sets by keeping slices from the same source in one fold only.

    - UrbanSound8K was divided into 10 folds, each containing audio slices grouped accordingly, which allows for unbiased and comparable results.



    - Classification accuracy assessed based on:

        - **Temporal scales:** Shorter slices reduced performance.

        - **Class-specific accuracy and salience:** Background sounds reduced accuracy.

    ### Results

    #### Slice Duration and Classification Performance

    - The experiment evaluated how varying maximum slice durations (from **10 seconds to 1 second**) affected classification accuracy.

    - Five classifiers were tested: **Decision Tree (J48), k-Nearest Neighbors (k=5), Random Forest (500 trees), Support Vector Machine (SVM) with RBF kernel**, and **ZeroR** (baseline).

    - Accuracy remained stable between 10 to 6 seconds, but began to decrease below 6 seconds.

    - The **SVM** classifier achieved the highest accuracy, showing that 4-second slices were optimal for UrbanSound8K.

    #### Per-Class Accuracy

    - Different sound classes exhibited varying accuracy based on slice duration:
        - Short-duration sounds (e.g., **gun shot** and **siren**) maintained accuracy even with shorter slices.

        - Long-duration sounds (e.g., **street music** and **children playing**) performed better with longer slices, suggesting that multi-scale analysis may benefit urban sound research.

    #### Confusion Matrix Observations

    - The SVM classifier showed specific **confusions** between similar-sounding classes:

        - **Air conditioners** and **idling engines**
        - **Jackhammers** and **drills**

        - **Children playing** and **street music**

        - These confusions are likely due to **similar timbre**, and future research could focus on features that better distinguish these sounds.

    #### Salience and Accuracy

    - Each sound occurrence was labeled for **salience** (foreground vs. background).

    - The classifier performed better on **foreground sounds** with minimal background interference, except for **sirens**, which have distinct frequencies that help in classification even with background noise.
    
    - Results highlight the challenge of identifying sounds amidst background noise, suggesting future work on robustness against noise interference.

