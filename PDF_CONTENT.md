
---
## Page 1

Performance Analysis of Logistic Regression on
Encrypted Data Using CKKS Scheme in Microsoft
SEAL
Merve Dönmez
Department of Computer Engineering,
Gebze TechnicalUniversity
Gebze, Turkey
m.donmez2024@gtu.edu.tr
Abstract—This study investigates the applicability of machine data without decryption. Fully Homomorphic Encryption
learning algorithms to encrypted data while preserving data (FHE), in particular, supports the execution of basic arithmetic
privacy. Homomorphic Encryption (HE), a modern
operations—such as addition and multiplication—on
cryptographic approach, enables computations on encrypted data
ciphertexts, ensuring data privacy throughout the computation
without requiring decryption. In this context, the Microsoft SEAL
process [4]–[5].
(Simple Encrypted Arithmetic Library) and the CKKS (Cheon-
Several open-source HE libraries have been developed in
Kim-Kim-Song) encryption scheme were utilized to implement a
Logistic Regression model. The model was evaluated on both recent years, including HElib [6], TFHE [7], PALISADE [8],
encrypted and unencrypted datasets, and its performance was OpenFHE [9], and Microsoft SEAL [10]. These libraries differ
compared in terms of classification accuracy, computation time, in their supported encryption schemes, performance
and ROC-AUC metrics. characteristics, and ease of use. Microsoft SEAL, for instance,
The dataset employed in this study is the “Default of Credit supports three schemes: BFV and BGV for exact computations
Card Clients” from the UCI Machine Learning Repository [1],
on integers, and CKKS for approximate arithmetic operations
which consists of real-world tabular financial records. Unlike
on real numbers [11]–[13]. The CKKS scheme is particularly
previous works that predominantly rely on image-based datasets
well suited for numerical applications such as machine
such as MNIST or CIFAR-10, this study addresses a more realistic
learning. However, due to the increased computational
classification task under encrypted computation. The results
indicate that while the classification accuracy is largely overhead and memory consumption associated with
maintained when using encrypted data, the total computation time homomorphic encryption compared to plaintext operations,
significantly increases due to the encryption and decryption evaluating its practical applicability requires detailed
processes. Overall, this study offers a comprehensive empirical performance analysis.
analysis of homomorphic classification under the CKKS scheme
and contributes a distinct evaluation perspective to the existing
literature by focusing on structured real-world data.
Index Terms—Privacy-preserving machine learning,
Homomorphic encryption, CKKS, Microsoft SEAL, Logistic
Regression
I. INTRODUCTION
As machine learning applications increasingly involve
processing users’ personal data, data privacy and security have
become critical concerns. In cloud-based environments,
sharing data for model training or inference poses significant
risks, such as the leakage or exposure of sensitive information
[2], [3]. To address these concerns, Homomorphic Encryption
(HE) has emerged as a modern cryptographic approach that Figure 1: Fully Homomorphic Encryption in the Client/Server
enables computations to be performed directly on encrypted Applications [17]
---
## Page 2

