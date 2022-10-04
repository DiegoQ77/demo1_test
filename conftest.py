def pytest_addoption(parser):
    parser.addini("rmse", "Min RMSE score for a model to past post-train test")
    parser.addini(
        "inference_time", "Max inference time for the model to be making predictions"
    )
