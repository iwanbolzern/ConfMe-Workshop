FROM 141502667606.dkr.ecr.eu-west-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3
COPY poetry* .

RUN pip uninstall -y typing
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install