In this study, we implement a Logistic Regression model • HomAdd(ct, t): Performs a homomorphic addition
using the CKKS scheme provided by the Microsoft SEAL operation (ct + t). In CKKS, the operands must be
library. The experiment is conducted on the “Default of Credit aligned in both scale and level for addition to be valid.
Card Clients” dataset obtained from the UCI Machine Learning • HomMul(ct, t): Performs a homomorphic
Repository [1]. Unlike image-based datasets commonly used in multiplication operation (ct × t). After multiplication,
previous studies (e.g., MNIST, CIFAR-10), this real-world, rescaling is typically required to manage noise and
tabular financial dataset provides a more practical and maintain computational stability.
generalized classification scenario for homomorphic • Rescale(ct): Reduces the scale of the ciphertext ct,
encryption applications.
enabling continued computation while keeping the
The objective of this study is to evaluate the performance
noise growth under control [14].
differences between encrypted and unencrypted data in terms
of accuracy, computation time, and feasibility, thereby
C. Microsoft SEAL Library
assessing the usability of CKKS-based classification models.
Although prior literature extensively evaluates HE libraries and
Microsoft SEAL is an open-source and widely adopted
deep learning models, there is limited research on classical
homomorphic encryption (HE) library developed by Microsoft
machine learning algorithms—particularly logistic
Research [10]. It is distinguished by its ease of use,
regression—under CKKS encryption. Therefore, this work
comprehensive documentation, and robust security parameters.
aims to fill that gap by offering a practical and measurable
SEAL supports three HE schemes: BFV, BGV, and CKKS—
contribution to the field.
the latter being particularly suitable for approximate numerical
computations [10]. In this study, the CKKS scheme was chosen
due to its compatibility with floating-point data.
II. BACKGROUND
However, SEAL requires the user to explicitly specify
relinearization and rescaling operations. While higher-level
A. Homomorphic Encryption (HE) Overview tools such as Microsoft EVA can automate these steps, they
may introduce additional runtime overhead due to message
Homomorphic Encryption (HE) is a cryptographic method encoding processes [16].
that allows computations to be performed directly on encrypted Because the CKKS scheme may result in scale mismatches
data without requiring decryption. This feature is particularly between operations, SEAL users must manually align the scales
advantageous for applications in which data privacy is before performing additions and multiplications. In contrast,
paramount, such as in privacy-preserving machine learning [2], libraries like OpenFHE are capable of handling these
[3]. With HE, users can submit encrypted data to a server, adjustments automatically [15].
which then performs computations without accessing the
underlying plaintext.
D. Encrypted Logistic Regression
Among various HE schemes, one of the most widely adopted
for approximate arithmetic is the CKKS (Cheon–Kim–Kim–
The logistic regression model performs classification by
Song) scheme, proposed by Cheon et al. [6]. CKKS enables
applying the sigmoid (logistic) activation function to the inner
operations on floating-point data by representing complex
product of the input features and the weight vector, thereby
numbers approximately in fixed-point format. This results in
mapping the result to the range [0,1]. The model’s training
minor decryption errors, but such inaccuracies can be
phase relies on parameter updates via the gradient ascent
minimized with proper parameter tuning [13].
method [17].
To improve computational efficiency, Cheon and colleagues
developed a Residue Number System (RNS) variant known as
FullRNS-CKKS. This version significantly reduces execution
time compared to the original CKKS scheme [13].
This formulation involves addition, multiplication,
B. Basic Components of the CKKS Scheme subtraction, and the sigmoid function. However, since
homomorphic encryption does not natively support non-linear
The CKKS scheme is particularly effective in applications functions such as the sigmoid, these functions must be
where floating-point computations are prevalent, such as approximated using polynomials [17].
machine learning. The fundamental concepts and operations of
the scheme are summarized below:
• scale(t): Returns the bit-length of the fractional part of
This study, the training phase of the logistic regression model
the element t. Initially, this is referred to as the scale
was performed in the plaintext domain, whereas the inference
factor ∆.
phase was executed using encrypted data. This setup enables a
• level(t): Indicates the remaining number of
comparative evaluation of inference accuracy, execution time,
homomorphic multiplications allowed for the element
and memory usage between encrypted (CKKS-based) and
t. The level decreases by one after each multiplication.
conventional (unencrypted) methods.
---
## Page 3

