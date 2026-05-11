import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump

# -----------------------------
# Dataset 불러오기
# -----------------------------

df = pd.read_csv("data/simulated_memory_error.csv")

# -----------------------------
# 입력(X), 출력(y) 분리
# -----------------------------

X = df[[
    "temperature_c",
    "voltage_v",
    "refresh_interval_ms",
    "timing_margin_ns",
    "noise_level",
    "leakage_factor"
]]

y = df["error_label"]

# -----------------------------
# Train / Test 분리
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# 모델 생성 및 학습
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# 예측
# -----------------------------

y_pred = model.predict(X_test)

# -----------------------------
# 성능 평가
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# 모델 저장
# -----------------------------

dump(model, "results/dram_error_model.joblib")

print("\nModel saved successfully.")
