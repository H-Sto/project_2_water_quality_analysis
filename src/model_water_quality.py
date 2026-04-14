"""Basic modelling for water quality prediction."""

# First modelling task:
# Predict dissolved oxygen from water temperature
# using a simple linear regression model.

# Target variable (y):
# dissolved_oxygen_mg_l

# Predictor variable (X):
# water_temp_c

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "water_quality_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

def load_data(path:Path) -> pd.DataFrame:
    """Load the cleaned water quality dataset"""
    df = pd.read_csv(path)
    return(df)

def prepare_modelling_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select and clean the variables needed for regression modelling"""
    model_df = df[["water_temp_c", "salinity_ppt", "ph", "water_depth_m", "dissolved_oxygen_mg_l"]].copy()
    model_df = model_df.dropna()
    return model_df

def split_features_target(model_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Split the modelling dataframe into predictor (X) and target (Y)"""
    X = model_df[["water_temp_c", "salinity_ppt", "ph", "water_depth_m"]]
    y = model_df["dissolved_oxygen_mg_l"]
    return X,y

def split_train_test(X: pd.DataFrame, y: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Split the data into training and testing sets"""
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Train a linear regression model"""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def make_predictions(model: LinearRegression, X_test: pd.DataFrame) -> pd.Series:
    """Generate predictions using the trained model"""
    y_pred = model.predict(X_test)
    return y_pred

def evaluate_model(y_test: pd.Series, y_pred: pd.Series) -> None:
    """Evaluate the model performance"""
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test,y_pred)

    print("R^2 score:", r2)
    print("Mean Absolute Error:", mae)

def main() -> None:
    df = load_data(DATA_PATH)
    model_df = prepare_modelling_data(df)

    print("Modelling dataset shape:")
    print(model_df.shape)
    print(model_df.head())

    X, y = split_features_target(model_df)

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    print(X.head())
    print(y.head())

    X_train, X_test, y_train, y_test = split_train_test(X, y)

    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    model = train_model(X_train, y_train)
    print("Model intercept:", model.intercept_)
    print("Model coefficients:")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"{feature}: {coef}")

    y_pred = make_predictions(model, X_test)
    print("Predictions:")
    print(y_pred[:5])

    evaluate_model(y_test, y_pred)

if __name__ == "__main__":
    main()