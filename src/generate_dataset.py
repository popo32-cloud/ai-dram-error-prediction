import numpy as np
import pandas as pd

# 재현성을 위한 seed 고정
np.random.seed(42)

# 샘플 개수
NUM_SAMPLES = 10000

# -----------------------------
# 입력 변수 생성
# -----------------------------

temperature_c = np.random.uniform(20, 100, NUM_SAMPLES)

voltage_v = np.random.uniform(0.9, 1.3, NUM_SAMPLES)

refresh_interval_ms = np.random.uniform(1, 10, NUM_SAMPLES)

timing_margin_ns = np.random.uniform(0.1, 5.0, NUM_SAMPLES)

noise_level = np.random.uniform(0, 1, NUM_SAMPLES)

leakage_factor = np.random.uniform(0, 1, NUM_SAMPLES)

# -----------------------------
# Error probability 계산
# -----------------------------
# 직관 기반 단순 모델
# 높은 온도 ↑
# 낮은 전압 ↓
# 긴 refresh interval ↑
# 작은 timing margin ↓
# 높은 noise ↑
# 높은 leakage ↑

error_score = (
    0.03 * (temperature_c - 20)
    + 2.0 * (1.3 - voltage_v)
    + 0.25 * refresh_interval_ms
    + 1.5 * (1 / timing_margin_ns)
    + 2.0 * noise_level
    + 1.5 * leakage_factor
)

# sigmoid 함수로 probability 변환
error_probability = 1 / (1 + np.exp(-error_score + 5))

# binary label 생성
error_label = np.random.binomial(1, error_probability)

# -----------------------------
# DataFrame 생성
# -----------------------------

df = pd.DataFrame({
    "temperature_c": temperature_c,
    "voltage_v": voltage_v,
    "refresh_interval_ms": refresh_interval_ms,
    "timing_margin_ns": timing_margin_ns,
    "noise_level": noise_level,
    "leakage_factor": leakage_factor,
    "error_probability": error_probability,
    "error_label": error_label
})

# -----------------------------
# CSV 저장
# -----------------------------

df.to_csv("data/simulated_memory_error.csv", index=False)

print("Dataset generated successfully.")
print(df.head())
