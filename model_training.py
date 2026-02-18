"""
Model Training Script — Tanzania GDP Predictor (Rebuilt)
Fixes applied:
  1. Deduplicates dataset (removes 200 near-duplicate rows)
  2. Time-based train/test split: train 2000–2019, test 2020–2024
  3. Ridge Regression as primary model (handles multicollinearity)
  4. Decision Tree with depth=4 (honest, non-overfitted)
  5. Saves all artifacts to models/ folder
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

def train_and_save_models(data_path='data/tanzania_gdp_data.csv'):
    print("🚀 Starting model training (rebuilt version)...")
    print("=" * 60)

    # ── Load data ──────────────────────────────────────────────────
    print("\n📊 Loading data...")
    try:
        df = pd.read_csv(data_path)
        print(f"  Raw records: {len(df)}")
    except FileNotFoundError:
        print(f"❌ File not found: {data_path}")
        return

    # ── Deduplicate ────────────────────────────────────────────────
    df = df.drop_duplicates(subset=['Year', 'Quarter'], keep='first').reset_index(drop=True)
    print(f"  After deduplication: {len(df)} unique records")

    # ── Features / target ──────────────────────────────────────────
    feature_cols = [c for c in df.columns if c not in ['GDP_Billion_USD']]
    X = df[feature_cols].copy()
    y = df['GDP_Billion_USD']

    # Fill missing with column median
    for col in X.columns:
        X[col] = X[col].fillna(X[col].median())

    # ── Time-based split ───────────────────────────────────────────
    train_mask = df['Year'] <= 2019
    X_train, X_test = X[train_mask], X[~train_mask]
    y_train, y_test = y[train_mask], y[~train_mask]
    print(f"\n  Train: {len(X_train)} samples (2000–2019)")
    print(f"  Test:  {len(X_test)} samples (2020–2024)")

    # ── Train Ridge ────────────────────────────────────────────────
    print("\n🔵 Training Ridge Regression (alpha=10)...")
    ridge = Ridge(alpha=10)
    ridge.fit(X_train, y_train)

    ridge_train_r2   = r2_score(y_train, ridge.predict(X_train))
    ridge_test_r2    = r2_score(y_test,  ridge.predict(X_test))
    ridge_test_mae   = mean_absolute_error(y_test,  ridge.predict(X_test))
    ridge_test_rmse  = np.sqrt(mean_squared_error(y_test, ridge.predict(X_test)))
    print(f"  Train R²:  {ridge_train_r2:.4f}")
    print(f"  Test  R²:  {ridge_test_r2:.4f}")
    print(f"  Test  MAE: ${ridge_test_mae:.2f}B")
    print(f"  Test  RMSE:${ridge_test_rmse:.2f}B")

    # ── Train Decision Tree ────────────────────────────────────────
    print("\n🌳 Training Decision Tree (max_depth=4, min_samples_leaf=5)...")
    dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=5, random_state=42)
    dt.fit(X_train, y_train)

    dt_train_r2  = r2_score(y_train, dt.predict(X_train))
    dt_test_r2   = r2_score(y_test,  dt.predict(X_test))
    dt_test_mae  = mean_absolute_error(y_test,  dt.predict(X_test))
    dt_test_rmse = np.sqrt(mean_squared_error(y_test, dt.predict(X_test)))
    print(f"  Train R²:  {dt_train_r2:.4f}")
    print(f"  Test  R²:  {dt_test_r2:.4f}  ← expected negative (can't extrapolate time-series)")
    print(f"  Test  MAE: ${dt_test_mae:.2f}B")

    # ── Save artifacts ─────────────────────────────────────────────
    os.makedirs('models', exist_ok=True)
    os.makedirs('data',   exist_ok=True)

    joblib.dump(ridge,        'models/ridge_model.pkl')
    joblib.dump(dt,           'models/dt_model.pkl')
    joblib.dump(feature_cols, 'models/feature_names.pkl')

    metrics = {
        'ridge': {
            'train_r2':   ridge_train_r2,
            'test_r2':    ridge_test_r2,
            'train_mae':  mean_absolute_error(y_train, ridge.predict(X_train)),
            'test_mae':   ridge_test_mae,
            'train_rmse': np.sqrt(mean_squared_error(y_train, ridge.predict(X_train))),
            'test_rmse':  ridge_test_rmse,
        },
        'dt': {
            'train_r2':   dt_train_r2,
            'test_r2':    dt_test_r2,
            'train_mae':  mean_absolute_error(y_train, dt.predict(X_train)),
            'test_mae':   dt_test_mae,
            'train_rmse': np.sqrt(mean_squared_error(y_train, dt.predict(X_train))),
            'test_rmse':  dt_test_rmse,
        }
    }
    joblib.dump(metrics, 'models/metrics.pkl')

    # Save cleaned data
    df.to_csv('data/tanzania_gdp_clean.csv', index=False)

    print("\n" + "=" * 60)
    print("✅ Done! Artifacts saved:")
    print("  models/ridge_model.pkl")
    print("  models/dt_model.pkl")
    print("  models/feature_names.pkl")
    print("  models/metrics.pkl")
    print("  data/tanzania_gdp_clean.csv")
    print("=" * 60)
    print(f"\n🏆 Recommended model: Ridge Regression")
    print(f"   Test R² = {ridge_test_r2:.4f} on 2020–2024 holdout")

if __name__ == "__main__":
    train_and_save_models()