E. ROC Curve: Performance Evaluation Metric for model training and inference with HE support. However,
most of these studies do not evaluate the performance of
One of the most widely used metrics for evaluating model classical models such as logistic regression.
performance is the Receiver Operating Characteristic (ROC) Among the limited studies on homomorphic logistic
curve. The ROC curve provides a two-dimensional regression, Lee et al. [17] demonstrated an inference pipeline
visualization of a classification model’s performance as a on encrypted data under the CKKS scheme, where the sigmoid
function of its decision threshold. The X-axis represents the function was approximated using a polynomial. However,
False Positive Rate (FPR), while the Y-axis represents the True comprehensive classification metrics such as ROC curves were
Positive Rate (TPR). These values are directly related to not included in their evaluation.
fundamental metrics such as sensitivity and specificity [18], In this context, the present study offers a novel contribution
[19]. by implementing logistic regression inference on encrypted
The ROC curve offers an advantage in that it evaluates model data using the CKKS scheme via PySEAL. The model’s
performance independently of class distribution, prior performance is evaluated through various metrics including
probability, or misclassification cost. It is particularly valuable ROC curves, accuracy, processing time, and memory usage.
in scenarios involving class imbalance, where traditional This work is among the few that not only assess the efficiency
metrics such as accuracy or error rate may be insufficient [20]. of primitive HE operations but also provide a practical analysis
of how a classical classification algorithm behaves on
Figure 2. Confusion matrix with evaluation index [18] encrypted data, accompanied by visual performance
representations.
IV. COMPARISON METHOD OF HOMOMORPHIC
ENCRYPTION LIBRARIES
A. Overview
The objective of this study is to investigate performance
differences between encrypted and unencrypted data
The Area Under the Curve (AUC) provides a scalar summary processing in the context of homomorphic encryption (HE),
of the ROC curve, quantifying the model’s overall specifically by applying a Logistic Regression model using the
classification ability. An AUC value closer to 1 indicates better Microsoft SEAL library and the CKKS encryption scheme. The
model performance [19]. Previous studies in the literature have methodology follows these main steps:
demonstrated that AUC is a more consistent and robust
performance metric compared to traditional measures.
• The CKKS encryption scheme was selected due to its
support for approximate computations on floating-
point numbers, making it well-suited for machine
III. RELATED WORK learning applications [13].
In recent years, numerous open-source libraries have been • A Logistic Regression model was trained and tested
developed in the field of homomorphic encryption (HE), and on both encrypted and unencrypted datasets.
their performance has been evaluated based on various criteria. • Performance evaluations were conducted using key
In 2022, Doan et al. [21] compared the performance of metrics such as accuracy, encryption and decryption
homomorphic addition and multiplication operations using time, and memory consumption.
SEAL, PALISADE, and HElib libraries under the CKKS • ROC curves were plotted based on the prediction
scheme. Their results indicated that SEAL was significantly probabilities obtained from both encrypted and
faster than the others, particularly in multiplication operations. unencrypted data.
In the same year, Takeshita et al. [22] introduced a profiling
framework named HEProfiler to benchmark CKKS-based This approach was inspired by the work of Takeshita et al.
libraries—SEAL, PALISADE, HElib, and HEAAN— [23], who conducted a comparative performance analysis of
considering primitive operations, bootstrapping costs, and SEAL, OpenFHE, and HElib libraries using a CNN model.
multi-threading capabilities. Their findings highlighted However, the present study distinguishes itself by focusing on
SEAL’s superior performance in low-depth computations. a classical machine learning algorithm—Logistic Regression—
Microsoft SEAL supports three major HE schemes: BFV, and by providing a more detailed evaluation of classification
BGV, and CKKS [8]. Among them, CKKS is particularly metrics such as ROC curves and AUC values.
suited for machine learning tasks involving floating-point data
[23]. SEAL-based libraries such as TenSEAL [11] enable
encrypted tensor operations through Python interfaces, while
frameworks like Concrete ML [24] provide more intuitive APIs
---
## Page 4

