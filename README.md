
# 🍷 Red Wine Quality Prediction using Random Forest

## 📌 Project Overview

This project predicts the **quality of red wine** based on its physicochemical features such as acidity,
sugar content, pH, alcohol, etc. We use the **Random Forest Classifier**, a powerful ensemble learning method,
to classify wine samples into different quality categories (typically scored from 3 to 8).

---

## 🎯 Problem Type

**Multiclass Classification**

* **Goal:** Predict wine quality score (integer value)
* **Target Variable:** `quality`

---

## 🧪 Dataset

* **Source:** UCI Machine Learning Repository
  [Red Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
* **Records:** 1,599 samples
* **Features:** 11 chemical properties of wine (e.g., acidity, alcohol, sugar)

---

## 🧰 Tools and Libraries Used

| Purpose          | Libraries                                  |
| ---------------- | ------------------------------------------ |
| Data Handling    | `pandas`, `numpy`                          |
| Visualization    | `matplotlib`, `seaborn`                    |
| Model Building   | `sklearn.ensemble.RandomForestClassifier`  |
| Model Evaluation | `sklearn.metrics`                          |
| Data Splitting   | `sklearn.model_selection.train_test_split` |

---

## 🧪 Features Used

* `fixed acidity`
* `volatile acidity`
* `citric acid`
* `residual sugar`
* `chlorides`
* `free sulfur dioxide`
* `total sulfur dioxide`
* `density`
* `pH`
* `sulphates`
* `alcohol`

---

## 🔍 Steps Followed

1. **Load the Data** using pandas.
2. **Explore & Clean the Data** (check for missing values, duplicates).
3. **Split the Data** into features (X) and target (y), and then into train-test sets.
4. **Train the Model** using RandomForestClassifier.
5. **Make Predictions** on the test set.
6. **Evaluate the Model** using accuracy, confusion matrix, and classification report.

---

## 📊 Model Performance

| Metric           | Score (Example)                         |
| ---------------- | --------------------------------------- |
| Accuracy         | 0.72                                    |
| F1-score         | Varies per class                        |
| Confusion Matrix | Shows predictions across quality levels |

(Note: Results may vary based on parameter tuning and class balancing)

---

## 💡 Why Random Forest?

* It combines multiple decision trees to improve accuracy.
* Reduces overfitting common in single decision trees.
* Works well with both categorical and numerical data.

---

## ✅ Conclusion

The Random Forest model performs reasonably well on red wine data, identifying patterns in chemical composition that
relate to wine quality. With proper tuning, the model can assist in wine grading automation or quality control in production.

---
