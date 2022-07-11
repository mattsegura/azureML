# Create and run an AutoML Experiment using SDK
# 1. Access the workspace
# 2. Get the input data from the workspace or another source
# 3. Create or access the compute cluster
# 4. Configure the AutoML
# 5. Submitthe AutoML experiment


# Import required libraries
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import Input

from azure.ai.ml import automl

credential = DefaultAzureCredential()
ml_client = None

# connect via config.json
try:
    ml_client = MLClient.from_config(credential)
# else connect via file
except Exception as ex:
    print(ex)
    # Enter details of your AzureML workspace
    subscription_id = "c97ade30-785d-478d-9bba-b114901e95c9"
    resource_group = "AzuremL0002"
    workspace = "Azureml-testing001ws"
    ml_client = MLClient(credential, subscription_id, resource_group, workspace)

"""Data Source and format:
1. Data must be in tabular form
2. Value to predict, target column, must be in the data...
"""

# Show Azure ML Workspace Information
workspace = ml_client.workspaces.get(name=ml_client.workspace_name)

output = {}
output["Workspace"] = ml_client.workspace_name
output["Subscription ID"] = ml_client.connections._subscription_id
output["Resource Group"] = workspace.resource_group
# output["Location"] = workspace.location


# A. Create MLTable for training data from your local directory
my_training_data_input = Input(type=AssetTypes.MLTABLE, path="./data/")


# B. Remote MLTable definition
# my_training_data_input  = Input(type=AssetTypes.MLTABLE, path="azureml://datastores/workspaceblobstore/paths/Classification/Train")

# general job parameters
compute_name = "gpu-cluster"
exp_name = "dpv2-nlp-text-classification-experiment"
dataset_language_code = "eng"

# Create the AutoML job with the related factory-function.

text_classification_job = automl.text_classification(
    compute=compute_name,
    # name="dpv2-nlp-text-classification-multiclass-job-01",
    experiment_name=exp_name,
    training_data=my_training_data_input,
    target_column_name="Sentiment",
    primary_metric="accuracy",
    tags={"my_custom_tag": "My custom value"},
)

text_classification_job.set_limits(timeout_minutes=120)

text_classification_job.set_featurization(dataset_language=dataset_language_code)

# Submit the AutoML job

returned_job = ml_client.jobs.create_or_update(
    text_classification_job
)  # submit the job to the backend

print(f"Created job: {returned_job}")

ml_client.jobs.stream(returned_job.name)