B. Dataset and Homomorphic Encryption Libraries
Table 1. Comparison of Homomorphic Encryption Libraries and Datasets Used in Recent Studies
Study and Year Used Library(ies) Encryption Evaluation Machine Dataset(s)
Scheme(s) Metrics Learning
Model
Doan et al. (2022) Microsoft SEAL BFV, CKKS Homomorphic Add CNN Synthetic / Low-
/ Multiply Timing Level Benchmarks
Takeshita et al. SEAL, HElib, CKKS Bootstrapping, CNN MNIST, CIFAR-10
(2022) OpenFHE, HEAAN multithreading,
latency
This Paper (2025) Microsoft SEAL CKKS Accuracy, Timing, Logistic Default of Credit
(PySEAL) ROC Curve Regression Card Clients (UCI)
In this study, the “Default of Credit Card Clients” dataset
from the UCI Machine Learning Repository was utilized [1].
Algorithm 1. Encryption Process Using Microsoft SEAL with
This dataset consists of 23 features and binary class labels
CKKS Scheme [13]
based on real-world financial records. Unlike studies that focus
on deep learning models, this work emphasizes a classical
machine learning approach by implementing the Logistic 1. Define encryption parameters:
Regression algorithm. Data encryption was performed using Input: Plaintext numeric dataset data
the PySEAL library with the Python programming language. Output: Encrypted dataset encrypted_data, public/private
keys, encoder configuration
C. Experiment Environment and Conditions
parms ← EncryptionParameters(scheme_type.ckks)
parms.set_poly_modulus_degree(8192)
• Homomorphic Encryption Library Used: Microsoft SEAL parms.set_coeff_modulus(CoeffModulus.Create(8192,
(via PySEAL interface)
[60, 40, 40, 60]))
• Encryption Scheme: CKKS [13]
// The polynomial modulus degree and coefficient modulus
• Encryption Parameters:
parameters are defined for the CKKS scheme.
- Polynomial modulus degree: 8192
- Coefficient modulus: [60, 40, 40, 60]
2. Create context and keys:
- Scale: 2^40
context ← SEALContext(parms)
keygen ← KeyGenerator(context)
Key generation, encryption, and decryption processes were
public_key ← keygen.create_public_key()
carried out using PySEAL, the Python wrapper for the
secret_key ← keygen.secret_key()
Microsoft SEAL library. The CKKS scheme was chosen for
// The public and secret keys required for encryption and
this study due to its ability to perform approximate decryption are generated.
computations, making it particularly suitable for machine
learning models that operate on floating-point data [13]. The
3. Initialize encoder and encryptor:
scheme supports homomorphic operations through
encoder ← CKKSEncoder(context)
mechanisms such as scaling, rescaling, and level management.
encryptor ← Encryptor(context, public_key)
The dataset [1] was split into training and testing subsets.
scale ← 2^40
First, inference was performed on plaintext data. Then, the
//A CKKS encoder and an appropriate scale factor are
same data were encoded in CKKS format, encrypted, and tested
initialized.
again using a Logistic Regression model on encrypted inputs.
Classification metrics and ROC curves obtained from both
4. Encode and encrypt the input data:
scenarios were analyzed and compared.
for row in data:
The following section outlines the CKKS encryption and
plain ← encoder.encode(row, scale)
decryption procedures step-by-step. These algorithms are encrypted_row ← encryptor.encrypt(plain)
provided to offer a formal academic description of operations
encrypted_data.append(encrypted_row)
performed using the SEAL API.
//The data are encoded and encrypted, then stored in encrypted
format.
### Table 4.1

| Study and Year | Used Library(ies) | Encryption
Scheme(s) | Evaluation
Metrics | Machine
Learning
Model | Dataset(s) |
|---|---|---|---|---|---|
| Doan et al. (2022) | Microsoft SEAL | BFV, CKKS | Homomorphic Add
/ Multiply Timing | CNN | Synthetic / Low-
Level Benchmarks |
| Takeshita et al.
(2022) | SEAL, HElib,
OpenFHE, HEAAN | CKKS | Bootstrapping,
multithreading,
latency | CNN | MNIST, CIFAR-10 |
| This Paper (2025) | Microsoft SEAL
(PySEAL) | CKKS | Accuracy, Timing,
ROC Curve | Logistic
Regression | Default of Credit
Card Clients (UCI) |


---
## Page 5

