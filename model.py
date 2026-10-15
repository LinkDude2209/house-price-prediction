def predict_price(features):
    """Placeholder for house price prediction."""
    return None


def train_model(X, y):
    """Train a linear regression model."""
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(X, y)
    return model
