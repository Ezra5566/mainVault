# AI Research & Fundamentals

## Core AI Concepts

### Machine Learning Types
- **Supervised Learning** - Learning from labeled data
  - Classification (spam detection, image recognition)
  - Regression (price prediction, trend forecasting)
- **Unsupervised Learning** - Finding patterns in unlabeled data
  - Clustering (customer segmentation, anomaly detection)
  - Dimensionality reduction (PCA, t-SNE)
- **Reinforcement Learning** - Learning through interaction
  - Agent-environment interactions
  - Reward-based optimization
  - Applications: game AI, robotics, recommendation systems

### Deep Learning Basics
- **Neural Networks** - Interconnected nodes inspired by neurons
- **Activation Functions** - ReLU, Sigmoid, Tanh, Softmax
- **Loss Functions** - MSE, Cross-entropy, Hinge loss
- **Optimization** - Gradient descent, Adam, RMSprop
- **Architecture Types**
  - Feedforward Networks
  - Convolutional Neural Networks (CNNs) - Image processing
  - Recurrent Neural Networks (RNNs) - Sequential data
  - Transformers - Attention mechanism, NLP breakthrough

### Key Mathematical Foundations
- **Linear Algebra** - Vectors, matrices, eigenvalues, SVD
- **Calculus** - Derivatives, gradients, chain rule, partial derivatives
- **Probability & Statistics** - Distributions, Bayes theorem, hypothesis testing
- **Information Theory** - Entropy, KL divergence, mutual information

## Natural Language Processing (NLP)

### Text Processing Pipeline
1. **Tokenization** - Splitting text into words/subwords
2. **Normalization** - Lowercasing, stemming, lemmatization
3. **Vectorization** - Converting text to numerical representations
   - Bag of Words, TF-IDF
   - Word Embeddings (Word2Vec, GloVe, FastText)
   - Contextual Embeddings (BERT, GPT, ELMo)

### Core NLP Tasks
- **Text Classification** - Sentiment analysis, topic labeling
- **Named Entity Recognition (NER)** - Identifying persons, organizations, locations
- **Part-of-Speech Tagging** - Grammatical role labeling
- **Machine Translation** - Language-to-language translation
- **Question Answering** - Extractive and generative QA
- **Text Summarization** - Extractive and abstractive summarization

### Transformer Architecture
- **Self-Attention Mechanism** - Weighing importance of different words
- **Positional Encoding** - Adding sequence order information
- **Encoder-Decoder Structure** - For seq2seq tasks
- **Decoder-Only** - For autoregressive generation (GPT-style)
- **Encoder-Only** - For understanding tasks (BERT-style)

## Computer Vision

### Image Processing Fundamentals
- **Pixel Operations** - Brightness, contrast, thresholding
- **Filtering** - Blurring, sharpening, edge detection
- **Feature Detection** - Corners, edges, blobs (SIFT, SURF, ORB)
- **Image Segmentation** - Partitioning image into meaningful regions

### Deep Learning for Vision
- **Convolutional Layers** - Feature extraction through filters
- **Pooling Layers** - Spatial downsampling (max, average)
- **Common Architectures**
  - LeNet - Early digit recognition
  - AlexNet - ImageNet breakthrough (2012)
  - VGG - Simplicity and depth
  - ResNet - Skip connections for very deep networks
  - YOLO/SSD - Real-time object detection
  - U-Net - Biomedical image segmentation

### Vision Tasks
- **Image Classification** - What is in the image?
- **Object Detection** - Where are objects and what are they?
- **Instance Segmentation** - Precise object boundaries
- **Semantic Segmentation** - Pixel-level labeling
- **Face Recognition** - Identity verification
- **Image Generation** - GANs, VAEs, Diffusion models

## Reinforcement Learning

### RL Framework
- **Agent** - Learner and decision maker
- **Environment** - What the agent interacts with
- **State** - Current situation representation
- **Action** - What the agent can do
- **Reward** - Feedback from environment
- **Policy** - Strategy for choosing actions
- **Value Function** - Expected future reward

### Key Algorithms
- **Q-Learning** - Value-based, off-policy TD learning
- **SARSA** - Value-based, on-policy TD learning
- **Policy Gradient** - Direct policy optimization (REINFORCE)
- **Actor-Critic** - Combines value and policy methods
- **Deep Q-Network (DQN)** - Q-learning with neural networks
- **Proximal Policy Optimization (PPO)** - Stable policy gradient method
- **Soft Actor-Critic (SAC)** - Maximum entropy RL

### Exploration vs Exploitation
- **Exploration** - Trying new actions to discover rewards
- **Exploitation** - Using known good actions to maximize reward
- **Strategies**: Epsilon-greedy, UCB, Thompson sampling, Boltzmann exploration

## AI Ethics & Safety

### Key Concerns
- **Bias & Fairness** - Algorithmic discrimination
- **Transparency & Explainability** - Black box problem
- **Privacy** - Data protection and surveillance
- **Accountability** - Who is responsible for AI decisions?
- **Safety** - Unintended consequences and harmful outputs
- **Job Displacement** - Economic impact of automation

### Best Practices
- **Data Quality** - Representative, unbiased datasets
- **Model Auditing** - Regular fairness and performance checks
- **Human-in-the-Loop** - Oversight for critical decisions
- **Robustness Testing** - Adversarial examples, edge cases
- **Value Alignment** - Ensuring AI goals align with human values
- **Transparency** - Model cards, datasheets, explainability tools

## Resources for Further Study

### Foundational Texts
- "Artificial Intelligence: A Modern Approach" - Russell & Norvig
- "Deep Learning" - Goodfellow, Bengio, Courville
- "Pattern Recognition and Machine Learning" - Bishop
- "Reinforcement Learning: An Introduction" - Sutton & Barto

### Online Courses
- Stanford CS229 (Machine Learning)
- MIT 6.867 (Machine Learning)
- CS231n (Convolutional Neural Networks for Visual Recognition)
- CS224n (Natural Language Processing with Deep Learning)
- Deep Learning Specialization (Andrew Ng)

### Research Venues
- Conferences: NeurIPS, ICML, ICLR, CVPR, ACL, EMNLP
- Journals: JMLR, TPAMI, IEEE TNNLS
- Preprint Servers: arXiv (stat.ML, cs.LG, cs.CV, cs.CL)

### Tools & Frameworks
- **Python Libraries**: TensorFlow, PyTorch, JAX, Scikit-learn
- **NLP**: Hugging Face Transformers, SpaCy, NLTK
- **Vision**: OpenCV, Detectron2, MMDetection
- **RL**: Stable Baselines3, RLlib, Gym
- **Experiment Tracking**: Weights & Biases, MLflow, TensorBoard

### Community & Practice
- Kaggle competitions
- GitHub repositories
- AI safety forums (Alignment Forum, LessWrong)
- Local AI/ML meetups
- Hackathons and bootcamps

---

*Related Notes:*
- [[03-Resources/Knowledge Management System]]
- [[06-Math/Mathematics for ML]]
- [[07-Cybersecurity/AI Security]]
- [[09-Knowledge/Interdisciplinary Applications]]

*Last updated: May 14, 2026*