that the CKKS encryption scheme successfully preserves the
integrity of the data without degrading model accuracy.
Algorithm 2. Decryption Process Using Microsoft SEAL with Furthermore, the findings suggest that the ROC curve remains
CKKS Scheme [10] a dependable evaluation method in homomorphic classification
scenarios.
Input: Encrypted dataset encrypted_data, secret key, and
encoder
Output: Decoded plaintext data
V. RESULT AND DISCUSSION
1. Initialize decryptor: In this section, the outputs of the Logistic Regression model
decryptor ← Decryptor(context, secret_key) applied to encrypted and unencrypted data are comparatively
analyzed. The encryption processes were carried out using the
2. Decrypt and decode ciphertexts: Microsoft SEAL library and the CKKS encryption scheme. The
for encrypted_row in encrypted_data: parameters used in the implementation were set as follows: a
plain ← decryptor.decrypt(encrypted_row) polynomial modulus degree of 8192, a scale value of 2⁴⁰, and a
decoded_row ← encoder.decode(plain) coefficient modulus of [60, 40, 40, 60]. The CKKS scheme is
append decoded_row to output widely adopted in machine learning applications due to its
ability to perform approximate arithmetic operations on
floating-point numbers [10], [13].
D. Evaluation Metric
A. Performance Comparison Between Encrypted and
This study presents a comparative performance analysis of Unencrypted Data
machine learning algorithms applied to both encrypted and
unencrypted data. The model was trained and tested using The Logistic Regression model was trained and tested using
identical parameters for both data types, enabling direct identical parameters on both encrypted and unencrypted
observation of the impact of encryption on classification datasets. A summary of the comparative results is presented
performance [13], [23]. below:
The comparison was conducted using the following metrics: • Accuracy: The classification accuracy was measured
Accuracy: Overall classification performance of the model. as 80.15% for both encrypted and unencrypted data.
Confusion Matrix: Analysis of true and false classifications. • Confusion Matrix and Classification Report: The
Classification Report: Includes detailed metrics such as confusion matrix and classification metrics were
precision, recall, and F1-score. identical in both scenarios. This indicates that the
Timing Measurements: CKKS encryption scheme implemented via the
- Encryption time Microsoft SEAL library preserved the mathematical
- Decryption and inference time structure of the data and did not compromise the
- Inference time with unencrypted data deterministic behavior of the model.
ROC Curve and AUC (Area Under Curve): Assessment of the • Timing Measurements:
model’s discriminative ability [17]. o Prediction time with unencrypted data: 1.07 seconds
The results showed that the accuracy, confusion matrix, and o Encryption time: 11.99 seconds
ROC curve obtained from encrypted data were identical to o Decryption and prediction time: 3.38 seconds
those from unencrypted data. This finding confirms that
homomorphic encryption with the CKKS scheme preserves the These findings show that while encryption and decryption
mathematical structure of the data and does not compromise the processes significantly increase computational time, they do
model’s deterministic behavior [13]. not negatively affect classification accuracy. The ROC curves
The Receiver Operating Characteristic (ROC) curve offers a and AUC (Area Under the Curve) values obtained from
robust method for evaluating model performance independent encrypted and unencrypted data were identical, confirming that
of the classifier. It is derived from the True Positive Rate (TPR) the model’s predictive performance remained unchanged.
and False Positive Rate (FPR), which are calculated based on These results highlight the effectiveness of homomorphic
the model’s output thresholds. These metrics are unaffected by encryption in preserving model accuracy [10], [13], [24].
class distribution, prior probabilities, or the type of
classification algorithm, making ROC a suitable tool for fair Unencrypted Data:
comparisons across different models [18], [19].
• Accuracy: 0.8015
A convex ROC curve indicates strong classification
• Confusion Matrix: [[4552 135]
performance and provides reliable evaluation, especially for
[1056 257]]
models with unknown internal structures [17]. In this study,
• Processing Time: 1.07 seconds
ROC curves were plotted and AUC values calculated for the
Logistic Regression model using both encrypted and
unencrypted data. The curves overlapped perfectly, confirming
---
## Page 6

Classification Report: Figure 4: ROC Curve for encrypted data
precision recall f1-score support
0 0.81 0.97 0.88 4687
1 0.66 0.20 0.30 1313
accuracy 0.80 6000
macro avg 0.73 0.58 0.59 6000
weighted avg 0.78 0.80 0.76 6000
Encrypted Data:
• Accuracy: 0.8015
• Confusion Matrix: [[4552 135]
[1056 257]]
• Encryption Time: 11.99 seconds
C. Discussion on Trade-offs
• Decryption and Prediction Time: 3.38 seconds
The evaluations indicate that the primary advantage of
Classification Report:
employing homomorphic encryption lies in its ability to
precision recall f1-score support
preserve data privacy; however, this comes at a notable cost in
0 0.81 0.97 0.88 4687 terms of computational time. Specifically, the encryption and
decryption processes resulted in approximately 15 seconds of
1 0.66 0.20 0.30 1313
additional processing time. Although memory usage was not
accuracy 0.80 6000
directly measured, similar studies in the literature report that
macro avg 0.73 0.58 0.59 6000 homomorphic encryption applications generally entail higher
memory consumption [21], [23].
weighted avg 0.78 0.80 0.76 6000
Furthermore, unlike widely used image-based datasets such
as MNIST or CIFAR-10 in previous research, this study
employed the “Default of Credit Card Clients” dataset [15],
B. Interpretation of ROC Curve
which consists of real-world, numerical financial data. This
distinction highlights the study’s valuable contribution by
ROC curves were plotted based on the model’s prediction
demonstrating the applicability of homomorphic encryption on
outputs to enable visual comparison. It was observed that the
alternative types of datasets.
ROC curves generated from predictions on both encrypted and
unencrypted data overlapped completely. This outcome can be
attributed to the deterministic nature of the Logistic Regression
algorithm and the CKKS encryption scheme’s ability to VI. C ONCLUSION
preserve the arithmetic structure of encrypted data with high
This study aimed to evaluate the performance of the Logistic
accuracy [13], [17].
Regression algorithm on encrypted data using the CKKS
scheme and the Microsoft SEAL library, which are based on
Figure 3: ROC Curve for unencrypted data
homomorphic encryption methods. The experimental results
demonstrated that the accuracy of models trained on encrypted
and unencrypted data was identical, and the ROC curves
overlapped perfectly. This suggests that, despite the
approximate arithmetic structure of the CKKS scheme, it
largely preserves the mathematical properties of the data and
does not disrupt the deterministic nature of the model [13].
However, performance analysis revealed that working with
encrypted data incurs a significant cost in terms of processing
time. Specifically, the encryption and decryption steps added
an additional delay of approximately 15 seconds to the
prediction time. These results are consistent with the high
computational costs reported in the literature for homomorphic
encryption applications [21].
### Table 6.1

|  | precision | recall | f1-score | support |
|---|---|---|---|---|
| 0 | 0.81 | 0.97 | 0.88 | 4687 |
| 1 | 0.66 | 0.20 | 0.30 | 1313 |
| accuracy |  |  | 0.80 | 6000 |
| macro avg | 0.73 | 0.58 | 0.59 | 6000 |
| weighted avg | 0.78 | 0.80 | 0.76 | 6000 |


### Table 6.2

|  | precision | recall |
|---|---|---|
| 0 | 0.81 | 0.97 |
| 1 | 0.66 | 0.20 |
| accuracy |  |  |
| macro avg | 0.73 | 0.58 |
| weighted avg | 0.78 | 0.80 |


### Table 6.3

| support |
|---|
| 4687 |
| 1313 |
| 6000 |
| 6000 |
| 6000 |


---
## Page 7

The ease of use, open-source nature, and comprehensive Triplett, V. Vaikuntanathan, and V. Zucca, “Openfhe: Open-source fully
documentation of the Microsoft SEAL library provide an homomorphic encryption library,” in Proceedings of the 10th Workshop
on Encrypted Computing Applied Homomorphic Cryptography
accessible environment for researchers, especially beginners in
(WAHC’22). ACM, 2022, pp. 53–63, doi:10.1145/3560827.3563379.
this field. However, topics such as memory usage, performance
[10] “Microsoft SEAL (release 4.0),” https://github.com/Microsoft/SEAL,
in multi-threaded environments, and comparisons between Mar. 2022, Microsoft Research, Redmond, WA.
different encryption schemes were beyond the scope of this [11] Z. Brakerski, C. Gentry, and V. Vaikuntanathan, “(leveled) fully
study. homomorphic encryption without bootstrapping,” in Proceedings of the
3rd Innovations in Theoretical Computer Science Conference (ITCS ’12).
Future work is planned to delve deeper into the following
ACM, 2012, pp. 309–325, doi:10.1145/2090236.2090262.
aspects:
[12] J. H. Cheon, K. Han, A. Kim, M. Kim, and Y. Song, “Bootstrapping for
• Comparison of Different Encryption Schemes (BFV, approximate homomorphic encryption,” in Proceedings of the Advances
BGV): A comparative performance analysis of other in Cryptology–EURO-CRYPT 2018, vol. 10820. LNCS, Springer, 2018,
encryption schemes supported by the SEAL library, in pp. 360–384, doi:10.1007/978-3-319-78381-914.
[13] J. H. Cheon, K. Han, A. Kim, M. Kim, and Y. Song, “A full rns variant
addition to CKKS, using the same data and model.
of approximate homomorphic encryption,” in Proceedings of the Selected
• Memory Usage and System Resource Measurement: Areas in Cryptography – SAC, vol. 11349. LNCS, Springer, 2018, pp.
Evaluation of resource usage, such as memory 347–368, doi:10.1007/978-3-030-10970-7 16.
consumption and CPU utilization, during encrypted [14] H. Zhu, T. Suzuki, and H. Yamana, “Performance Comparison of
Homomorphic Encrypted Convolutional Neural Network Inference
and unencrypted operations.
among HElib, Microsoft SEAL and OpenFHE,” Proc. IEEE Int. Conf. on
• Testing with Real-World Richer Datasets: Analyzing
Computer Science and Educational Informatization (CSEI), pp. 1–6,
the applicability of homomorphic encryption on 2023. [Online]. Available:
various data types, such as image, text, or health data. https://ieeexplore.ieee.org/document/10487709
• Comparison with Other Homomorphic Libraries: A [15] H. Chen, K. Han, Z. Huang, A.
Jalali, and
comparative evaluation of other homomorphic
K. Laine, “Simple encrypted arithmetic library v2.3.0,” vol. 13, 2017.
encryption libraries, such as PALISADE, HElib, and [Online]. Available:
OpenFHE, under the same experimental scenario as https://www.microsoft.com/enus/research/uploads/prod/2017/11/sealma
PySEAL. nual-2-3-1.pdf
[16] R. Dathathri, B. Kostova, O. Saarikivi, W. Dai, K. Laine, and M.
• Model Complexity and Training Phases: Investigating
Musuvathi, “Eva: An encrypted vector arithmetic language and compiler
the feasibility of applying homomorphic encryption to
for efficient homomorphic computation,” in Proceedings of the 41st
more complex models, such as MLPs and CNNs, ACM SIGPLAN Conference on Programming Language Design and
during training and prediction phases. Implementation, ser. PLDI 2020. New York, NY, USA: ACM, 2020, pp.
546–561, doi:10.1145/3385412.3386023.
[17] D. C.-T. Lo, Y. Shi, H. Shahriar, B. Deng, X. Zhang, and M.-L. Chen,
R
EFERENCES “Practical considerations of fully homomorphic encryption in privacy-
preserving machine learning,” in Proc. 2024 IEEE Int. Conf. Big Data
[1] Yeh, I.-C., & Lien, C.-H. “Default of Credit Card Clients Data Set.” UCI (BigData), Seattle, WA, USA, Dec. 2024, pp. 5181–5190, doi:
Machine Learning Repository. [Online]. Available: 10.1109/BigData62323.2024.10825068.
https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients [18] David J Hand,Robert J Till.A simple generalization of the area under the
[2] C. Gentry, “A fully homomorphic encryption scheme,” Ph.D. ROC curve for multiple class classification problems[J].Machine
dissertation, Stanford University, Stanford, CA, USA, 2009. [Online]. learning,2001,45(2):171-186.
Available: https://crypto.stanford.edu/craig/craig-thesis.pdf [19] Son HK, Yun MJ, Jeon TJ, et al. ROC analysis of ordered subset
[3] S. Halevi and V. Shoup, “Design and implementation of helib: a expectation maximization and filtered back projection technique for
homomorphic encryption library,” Cryptology ePrint Archive, Paper FDG-PET in lung cancer. IEEE transactions on Nuclear Science, 2003,
2020/1481, 2020. [Online]. Available: https://eprint.iacr.org/2020/1481 50(1):37-41.
[4] E. Lee, J.-W. Lee, Y.-S. Kim, and J.-S. No, “Optimization of [20] Vladimir Cherkassky, Yunqian Ma. Practical selection of SVM
homomorphic comparison algorithm on rns-ckks scheme,” IEEE Access, parameters and noise estimation for SVM regression [J]. Neural
vol. 10, pp. 26163–26176, 2022. Networks, 2004, 17(1):113-126.
[5] R. Lazzeretti, T. Pignata, and M. Barni, “Piecewise function [21] C. Mouchet, J.-P. Bossuat, J. R. Troncoso-Pastoriza, and J.-P. Hubaux,
approximation with private data,” IEEE Transactions on Information “Lattigo: a multiparty homomorphic encryption library in go,” 2020.
Forensics and Security, vol. 11, no. 3, pp. 642–657, 2016. [Online]. Available:
[6] J. H. Cheon, A. Kim, K. Kim, and Y. Song, “Homomorphic encryption https://api.semanticscholar.org/CorpusID:231609747
for arithmetic of approximate numbers,” in Proceedings of International [22] J. Fan and F. Vercauteren, “Somewhat practical fully homomorphic
Conference on the Theory and Application of Cryptology and Information encryption,” 01 2012. [Online]. Available:
Security 2017, vol. 10624. LNCS, Springer, 2017, pp. 409–437, https://eprint.iacr.org/2012/144
doi:10.1007/978-3-319-70694-8 15. [23] J. Takeshita, N. Koirala, C. McKechney, and T. Jung, “Heprofiler: An in-
[7] I. Chillotti, N. Gama, M. Georgieva, and M. Izabach‘ene, “Tfhe: fast fully depth profiler of approximate homomorphic encryption libraries,” in
homomorphic encryption over the torus,” in Journal of Cryptology, vol. Research Square, 2022, preprint, doi: 10.21203/rs.3.rs-2164106/v1.
33, no. 1. Springer, 2018, pp. 34–91, doi:10.1007/s00145-01909319-x. [24] H. Zhu, T. Suzuki, H. Huang, and H. Yamana, “Performance comparison
[8] Y. Polyakov, R. Rohloff, G. W. Ryan, and D. Cousins., “Palisade lattice of homomorphic encrypted convolutional neural network inference
cryptography library (release 1.11.5).” 2021. [Online]. Available: between microsoft seal and openfhe,” in Proceedings of the 15th Forum
https://palisade-crypto.org/. https://gitlab.com/palisade/palisade- on Data Engineering and Information Management, Tokyo, Japan, 2023.
release//blob/master/doc/palisade manual.pdf [Online]. Available: https://proceedings-
[9] A. A. Badawi, J. Bates, F. Bergamaschi, D. B. Cousins, S. Erabelli, ofdeim.github.io/DEIM2023/5b-9-2.pdf
N. Genise, S. Halevi, H. Hunt, A. Kim, Y. Lee, Z. Liu, D. Micciancio, I.
Quah, Y. Polyakov, S. RV, K. Rohloff, J. Saylor, D. Suponitsky, M.